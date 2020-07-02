import bs4
import requests
import pandas as pd
import re
import argparse
from tqdm import tqdm


# python diseases_components_scraper.py -c basic -i diseases.csv -o disease_components.csv

class utilities:
    """
    Provides basic utility functions
    """

    def convert_to_list(self, obj):
        my_list = []
        for items in obj:
            my_list.append(items)
        return my_list

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3


class basic_diseases_data:
    """
    Scrape basic features for given diseases.
    Basic features include Symptoms, Overview,Risk factors, and Causes
    """

    def __init__(self, url, soup_obj):
        self.url = url
        self.soup_obj = soup_obj

    def get_basic_components(self, component):
        """
        Scrapes the basic components 
        """

        head_s = self.soup_obj.find("h2", text=re.compile(component))
        if (head_s == None):
            return 'NA'
        else:
            head_c = head_s.find_next("h2")

        obj1_p = head_s.find_all_next("p")
        obj1_l = head_s.find_all_next("li")
        obj2_p = head_c.find_all_previous("p")
        obj2_l = head_c.find_all_previous("li")

        utl = utilities()

        list1 = utl.convert_to_list(obj1_p)
        list2 = utl.convert_to_list(obj1_l)
        list3 = utl.convert_to_list(obj2_p)
        list4 = utl.convert_to_list(obj2_l)

        list_one = utl.intersection(list1, list3)
        list_two = utl.intersection(list2, list4)

        unwanted = ['Twitter', 'Diseases & Conditions',
                    'Patient Care & Health Information', 'Facebook', 'Pinterest', 'YouTube']

        comp_list = [*list_one, *list_two]

        comp1 = []

        for i in range(0, len(comp_list)):
            comp1.append(comp_list[i].text)

        comp = [sa for sa in comp1 if not any(sb in sa for sb in unwanted)]

        return comp


class other_data:
    """
    Scrapes remedies, diagnosis, treatment, medication 
    """

    def __init__(self, url, soup_obj):
        self.url = url
        self.soup_obj = soup_obj

    def get_remedies_or_diagnosis(self, comp):
        """
        Scrapes : 
        Lifestyle and home remedies
        Diagnosis
        """
        a = self.soup_obj

        if (a == None):
            return "NA"

        home = "https://www.mayoclinic.org/"
        link = home + a.get("href")

        res = requests.get(link, headers=agent)
        soup = bs4.BeautifulSoup(res.text, 'html5lib')

        head_s = soup.find("h2", text=re.compile(comp))

        if (head_s == None):
            return 'NA'
        else:
            head_c = head_s.find_next("h2")

        obj1_p = head_s.find_all_next("p")
        obj1_l = head_s.find_all_next("li")
        obj1_s = head_s.find_all_next("strong")

        obj2_p = head_c.find_all_previous("p")
        obj2_l = head_c.find_all_previous("li")
        obj2_s = head_c.find_all_previous("strong")

        utl = utilities()

        list1 = utl.convert_to_list(obj1_p)
        list2 = utl.convert_to_list(obj1_l)

        list3 = utl.convert_to_list(obj2_p)
        list4 = utl.convert_to_list(obj2_l)

        list5 = utl.convert_to_list(obj1_s)
        list6 = utl.convert_to_list(obj2_s)

        list_one = utl.intersection(list1, list3)
        list_two = utl.intersection(list2, list4)
        list_three = utl.intersection(list5, list6)

        unwanted = ['Twitter', 'Diseases & Conditions',
                    'Patient Care & Health Information', 'Facebook', 'Pinterest', 'YouTube']

        other_list = [*list_one, *list_two, *list_three]

        other1 = []

        for i in range(0, len(other_list)):
            other1.append(other_list[i].text)

        other = [sa for sa in other1 if not any(sb in sa for sb in unwanted)]

        return other

    def get_treatment(self):
        """
        Scrapes treatment for diseases.
        """

        a = self.soup_obj

        if (a == None):
            return "NA"

        home = "https://www.mayoclinic.org/"
        link = home + a.get("href")

        res = requests.get(link, headers=agent)
        soup = bs4.BeautifulSoup(res.text, 'html5lib')

        head_s = soup.find("h2", text=re.compile("Treatment"))

        if (head_s == None):
            return 'NA'
        else:
            head_c = head_s.find_next("h3")

        obj1_p = head_s.find_all_next("p")
        obj1_l = head_s.find_all_next("li")
        obj1_s = head_s.find_all_next("strong")

        obj2_p = head_c.find_all_previous("p")
        obj2_l = head_c.find_all_previous("li")
        obj2_s = head_c.find_all_previous("strong")

        utl = utilities()

        list1 = utl.convert_to_list(obj1_p)
        list2 = utl.convert_to_list(obj1_l)

        list3 = utl.convert_to_list(obj2_p)
        list4 = utl.convert_to_list(obj2_l)

        list5 = utl.convert_to_list(obj1_s)
        list6 = utl.convert_to_list(obj2_s)

        list_one = utl.intersection(list1, list3)
        list_two = utl.intersection(list2, list4)
        list_three = utl.intersection(list5, list6)

        unwanted = ['Twitter', 'Diseases & Conditions',
                    'Patient Care & Health Information', 'Facebook', 'Pinterest', 'YouTube']

        treatment_list = [*list_one, *list_two, *list_three]

        treatment1 = []

        for i in range(0, len(treatment_list)):
            treatment1.append(treatment_list[i].text)

        treatment = [sa for sa in treatment1 if not any(
            sb in sa for sb in unwanted)]

        return treatment

    def get_medication(self):
        """
        Scrapes medication for diseases.
        """

        a = self.soup_obj

        if (a == None):
            return "NA"

        home = "https://www.mayoclinic.org/"
        soup = bs4.BeautifulSoup(requests.get(
            home + a.get("href"), headers=agent).text, 'html5lib')

        head_s = soup.find("h3", text=re.compile("Medications"))

        if (head_s == None):
            return 'NA'
        else:
            head_c = head_s.find_next("div")

        obj1_p = head_s.find_all_next("p")
        obj1_l = head_s.find_all_next("li")
        obj1_s = head_s.find_all_next("strong")

        obj2_p = head_c.find_all_previous("p")
        obj2_l = head_c.find_all_previous("li")
        obj2_s = head_c.find_all_previous("strong")

        utl = utilities()

        list1 = utl.convert_to_list(obj1_p)
        list2 = utl.convert_to_list(obj1_l)

        list3 = utl.convert_to_list(obj2_p)
        list4 = utl.convert_to_list(obj2_l)

        list5 = utl.convert_to_list(obj1_s)
        list6 = utl.convert_to_list(obj2_s)

        list_one = utl.intersection(list1, list3)
        list_two = utl.intersection(list2, list4)
        list_three = utl.intersection(list5, list6)

        unwanted = ['Twitter', 'Diseases & Conditions',
                    'Patient Care & Health Information', 'Facebook', 'Pinterest', 'YouTube']

        medication_list = [*list_one, *list_two, *list_three]

        medication1 = []

        for i in range(0, len(medication_list)):
            medication1.append(medication_list[i].text)

        medication = [sa for sa in medication1 if not any(
            sb in sa for sb in unwanted)]

        return medication


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Scraper to get basic and other data for diseases.")
    parser.add_argument("-components", choices=['basic', 'remedies', 'diagnosis', 'treatment', 'medication'],
                        help="Enter the components that you would like to scrape", dest="comp", type=str, required=True)
    parser.add_argument("-inpfile", help="Enter file containing diseases urls .",
                        dest="inp", type=str, required=True)
    parser.add_argument("-opfile", help="Enter file name for storing the scraped diseases data.",
                        dest="op", type=str, required=True)

    args = parser.parse_args()

    comp = args.comp
    inp_fname = args.inp
    op_fname = args.op

    df_diseases = pd.read_csv(inp_fname)

    # drop duplicate links from the dataset as multiple diseases can map to the same page
    df_diseases.drop_duplicates(subset="link", keep="last", inplace=True)

    agent = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    # basic components
    if (comp == 'basic'):

        grp1 = ["Symptoms", "Overview", "Causes", "Risk factors"]
        for co in grp1:
            tqdm.pandas(desc=co)
            df_diseases[co] = df_diseases['link'].progress_apply(lambda x:
                                                                 basic_diseases_data(x, bs4.BeautifulSoup(requests.get(
                                                                     x, headers=agent).text, 'html5lib')).get_basic_components(co),
                                                                 )
            print("Scraped " + co + " !!")

    # Remedies
    elif (comp == 'remedies'):
        tqdm.pandas(desc=comp)
        df_diseases[comp] = df_diseases['link'].progress_apply(lambda x:
                                                               other_data(x, bs4.BeautifulSoup(requests.get(x, headers=agent).text, 'html5lib').find(
                                                                   id="et_genericNavigation_diagnosis-treatment")).get_remedies_or_diagnosis('Lifestyle and home remedies'),
                                                               )
        print("Scraped " + comp + " !!")

    # diagnosis
    elif (comp == 'diagnosis'):
        tqdm.pandas(desc=comp)
        df_diseases[comp] = df_diseases['link'].progress_apply(lambda x:
                                                               other_data(x, bs4.BeautifulSoup(requests.get(x, headers=agent).text, 'html5lib').find(
                                                                   id="et_genericNavigation_diagnosis-treatment")).get_remedies_or_diagnosis('Diagnosis'),
                                                               )
        print("Scraped " + comp + " !!")

    # treatment
    elif (comp == 'treatment'):
        tqdm.pandas(desc=comp)
        df_diseases[comp] = df_diseases['link'].progress_apply(lambda x:
                                                               other_data(x, bs4.BeautifulSoup(requests.get(x, headers=agent).text, 'html5lib').find(
                                                                   id="et_genericNavigation_diagnosis-treatment")).get_treatment(),
                                                               )
        print("Scraped " + comp + " !!")

    # medication
    elif (comp == 'medication'):
        tqdm.pandas(desc=comp)
        df_diseases[comp] = df_diseases['link'].progress_apply(lambda x:
                                                               other_data(x, bs4.BeautifulSoup(requests.get(x, headers=agent).text, 'html5lib').find(
                                                                   id="et_genericNavigation_diagnosis-treatment")).get_medication(),
                                                               )
        print("Scraped " + comp + " !!")

    # save dataframe
    df_diseases.to_csv(op_fname, index=False)

import bs4
import requests
import pandas as pd
import argparse
from tqdm import tqdm

# python disease_names_and_urls_scraper.py -fname diseases.csv

def get_alphabet_links(s,home):
    """
    returns:
    list = links for pages for each alphabet
    """
    alphabets =[]
    for link in s:
        alphabets.append(link.get('href'))
    
    links_alphabets=[]
    print("Getting links for alphabets..")
    for i in tqdm(range(0,len(alphabets))):
        if len(alphabets[i])>27 and alphabets[i][27]=='l' and alphabets[i][1]=='d':
            links_alphabets.append(home + alphabets[i])
    
    return links_alphabets

def get_diseases_dataframe(links_alphabets,df_name):
    """
    Scrapes disease names and their urls and stores in  csv file.
    """
    
    df_diseases = pd.DataFrame(columns=['name','link'])
    
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    print("Scraping disease names and urls..")
    for i in tqdm(range(0,len(links_alphabets))):
        alpha = links_alphabets[i]
        res2 = requests.get(alpha,headers=agent)
        soup = bs4.BeautifulSoup(res2.text,'html5lib')
        det = soup.find("div",id="index")
        names = det.find_all('li')

        for item in names:
            link = home + item.find('a').get("href")
            n = (item.text).strip()
            df_diseases = df_diseases.append({'name':n,'link':link},ignore_index=True)
            
    df_diseases.to_csv(df_name,index=False)
    print("Done!!!!")
    

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description="generate csv file containing diseases and their urls")
    parser.add_argument("-fname", help="Enter the name for csv file",dest="df_name", type=str, required=True)
    args = parser.parse_args()
    df_name = args.df_name
    
    home = "https://www.mayoclinic.org"
    res = requests.get(home)
    soup = bs4.BeautifulSoup(res.text,'html5lib')

    s = soup.find_all(attrs = { 'class' : 'access-alpha' })
    s = soup.find_all('a')
    
    alphabet_links = get_alphabet_links(s,home)
    
    get_diseases_dataframe(alphabet_links,df_name)

    

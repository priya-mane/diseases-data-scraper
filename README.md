# Diseases-dataset-scraper

Scrapes diseases data from mayoclinic.org

***

## STEP 0

Install dependencies.

```
pip install -r requirements.txt 
```

***
## STEP 1

### Scrape disease names and urls to their respective pages

Parameters needed : 

* fname - name of file where the dataset has to be stored.

```
python disease_names_and_urls_scraper.py -fname <file_name>
```

This will create a csv file containing 2 columns - 
* names of diseases. 
* url to the dedicated page for respective diseases. 

<u> Example </u> : 

```
python disease_names_and_urls_scraper.py -fname diseases.csv
```

![sample op](imgs/name_urls_sample.jpg)

***
## STEP 2

### Scrape disease components

The disease components are divided into 5 groups : 

1. basic (includes Symptoms, Overview, Causes and Risk factors)
2. diagnosis 
3. treatment 
4. remedies 
5. medication

The user can choose from above to add the respective component to the dataset as per his/her need.

Parameters needed:

* component - one of the 5 components mentioned above

* inpfile - name of the file containing disease names and urls (generated in Step 1)

* opfile - file to store the data scraped for component selected.

```
python diseases_components_scraper.py -c <component> -i <diseases_url_filename> -o <output_file_for_components>
```

<u> Example </u> : 

```
python diseases_components_scraper.py -c basic -i diseases.csv -o disease_components.csv
```

![basic_scraped_ss](imgs/basic_op.jpg)

Adding diagnosis column to the existing dataframe

```
python diseases_components_scraper.py -c diagnosis -i disease_components.csv -o disease_components.csv
```

![diagnosis_ss](imgs/diagnosis.jpg)


Dataset so far as per above execution : [Here](disease_components.csv)

***

NOTE : It is advised to build the dataset as required using the  separate commands mentioned above for each component as it takes a long time to execute the operation. 

***

## Check out the complete scraped data on Kaggle !

[Diseases dataset](https://www.kaggle.com/priya1207/diseases-dataset)






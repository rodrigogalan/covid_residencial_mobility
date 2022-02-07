# Data-covid-residential-movility

En este proyecto se ha importado un data set de [Kaggle](https://www.kaggle.com/aestheteaman01/people-staying-in-home-during-covid19) sobre las preferencias de la población en torno a estar en casa respecto momentos previos al COVID. Posteriormente se ha creado una función para el scrapeo de datos de Yahoo finance y se han scrapeado los datos de diferentes compañías. Por último se han añadido todos los datos recopilados a un database en SQL.
***
## Método
1. Descarga e importación del .csv como pandas data frame.



## Documentos
### Jupyter notebooks
* [1-data_collection.ipynb](https://github.com/rodrigogalan/data-covid_residencial_mobility/blob/main/1-data_collection.ipynb)
* [2.data_uploading.ipynb](https://github.com/rodrigogalan/data-covid_residencial_mobility/blob/main/2.data_uploading.ipynb)
### Data
* [Worldwide Residential Mobility in COVID-19](https://www.kaggle.com/aestheteaman01/people-staying-in-home-during-covid19): datos limpios
### Functions
* [src/scraping_functions.py](https://github.com/rodrigogalan/data-covid_residencial_mobility/blob/main/src/scraping_functions.py)

## Librerias
* [re](https://github.com/python/cpython/blob/3.10/Lib/re.py) 
* [numpy](https://numpy.org/doc/1.22/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/) 
* [sys](https://github.com/python/cpython/blob/3.10/Doc/library/sys.rst)
 * requests
 * selenium
 * sqlalchemy
 * datetime


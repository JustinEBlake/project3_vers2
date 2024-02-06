# Data Engineering Project

## Overview
- In this project, we explore the processes involved in data engineering to create an effective database system. The focus is on collecting and storing performance data for companies based on their stock symbol. The data engineering process includes extracting information from different sources, transforming the data to make it usable, and then loading the transformed data into a SQLite database. This engineering of data aims to enhance its usefulness and accessibility for end-users.

## Instructions ([etl.py](https://github.com/JustinEBlake/project3_vers2/blob/main/etl.py))
1. Install dependencies.
1. Update `company_tickers` with the specific company symbols. 
1. Run python app to create Database according to the ERD.



## Streamlit App
- [Financial Database App](https://group2proj3.streamlit.app) that allows users to read/ analyze data in the sqlite database.


## Dependencies
- [Finhubb](https://finnhub.io) needed to get company names
     ```sh
     pip install finnhub-python
     ```


- [Yfinance]() to get all financial data
    ```sh
    pip install yfinance
    ``````

- [Streamlit](https://streamlit.io) for front-end
    ```sh
    pip install streamlit
    ```

## Ethical Considerations
- Given that all the data is public information, we felt confident that we were not in violation of any ethical laws. 

## ERD
![ERD](misc/erd.png)


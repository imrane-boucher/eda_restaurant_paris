# Exploratory Data Analysis - Where to find the best value restaurants in Paris ?

## Background:

I have been studying for a year in Paris now and something I really enjoy is going out with friends to a restaurant. However for newcomers it can be hard to know where to look when searching for a restaurant. Infact they are plenty of good restaurants in Paris but you want to be able to get good price for value, and avoid touristic destinations while still benefiting from a nice and attractive area. 
This exploratory analysis aims to provide some guidelines for newcomers in Paris by highlighting the best "arrondissement" where you can find value restaurants, as well as helping me and my friend to find better restaurants at a better price.

## Project Overview:

* Collected data about close to 1000 restaurants using Yelp's API
* Cleaned the data and performed feature engeenering to extract some valuable information (ex: street of the restaurant)
* Performed a statiscal and geographical analysis using python and folium to find the best areas for value restaurants in Paris 
* Came up with two "arrondissement" to recommend based on the value of the restaurants and the attractiveness of the aera

## Code and Ressources used:

**Python version:** 3.8

**Packages:** `requests, Pandas, json, ast, re, NumPy, matplotlib, seaborn, folium, qgrid`

**Inspiration:** this project was inspired by justinmlam's work who did an [analysis of restaurants in Vancouver](https://github.com/justinmlam/foodcouver) using folium

**Using Yelp's API:** https://learn.co/lessons/python-api-intro-yelp

## Exploratory Data Analysis:

### Statistical Analysis:

![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/top_categories_restaurants.png) ![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/avg_price_busy_streets.png)

**Main findings**:
* The global ranking of restaurants in Paris seem pretty good. It is something we were quite expecting since France is a country known for the quality of its cuisine
* 'Rue du Temple' seems to have relatively good rating restaurants for a relatively low price in comparisson to the other four 'busiest streets' (these streets are top streets ranked by the number of restaurants in the dataset)

### Geographical Analysis:

* Areas classfied by the number of restaurants 

![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/map_nber_restaurants.PNG)

* Areas classified by the average quality price ratio of the restaurants 

![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/map_avg_quality_ratio.PNG)

**Main findings**:
* They seem to be far more restaurants in the 1st arrondissement compared to the others. This result should be interpreted with caution. In fact we are only analysing a sample (877) of the total number of restaurants in Paris.
* The west part of Paris as well as the 8th arrondissement definitely seems a bad choice to pick a restaurant since they give the worse value for money. If the far east seems to present an attractive quality price ratio, I will avoid this area since it is pretty far from the center. 
* **My recommandation based on this analysis would therefore be to look for a restaurant in the 3rd Arrondissement or in the 5th since they have an attractive location while still hosting good value for money restaurants.**

## Legacity:

This project is a personal work for non commercial use only.
The Yelp's API terms can be find here : https://www.yelp.com/developers/api_terms

## Further work:

* The final analysis was based on 877 restaurants. I intend in the future to replicate this analysis on a larger sample (to get closer of the actual population) and verify it this current analysis holds on
* I focused my analysis on trying to find the best location for value restaurants, I could instead try to find the location where I can find the highest vegan quality restaurants (which might be useful when taking out my girl friend)
* I could precise my analysis on categories of restaurants and explore which categories are bring the best value for price etc.
* Finally I project on analysing the restaurant scene in other big cities 

# Exploratory data analysis - Where to find the best value restaurants in Paris ?

### Background:

I have been studying for a year in Paris now and something I really enjoy is going out with friends to a restaurant. However for newcomers it can be hard to know where to look when searching for a restaurant. Infact they are plenty of good restaurants in Paris but you want to be able to get good price for value, and avoid touristic destinations while still benefiting from a nice and attractive area. 
This exploratory analysis aims to provide some guidelines for newcomers in Paris by highlighting the best "arrondissement" where you can find value restaurants, as well as helping me and my friend to find better restaurants at a better price.

### Project Overview:

* Collected data about close to 1000 restaurants using Yelp's API
* Cleaned the data and performed feature engeenering to extract some valuable information (ex: street of the restaurant)
* Performed a statiscal and geographical analysis using python and folium to find the best areas for value restaurants in Paris 
* Came up with two "arrondissement" to recommend based on the value of the restaurants and the attractiveness of the aera

### Code and Ressources used:

**Python version:** 3.8

**Packages:** `requests, Pandas, json, ast, re, NumPy, matplotlib, seaborn, folium, qgrid`

**Inspiration:** this project was inspired by justinmlam's work who did an [analysis of restaurants in Vancouver](https://github.com/justinmlam/foodcouver) using folium

**Using Yelp's API:** https://learn.co/lessons/python-api-intro-yelp

### EDA:

#### Stastical analysis:

![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/top_categories_restaurants.png) ![alt text](https://github.com/imrane-boucher/eda_restaurant_paris/blob/master/images/avg_price_busy_streets.png)


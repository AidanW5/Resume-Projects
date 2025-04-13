

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests


#Web page
source = requests.get('https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table').text

soup = BeautifulSoup(source, 'lxml')


#Find table needed
table = soup.find_all('tbody')[3]


#Find all <a> tags in table
a_tags = table.find_all('a')

#Put country names in list
country_list = []

for a in a_tags:
    country = a.text
    country_list.append(country)


#Find all <td> tags in table                        
td_tags = table.find_all('td')

#Put total medals of each country in list
medal_list = []

for td in td_tags:
    medals = td.text
    medal_list.append(medals)
    

#Remove countries that are not in the top 20
new_medal_list = medal_list[4:100:5] 

#Turn medal_list type to integers
new_medal_list = list(map(int, new_medal_list))


#Combine country_list and new_medal_list
country_medals = dict(zip(country_list, new_medal_list))


#Dictionary to store countries with 20 or more medals
new_country_medals = {}

for country_medal in country_medals:
        
    if country_medals[country_medal] >= 20:
        new_country_medals[country_medal] = country_medals[country_medal]
    
    else:
        pass
    
    
#Sort dictionary by greatest value
sorted_country_medals = sorted(new_country_medals.items(), key=lambda x: x[1], reverse=True)

#Change sorted_country_medals from tuple back to dictionary
sorted_country_medals = dict(sorted_country_medals)

#Plot dictionary
plt.title("Countries With The Most Medals 2024")

plt.bar(sorted_country_medals.keys(), sorted_country_medals.values(), edgecolor="black")


plt.show()

    

        








    



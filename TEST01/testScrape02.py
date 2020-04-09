import requests
from bs4 import BeautifulSoup
# import urllib.request

url = "https://forecast.weather.gov/MapClick.php?lat=21.29419000000007&lon=-157.78723499999998#.XoBVXNNKiQU"

# response object
page = requests.get(url)

# bs instance - instantiates a web scraper
soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify()) #formats html output 

week = soup.find(id="seven-day-forecast-body") #finds all elements with id=""

# print(week) #test 
# print(week.find_all("li")) #prints all list tags in week 

items = week.find_all(class_ = "tombstone-container")
# print(items[1]) #prints second item in list

# print(items[0].find(class_ = "period-name").get_text())

# for each item in items as loop through find the period name add to list
period_names = [item.find(class_ = "period-name").get_text() for item in items]
print(period_names)
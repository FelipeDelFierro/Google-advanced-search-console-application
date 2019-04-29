Python modules
import time
import sys

#Script modules:
from Countries import GetCountry,countries
from Dates import GetDate
from Languages import GetLanguage, Languages
from UrlBuilder import url_builder, url_builder_SpecificSite
from Crawler import scraping
from Export_csv import export_csv

totalUrlBuilder = []
print (5 * "-" , "Welcome to the advanced Web search console. Just follow instrucions and enjoy !",5 * "-","\n")
print ("Fist step : Choice your Country\n")
print ("Second step: Choice your Language\n")
print ("Third step: Choice your Range of time to search\n")
print ("Quarter step: Choice your keywords and badwords\n")
print ("Fifth step: If there are results, go to folder where is this script and your csv file will be there with results\n")
input("Press any key to start the game!...")

#user parameters   
country = GetCountry(countries)
language = GetLanguage(Languages)
date = GetDate()
#start query
UserResponse=input("Do you want to search in a specific website?").capitalize()
if UserResponse=='Y':
    while UserResponse =='Y':
        url = url_builder_SpecificSite(country,language,date)
        totalUrlBuilder.append(url)
        UserResponse = input("Do you want to create more queries in other website? [ Y / Any key]").capitalize()
UserResponse=input("Do you want to search in all the web?").capitalize()
while UserResponse =='Y':
    url = url_builder(country,language,date)
    totalUrlBuilder.append(url)
    UserResponse = input("Do you want to create more queries? [ Y / Any key]").capitalize()   
else:
    print("Fetching Results...") 
    found_results=scraping(totalUrlBuilder)
    count = len(found_results)
    print( "there are "+  " " + str(count) + " found results in your search")
    print("these are your url queries. You can copy each one and paste into your browser: "+ str(totalUrlBuilder))
    export_csv(found_results)  
input("Press any key for exit")
sys.exit(0)









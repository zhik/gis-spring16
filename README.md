#cartographic studio for spring 16 

##locations.py
to get a .csv file of the location and types of mcdonalds using zipcodes 
not efficient at all but works

uses selenium + chromedriver

notes:
- if there is a ton of errors increase the sleep
- using all the zipcodes is not recommended (takes a while) 
- mcdonalds uses googleapps, so data could be pulled directly from json. (this doesn't do it)
- geocoding could be improved upon

##data/
1. fixed_mcd_locations.csv- contains all the mcdonalds locations in NYC - with fixes

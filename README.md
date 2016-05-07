#cartographic studio for spring 16 
Do low-income zones contain more [stores] in walking/driving distance than higher-income zones in Manhattan? 

1. get locations of stores , income data and streets of NYC
2. buffer stores using drive-time areas
3. count the amount of stores in a income area
4. look for correlation and make the map pretty 

##mcd_locations.py
gets a .csv file of the location and types of mcdonalds using zipcodes ,not very efficient but works

uses selenium + chromedriver 

notes:
- if there is a ton of errors increase the sleep
- using all the zipcodes is not recommended (takes a while) 
- mcdonalds uses googleapps, so data could be pulled directly from json. (not done)

##data/
1. mc_locations- contains all the mcdonalds locations in NYC - with fixes

#not efficient at all !!! but works :)
from selenium import webdriver
import geocoder
import csv
import time

store_list = []
#get a list of zipcodes 
with open('zipcodes.txt', 'r') as f:
	for line in f:
		zipcodes = (line.split())
print "there are", len(zipcodes), "zipcodes"

browser = webdriver.Chrome('chromedriver.exe')
# url = 'http://www.nycbynatives.com/nyc_info/new_york_city_zip_codes.php'
# browser.get(url)
# time.sleep(.1)
# zipcodes = [] 
# count = 0
# #range depends
# for number in range(1,240):
# 	number = str(number)
# 	zipcodes.append(browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/table/tbody/tr['+number+']/td[1]').text.encode("utf-8"))
# 	zipcodes.append(browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/table/tbody/tr['+number+']/td[4]').text.encode("utf-8"))
# 	count += 2
# print "there are",count,"zipcodes"
# with open('zipcodes.txt', 'wb') as f:
# 	for zipcode in zipcodes:
# 		f.write(zipcode + " ")


#find stores with those zipcodes
count = 0
for zipcode in zipcodes:
	url = 'https://rl.mcdonalds.com/googleapps/GoogleSearchUSAction.do?method=googlesearchLocation&primaryCity='\
	+ zipcode +'&postalCode=&country=us&language=en'
	browser.get(url)
	time.sleep(1)
	try:	
		for number in ('1','2','3','4','5'):
			storename = browser.find_element_by_xpath('//*[@id="results"]/table/tbody['+number+']/tr/td[2]/h3').text
			storetype = browser.find_element_by_xpath('//*[@id="results"]/table/tbody['+number+']/tr/td[4]').text
			if browser.find_elements_by_xpath('//*[@id="results"]/table/tbody['+number+']/tr/td[5]/div') != []:
				storeplay = True
			else:
				storeplay = False
			if browser.find_elements_by_xpath('//*[@id="results"]/table/tbody['+number+']/tr/td[6]/div') != []:
				storedrive = True
			else:
				storedrive = False
			storelatlng = geocoder.arcgis(storename+" New York").latlng
			storefull = [storename.encode("utf-8"), storetype.encode("utf-8"), storeplay, storedrive, storelatlng]
			if storefull not in store_list:
				store_list.append(storefull)
				if storelatlng == []:
					print "lat-long for", storename, "is not found"
		count += 1
	except:
		print zipcode, "error!, no such thing :", str(count)
	else:
		print zipcode, "is done :", str(count)

browser.close()

#write all results to .csv
with open('data/mc_locations.csv', 'wb') as f:
	csv.writer(f).writerow(['location','type','playplace','drive-thur', 'latlng'])
	for row in store_list:
		csv.writer(f).writerow(row)

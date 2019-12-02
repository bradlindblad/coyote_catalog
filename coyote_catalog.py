# -*- coding: utf-8 -*-


#! /usr/bin/python3

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time



## READ URLS TO ITER OVER -------------------------------------------------------

with open('counties.txt') as f:
    counties = f.read().splitlines()


## FOR EACH PAGE ----------------------------------------------------------------

def page_iter(county):

    driver = webdriver.Chrome()

	# open url from list
    driver.get("https://gfappspublic.nd.gov/HunterContact/huntercontact.asp")
    time.sleep(3)

	# get episode number - save
    license = driver.find_element_by_xpath("//*[(@id = 'OLN')]")
    license.click()
    license.send_keys("OLN04897404")
    time.sleep(1)

    lastn = driver.find_element_by_xpath("//*[(@id = 'lkLastName')]")    
    lastn.click()
    lastn.send_keys("Lindblad")
    time.sleep(1)
    
    submit = driver.find_element_by_xpath("//*[(@id = 'retrieve')]")
    submit.click()
    time.sleep(3)
    
    species = driver.find_element_by_xpath("//*[(@id = 'speciesnew')]")  
    species.click()
    species.send_keys("coyote")
    
    unit = driver.find_element_by_xpath("//*[(@id = 'unitnew')]")
    unit.click()
    unit.send_keys(county)
    time.sleep(2)
	
    submitfinal = driver.find_element_by_xpath("//*[(@id = 'submit2')]")
    submitfinal.click()
    time.sleep(2)
    
    print(county + " county has been submitted..")
    
    driver.close()

## RUN PROGRAM ------------------------------------------------------------------
if __name__ == '__main__':
    for county in counties:
        page_iter(county)


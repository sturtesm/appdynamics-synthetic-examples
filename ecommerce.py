#!/usr/bin/python

import time
import re    
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:

    driver.get('http://ec2-52-88-18-250.us-west-2.compute.amazonaws.com/appdynamicspilot/')
    time.sleep(1)

    elem = driver.find_element_by_css_selector('#textBox') # Find the username login box
    elem.send_keys('tom.hardy@foobar.com')
    time.sleep(1)

    elem = driver.find_element_by_css_selector('#password') # Find the password text box
    elem.send_keys('jokerhardy')
    time.sleep(1)
    elem.send_keys(Keys.ENTER)

    #this should find the first book in the table list, and then we'll add it to cart
    elem = driver.find_element_by_css_selector('tbody > tr:first-child > td:nth-of-type(1) > div.itemBoxes > div.Cart > input')
    elem.click()
    time.sleep(1)

    #this should find the second book in the table list, and then we'll add it to cart
    elem = driver.find_element_by_css_selector('tbody > tr:first-child > td:nth-of-type(2) > div.itemBoxes > div.Cart > input')
    elem.click()
    time.sleep(1)

    #now add the selected books to the cart
    elem = driver.find_element_by_css_selector('tr > td:nth-of-type(1) > div.buttonClass > input.submit')
    elem.click()
    time.sleep(1)
    
    s = driver.page_source
    assert "A Clockwork Orange" in s
    assert "The Goldfinch" in s

    print ("Successfully added 2 books to our Shopping Cart...")
    
    elem = driver.find_element_by_css_selector('#ViewCart_submitValue')
    elem.click()

    s = driver.page_source
    assert "Order ID" in s

    print ("Checkout completed, confirmed Order ID(s)")

    driver.close()
except:
    driver.close()

    print ("Unexpected error: ", sys.exc_info()[0])
    raise

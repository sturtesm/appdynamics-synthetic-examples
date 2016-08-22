from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()
#driver = webdriver.Ie("C:\\Tools\\Selenium\\IEDriverServer_Win32_2.53.0\\IEDriverServer.exe");

count = 0
while count < 250:
	driver.get("http://127.0.0.1/eum-error.html");
	count += 1;
	time.sleep(1);


driver.quit()

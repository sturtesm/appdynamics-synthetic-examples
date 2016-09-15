# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, sys, traceback, datetime

class SNOWLoginCreateApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://dev25989.service-now.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_s_n_o_w_login_create_app(self):
        driver = self.driver
        driver.get(self.base_url)

        wait = WebDriverWait(driver, 10)

        try:
            self.switch_to_iframe('gsft_main', 10)

            #make sure the iframe and the form is visible
            userNameElem = wait.until(EC.element_to_be_clickable((By.ID,'user_name')))
            passwordElem = wait.until(EC.element_to_be_clickable((By.ID,'user_password')))

            self.log(1, "Found user_name and user_password elements in login form")

            # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | gsft_main | ]]
            #userNameElem = driver.find_element_by_css_selector("#user_name")
            userNameElem.clear()
            userNameElem.send_keys("admin")

            #passwordElem = driver.find_element_by_css_selector("user_password")
            passwordElem.clear()
            passwordElem.send_keys("apm13ad3r")

            driver.find_element_by_id("sysverb_login").click()

            self.log(2, "Submitting login")

            filterElem = wait.until(EC.element_to_be_clickable((By.ID,'filter')))

            self.log(3, "Found filter, searching for applications link")


            # filters the list of menu items to find the 'create application' item
            filterElem.click()
            filterElem.clear()
            filterElem.send_keys("applications")

            #clicks on the 'Applications' link
            applicationsElem = wait.until(EC.element_to_be_clickable((By.ID, '8c021ad2d70221004a1dcdcf6e6103f9')))
            applicationsElem.click()

            self.log(4, "Found applications link")

            #selects that we want to create a new app
            self.switch_to_iframe('gsft_main', 10)

            newAppButtonElem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary')))
            newAppButtonElem.click()

            self.log(5, "Found and selected 'New' application button")

            #multiple creates, but the first is to create from scratch
            #self.switch_to_iframe('gsft_main', 10)

            createAppElem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tbody > tr:first-child > td:nth-of-type(3) > button.btn.btn-default')))
            createAppElem.click()

            self.log(6, "Found and selected 'Create' application button, using Create from Scratch option")

            #find / configure the new
            #self.switch_to_iframe('gsft_main', 10)

            epoch_time = int(time.time())
            app_table_name = "app-" + str(epoch_time)

            nameElem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="app_name"]')))
            nameElem.clear()
            nameElem.send_keys(app_table_name)

            self.log(7, ("Input new app name - " + app_table_name))

            #creates the new app, and confirms creation
            driver.find_element_by_css_selector("div > div:nth-of-type(3) > button.btn.btn-default").click()

            self.log(8, "Selected 'Create' new Application from Scratch");

            confirmElem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary')))
            confirmElem.click()

            self.log(9, "Confirmed ('OK') creation of new app from scratch")

            #logout
            #driver.find_element_by_id('user_info_dropdown').click()
            #driver.find_element_by_link_text('ul.dropdown-menu > li:nth-of-type(4) > a').click()

            #print ("[step 10] Logged out")

        except:
            print ('-'*60)
            traceback.print_exc(file=sys.stdout)
            print ('-'*60)

            raise Exception("ServiceNow Login failed...")

    def log(self, step, msg):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print ("[" + dt + "] [step " + str(step) + "] " + msg)

    def switch_to_iframe(self, iframe, timeout):
        wait = WebDriverWait(self.driver, timeout)

        frame = wait.until(EC.element_to_be_clickable((By.ID, iframe)))
        self.driver.switch_to.frame(frame)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

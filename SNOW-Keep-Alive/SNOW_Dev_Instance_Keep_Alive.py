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

class SNOW_Dev_Instance_Keep_Alive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://developer.servicenow.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_SNOW_Dev_Instance_Keep_Alive(self):
        driver = self.driver
        driver.get(self.base_url)

        wait = WebDriverWait(driver, 30)

        try:

            #wait for the login button
            signInButton = wait.until(EC.element_to_be_clickable((By.ID, 'SignInButton')))
            signInButton.click()

            self.log(0, "Home Page and Login Button is Accessible")

            #make sure the iframe and the form is visible
            userNameElem = wait.until(EC.element_to_be_clickable((By.ID,'username')))
            passwordElem = wait.until(EC.element_to_be_clickable((By.ID,'password')))

            self.log(1, "Found user_name and user_password elements in login form")

            # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | gsft_main | ]]
            #userNameElem = driver.find_element_by_css_selector("#user_name")
            userNameElem.clear()
            userNameElem.send_keys("steve.sturtevant@appdynamics.com")

            #passwordElem = driver.find_element_by_css_selector("user_password")
            passwordElem.clear()
            passwordElem.send_keys("W\"Q)w-D4:s")

            submitLoginButton = wait.until(EC.element_to_be_clickable((By.ID, 'submitButton')))
            submitLoginButton.click()

            manageInstanceButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.sn-red.sn-red-border')))

            self.log(2, "Found, and Selecting Manage Instance")
            manageInstanceButton.click()

            self.log(3, "Waiting for extend instance to be clickable")
            extendInstanceButton = wait.until(EC.element_to_be_clickable((By.ID, 'div.hint--top.hint-info.custom-hint.custom-hint-cell')))

            self.log(4, "Extend Instance Button is Clickable, Extending Instance")
            extendInstanceButton.click()

        except:
            print ('-'*60)
            traceback.print_exc(file=sys.stdout)
            print ('-'*60)

            raise Exception("ServiceNow Extend Instance Failed...")

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

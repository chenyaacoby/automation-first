import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from pages import general_methods
from pages.Form import FillForm
from selenium.webdriver.common.by import By

class FormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        print('SetUpClass')

    def setUp(self):
        print('setUp')

    def test_submit_form(self):
        print('\nStart test_submit_form')
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        mickey = FillForm(driver, 'Mickey', 'Mouse', 'mickey@disney.com', 'other', '5555555555', '20 May,2020',
                               'arts', 'music, reading', 'address 12/3', 'ncr', 'delhi')
        element = driver.find_element(By.ID, 'userForm')
        general_methods.scroll_to_element(self, element)
        time.sleep(1)

        mickey.fill_all_fields()
        mickey.submit_form()
        print(' \n ***  The form was submitted successfully !  *** \n')
        time.sleep(1)

        mickey.verification_test()
        print('End test_submit_form')


    def test_field_is_disabled(self):
        print('\nStart test_field_is_disabled')
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")

        element = driver.find_element(By.ID, 'userForm')
        general_methods.scroll_to_element(self, element)
        time.sleep(1)

        print (" - Initialize an object with an empty state")
        chen = FillForm(driver, 'Chen', 'Balassiano', 'chen@b.com', 'female', '1234567890', '20 March,1990',
                               '', 'music', 'address 12/3', '', 'delhi')
        chen.fill_all_fields()

        print(" - is the city disabled when the state is empty?")
        chen.is_city_disabled()
        time.sleep(1)

        print(" - State update:")
        chen.state = "ncr"
        chen.fill_state()
        chen.is_city_disabled()
        time.sleep(1)
        print('End test_field_is_disabled')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        print('tearDownClass')
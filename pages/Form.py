import time

from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class FillForm:
    def __init__(self, driver, first_name, last_name, email, gender, mobile, birthday, subjects, hobbies, address, state, city):
        self.driver = driver
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + ' ' + self.last_name
        self.email = email
        self.gender = ''
        self.set_gender(gender)
        self.mobile = mobile
        self.birthday = birthday
        self.subjects = subjects
        self.hobbies = hobbies
        self.address = address
        self.state = state
        self.city = city
        self.details = {}

    def student_details(self):
        self.details['Student Name'] = self.name
        self.details['Student Email'] = self.email
        self.details['Gender'] = self.gender
        self.details['Mobile'] = self.mobile
        self.details['Date of Birth'] = self.birthday
        self.details['Subjects'] = self.subjects
        self.details['Hobbies'] =  self.hobbies
        self.details['Address'] = self.address
        self.details['State and City'] = self.state + ' ' + self.city
        return self.details

    def set_gender(self, gender):
        gender = gender.capitalize()
        if gender not in ['Male', 'Female', 'Other']:
            self.gender = 'Other'
            print("Gender was not found, therefore set to \"Other\".")
        else:
            self.gender = gender

    def fill_all_fields(self):
        self.fill_name()
        self.fill_email()
        self.fill_gender()
        self.fill_mobile()
        self.fill_birthday()
        self.fill_subjects()
        self.fill_hobbies()
        self.fill_address()
        self.fill_state()
        if self.state:
            self.fill_city()

    def fill_name(self):
        first_name_field = self.driver.find_element(By.ID, 'firstName')
        first_name_field.send_keys(self.first_name)
        last_name_field = self.driver.find_element(By.ID, 'lastName')
        last_name_field.send_keys(self.last_name)
        print(f'Name {self.name} is filled in')

    def fill_email(self):
        email_field = self.driver.find_element(By.ID, 'userEmail')
        email_field.send_keys(self.email)
        print('E-mail is filled in')

    def fill_gender(self):
        gender_map = {'Male': '1', 'Female': '2', 'Other': '3'}
        gender_value = gender_map[self.gender]
        gender_xpath = f"//label[@for='gender-radio-{gender_value}']"
        gender_radio = self.driver.find_element(By.XPATH, gender_xpath)
        gender_radio.click()
        print(f'Gender "{self.gender}" is filled in')

    def fill_hobbies(self):
        hobbies_map = {'sports': '1', 'reading': '2', 'music': '3'}
        if len(self.hobbies) > 0:
            hobbies_list = self.hobbies.split(',')
            for hobby in hobbies_list:
                hobby = hobby.strip()
                for key, value in hobbies_map.items():
                    if hobby == key:
                        hobby_checkbox = self.driver.find_element(By.ID, f"hobbies-checkbox-{value}")
                        if hobby_checkbox.is_selected():
                            continue
                        else:
                            hobby_locator = self.driver.find_element(By.XPATH, f"//label[@for='hobbies-checkbox-{value}']")
                            hobby_locator.click()
                        print(f"{key} hobby checked")
        else:
            print("No hobby was selected")

    def fill_mobile(self):
        mobile_field = self.driver.find_element(By.ID, 'userNumber')
        mobile_field.send_keys(self.mobile)
        print('Mobile is filled in')

    def fill_birthday(self):
        birthday_field = self.driver.find_element(By.ID, 'dateOfBirthInput')
        birthday_field.send_keys(Keys.CONTROL,"a")
        birthday_field.send_keys(self.birthday)
        birthday_field.send_keys(Keys.ENTER)
        print('Birthday is filled in')

    def fill_subjects(self):
        subject_field = self.driver.find_element(By.ID, 'subjectsInput')
        subject_field.send_keys(self.subjects)
        subject_field.send_keys(Keys.TAB)

    def fill_address(self):
        address_field = self.driver.find_element(By.ID, 'currentAddress')
        address_field.send_keys(self.address)
        print("Address is filled in")

    def fill_state(self):
        state_field = self.driver.find_element(By.ID, 'react-select-3-input')
        state_field.send_keys(self.state)
        state_field.send_keys(Keys.TAB)
        time.sleep(1)
        print("State is filled in")

    def fill_city(self):
        city_select = self.driver.find_element(By.ID, 'react-select-4-input')
        city_select.send_keys(self.city)
        city_select.send_keys(Keys.TAB)
        print("City is filled in")

    def submit_form(self):
        form = self.driver.find_element(By.ID, 'userForm')
        form.submit()

    def verification_test(self):
        print ("Table Results:")
        expected = None
        student = self.student_details()   # a dictionary of student details
        rows = self.driver.find_elements(By.XPATH, '//tbody//tr')
        for row in rows:
            cells = row.find_elements(By.XPATH, './/td')  # two cells in every row
            if cells[0].text == "Picture":
                continue
            for key, value in student.items():
                if cells[0].text == key:
                    expected =  value
            result = (cells[1].text.strip().lower() == expected.strip().lower())   # returns TRUE/FALSE
            print (f" {cells[0].text}: Expected = {expected}; Actual = {cells[1].text}; result = {result}")

    def is_city_disabled(self):
        try:
            self.fill_city()
            print("City field is enabled")
        except ElementNotInteractableException:
            print("City field is disabled")
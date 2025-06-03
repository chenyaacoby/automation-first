from selenium.webdriver.common.by import By

def subjects_list(self, locator):
    subjects = self.driver.find_elements(By.XPATH, locator)
    subject_names = []
    for subject in subjects:
        card_name = subject.text
        subject_names.append(card_name)
    return subject_names

def scroll_to_element(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
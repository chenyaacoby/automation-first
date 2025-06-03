from selenium.webdriver.common.by import By
from pages import general_methods


class Menu:
    def __init__(self, driver):
        self.driver = driver

    def cards_list(self):
        card_names = general_methods.subjects_list(self,'//div[@class = "card mt-4 top-card"]')
        return card_names

    def print_cards(self):
        print("Card list in main page:")
        cards_name_list = self.cards_list()
        for card in cards_name_list:
            print (" ", card)


    def card_click(self, card):
        subj = self.driver.find_element(By.XPATH, f'//div[@class = "card mt-4 top-card"][.//*[text() = "{card}"]]')
        general_methods.scroll_to_element(self, subj)
        subj.click()
        print (f"The '{card}' card was clicked")

    def print_text(self):
        div = self.driver.find_element(By.XPATH, '//div[@class="col-12 mt-4 col-md-6"]')
        print(f"Displayed text: '{div.text}'")
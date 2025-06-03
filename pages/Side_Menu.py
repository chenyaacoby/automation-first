from selenium.webdriver.common.by import By
from pages import general_methods

class SideMenu:
    def __init__(self, driver):
        self.driver = driver

    def side_menu_list(self):
        side_menu = general_methods.subjects_list(self,'//div[@class = "header-text"]')
        return side_menu

    def verify_side_menu_list(self, cards):
        side_list = self.side_menu_list()
        all_present = True
        for card in cards:
            if card not in side_list:
                all_present = False
                print(f"'{card}' card is missing from the side menu !")
        if all_present:
            print("All cards are present in the side menu !")


    def click_side_list_item(self, chosen_side_list_item):
        side_item = self.driver.find_element(By.XPATH,
                                             f'//ul[@class = "menu-list"][.//text() = "{chosen_side_list_item}"]')
        side_item.click()
        print(f"Side item '{chosen_side_list_item}' was clicked")

    # verify headline from the item page, after choosing an item from side list:
    def verify_headline(self, item):
        headline = self.driver.find_element(By.XPATH, '//*[@class = "text-center"]')
        if headline.text == item:
            print(f"The headline '{headline.text}' - is correct")
        else:
            print(f"The headline  '{headline.text}' - is wrong !")
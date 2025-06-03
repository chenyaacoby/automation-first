import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from pages.Menu import Menu
from pages.Side_Menu import SideMenu

class Sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        print('SetUpClass')

    def setUp(self):
        print('setUp')

    def test_menu(self):
        print('Start test_menu')

        driver = self.driver
        driver.get("https://demoqa.com/")

        main_menu = Menu(driver)
        main_menu.print_cards()
        cards = main_menu.cards_list()  #getting cards list for verify_side_menu_list test

        # verify "Form" card navigates to next page
        chosen_subject = "Forms"
        main_menu.card_click(chosen_subject)
        main_menu.print_text()

        # verify side menu list is equal to cards in the main menu
        side_menu = SideMenu(driver)
        side_menu.verify_side_menu_list(cards)

        # verify "Practice Form" button navigates to "Practice Form" page
        chosen_side_list_item = "Practice Form"
        side_menu.click_side_list_item(chosen_side_list_item)
        side_menu.verify_headline(chosen_side_list_item)

        print('End test_menu')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        print('tearDownClass')
from Pages.base_page import BasePage
from Locators.locators import HomePageLocators


class CareersPage(BasePage):
    def drop_bar_menu(self):
        self.click_element(HomePageLocators.DROP_BAR)

    def company_cart_click(self):
        return self.click_element(HomePageLocators.COMPANY_MENU)

    def career_select_menu(self):
        self.click_element(HomePageLocators.CAREERS)





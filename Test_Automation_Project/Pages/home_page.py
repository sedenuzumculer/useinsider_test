from Locators.locators import HomePageLocators
from Pages.base_page import BasePage


class HomePage(BasePage):

    def close_add(self):
        try:
            self.click_element(HomePageLocators.ADD_CLOSE_BUTTON)
        except Exception as e:
            print(f"ADD block tıklanamadı: {e}")
            pass

    def accept_cookies(self):
        try:
            self.click_element(HomePageLocators.COOKIE_BANNER_ACCEPT_BUTTON)
        except Exception as e:
            print(f"Cookie kabul button tıklanamadı: {e}")
            pass

    def logo_item_click(self):

        return self.click_element(HomePageLocators.INSIDER_LOGO)

    def verify_on_correct_page(self, expected_url):
        current_url = self.get_current_url()
        assert expected_url in current_url, f"Expected product ID '{expected_url}' not in URL '{current_url}'"

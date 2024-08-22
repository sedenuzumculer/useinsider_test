import time

from Pages.home_page import HomePage
from Pages.careers_page import CareersPage
from Tests.base_tests import BaseTest


class InsiderTests(BaseTest):
    def test_insider_tests(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(), "Insider Anasayfa Açılamadı")
        home_page.verify_on_correct_page("https://useinsider.com/")
        home_page.accept_cookies()
        time.sleep(1)
        careers_page = CareersPage(self.driver)

        careers_page.company_cart_click()

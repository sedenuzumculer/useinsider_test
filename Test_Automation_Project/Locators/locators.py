from selenium.webdriver.common.by import By


class HomePageLocators:
    """A class for main page locators. All main page locators should come here"""
    ADD_CLOSE_BUTTON = (By.CLASS_NAME, 'ins-element-close-button ins-selectable-element ins-element-wrap')
    COOKIE_BANNER_ACCEPT_BUTTON = (By.ID, 'wt-cli-accept-all-btn')
    INSIDER_LOGO = (By.CLASS_NAME, 'navbar-brand d-flex flex-row align-items-center')
    DROP_BAR = (By.CLASS_NAME, 'navbar-toggler collapsed')
    COMPANY_MENU = (By.LINK_TEXT, 'Company')
    CAREERS = (By.CSS_SELECTOR, "a.dropdown-sub[href='https://useinsider.com/careers/']")
    SEE_ALL_QA_JOBS = (By.CLASS_NAME, "btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50")
    FILTER = (By.CSS_SELECTOR, 'Filter')
    FILTER_OPEN = (By.CSS_SELECTOR, "span.select2-selection__arrow[role='presentation']")
    LOCATION_SELECT = (By.ID, "select2-filter-by-location-result-ip5e-Istanbul, Turkey")
    SELECTION_QA = (By.XPATH, "//a[@href='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc']")

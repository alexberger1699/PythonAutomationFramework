from autoTests.src.helpers.config_helpers import get_base_url
class Home_page:

    def __init__(self, driver):
        self.driver = driver


    def go_to_home_page(self):
        home_page_url = get_base_url()
        self.driver.get(home_page_url)

#
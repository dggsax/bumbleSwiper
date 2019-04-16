import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Swiper:
    def __init__(self):
        #self.driver = webdriver.Firefox('./geckodriver')
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5) # Give 5 seconds for things to run before error-ing out
        self.login()

    def login(self):
        # Navigate to the login page
        self.driver.get("https://bumble.com/login/")
        
        # Wait for page to load because MIT internet is trash
        time.sleep(5)

        # Select the option to log in with facebook
        facebook_xpath = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div/div/div[1]/div'
        facebook_button = self.driver.find_element_by_xpath(facebook_xpath)
        facebook_button.click()
        print('Follow the instructions and log in to facebook')

    def start_swiping(self):
        input('When you\'re logged in and ready to swipe, press any key')
        
        sad_boi_text = '//*[@id="main"]/div/div[1]/main/div[2]/article/div/span/section/div/h1/span'
        love_is_in_the_air = True
        
        # Yeah, I know, no while loops, but oh well
        while love_is_in_the_air:
            time.sleep(1)
            try:
                # The `sad_boi_text` xpath represents what you'd see when there
                # aren't any more people to swipe on
                self.driver.find_element_by_xpath(sad_boi_text)
                love_is_in_the_air = False
            except NoSuchElementException as e:
                ActionChains(self.driver).send_keys(Keys.ARROW_RIGHT).perform()

        print('Done, no more people to swipe on. Come back later.')


if __name__ == "__main__":
    # run the thing
    instance = Swiper()
    instance.start_swiping()

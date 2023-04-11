from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    link_electronics_xpath = "(//a[@id='electronics'])[1]"
    link_cameras_xpath = "//a[normalize-space()='Cameras']"
    button_addtocart_xpath = "(//button[@type='button'])[2]"
    link_addtocarticon_cssselector = "#cartIcon"


    def __init__(self, driver):
        self.driver = driver

    def Click_Electronics(self):
        self.driver.find_element(By.XPATH, self.link_electronics_xpath).click()

    def Click_Cameras(self):
        self.driver.find_element(By.XPATH, self.link_cameras_xpath).click()

    def Click_AddToCart(self):
        self.driver.find_element(By.XPATH, self.button_addtocart_xpath).click()

    def VerifyPresenceofLink(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartIcon")))

    def Click_AddCartIcon(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_addtocarticon_cssselector).click()

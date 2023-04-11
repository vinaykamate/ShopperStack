from selenium.webdriver.common.by import By


class PaymentPage:
    radiobtn_netbanking_xpath = "//input[@value='Net Banking']"
    radiobtn_cod_xpath = "//input[@value='COD']"
    button_addcard_xpath = "//button[contains(text(),'Add Card')]"
    textbox_cardholdername_xpath = "//input[@id=':r1m:']"
    textbox_cardnumber_xpath = "//input[@id=':r1u:']"
    textbox_pin_xpath = "//input[@id=':r1v:']"
    textbox_expirymonth_xpath = "//input[@id=':r20:']"
    textbox_expiryyear_xpath = "//input[@id=':r21:']"
    textbox_cvv_xpath = "//input[@id=':r21:']"
    radiobtn_debit_xpath = "//input[@value='DEBIT']"
    button_add_xpath = "//button[normalize-space()='Add']"
    button_proceed_xpath = "//button[contains(text(),'Proceed')]"

    def __init__(self, driver):
        self.driver = driver

    def Select_Payment(self, Payment):
        if Payment == "NetBanking":
            self.driver.find_element(By.XPATH, self.radiobtn_netbanking_xpath).click()

        elif Payment == "AddCard":
            self.driver.find_element(By.XPATH, self.button_addcard_xpath).click()
            self.driver.find_element(By.XPATH, self.textbox_cardholdername_xpath).send_keys("Vinay")
            self.driver.find_element(By.XPATH, self.textbox_cardnumber_xpath).send_keys("3014401191608021")
            self.driver.find_element(By.XPATH, self.textbox_pin_xpath).send_keys("6526")
            self.driver.find_element(By.XPATH, self.textbox_expirymonth_xpath).send_keys("4")
            self.driver.find_element(By.XPATH, self.textbox_expiryyear_xpath).send_keys("28")
            self.driver.find_element(By.XPATH, self.textbox_cvv_xpath).send_keys("832")
            self.driver.find_element(By.XPATH, self.radiobtn_debit_xpath).click()
            self.driver.find_element(By.XPATH, self.button_add_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.radiobtn_cod_xpath).click()

    def Click_Proceed(self):
        self.driver.find_element(By.XPATH, self.button_proceed_xpath).click()

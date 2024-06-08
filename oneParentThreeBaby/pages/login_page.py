from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
# login_email = driver.find_element(By.NAME, 'email').send_keys('bhojrajjichadhokar@gmail.com')
    username_field = (By.NAME, 'email')

# login_pass = driver.find_element(By.ID, 'login-pass').send_keys("bhojraj@123")
    password_field = (By.ID, 'login-pass')

# submit = driver.find_element(By.CSS_SELECTOR, 'button#s-submit-login').click()
    login_button = (By.CSS_SELECTOR, 'button#s-submit-login')

    def enter_username(self,username):
        self.wait_for_element(self.username_field).send_keys(username)

    def enter_password(self,password):
        self.wait_for_element(self.password_field).send_keys(password)

    def click_login(self):
        self.wait_for_element(self.login_button).click()

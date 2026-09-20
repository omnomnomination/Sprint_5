from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from locators.login_locators import LoginPageLocators
from data import TestData

class TestLogin:

    # ========================================================
    # 1. Вход по кнопке «Войти в аккаунт» на главной
    # ========================================================
    def test_login_via_main_page_button(self, driver, registered_user_email):
        # Получаем email автоматически зарегистрированного пользователя из фикстуры
        user_email = registered_user_email
        
        driver.get(TestData.BASE_URL) # Открываем главную
        driver.find_element(*LoginPageLocators.MAIN_LOGIN_BUTTON).click() # Кликаем «Войти в аккаунт»
        
        # Заполняем форму
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем, что вход успешен (появилась кнопка заказа)
        order_btn = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert order_btn.is_displayed()

    # ========================================================
    # 2. Вход через кнопку «Личный кабинет»
    # ========================================================
    def test_login_via_account_button(self, driver, registered_user_email):
        user_email = registered_user_email
        
        driver.get(TestData.BASE_URL) # Открываем главную
        driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click() # Кликаем «Личный кабинет»
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_btn = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert order_btn.is_displayed()

    # ========================================================
    # 3. Вход через кнопку в форме регистрации
    # ========================================================
    def test_login_via_registration_form_link(self, driver, registered_user_email):
        user_email = registered_user_email
        
        driver.get(f"{TestData.BASE_URL}register") # Открываем регистрацию
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click() # Кликаем на ссылку «Войти» внизу
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_btn = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert order_btn.is_displayed()

    # ========================================================
    # 4. Вход через кнопку в форме восстановления пароля
    # ========================================================
    def test_login_via_forgot_password_form_link(self, driver, registered_user_email):
        user_email = registered_user_email
        
        driver.get(f"{TestData.BASE_URL}forgot-password") # Открываем восстановление пароля
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LOGIN_LINK).click() # Кликаем «Войти»
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_btn = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert order_btn.is_displayed()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from locators.login_locators import LoginPageLocators
from data import TestData

# Регистрируем пользователя 
def register_new_user(driver, email):
    driver.get(f"{TestData.BASE_URL}register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Владимир")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))

# ========================================================
# 1. Вход по кнопке «Войти в аккаунт» на главной
# ========================================================
def test_login_via_main_page_button(driver):
    user_email = TestData.generate_unique_email()
    register_new_user(driver, user_email)
    
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
def test_login_via_account_button(driver):
    user_email = TestData.generate_unique_email()
    register_new_user(driver, user_email)
    
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
def test_login_via_registration_form_link(driver):
    user_email = TestData.generate_unique_email()
    register_new_user(driver, user_email)
    
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
def test_login_via_forgot_password_form_link(driver):
    user_email = TestData.generate_unique_email()
    register_new_user(driver, user_email)
    
    driver.get(f"{TestData.BASE_URL}forgot-password") # Открываем восстановление пароля
    driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LOGIN_LINK).click() # Кликаем «Войти»
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    order_btn = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
    assert order_btn.is_displayed()

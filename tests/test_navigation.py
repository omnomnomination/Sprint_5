from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from locators.login_locators import LoginPageLocators
from data import TestData

# ====================================================================
# Регистрируем пользователя и входим
# ====================================================================
def register_and_login_user(driver):
    user_email = TestData.generate_unique_email()
    
    # Регистрация
    driver.get(f"{TestData.BASE_URL}register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Владимир")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))
    
    # Авторизация
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))


# ====================================================================
# №1 Переход в личный кабинет 
# ====================================================================
def test_navigate_to_profile_page(driver):
    register_and_login_user(driver)
    
    driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click() # Нажимаем "личный кабинет" в шапке сайта

    # Проверяем, что в адресе страницы появилось упоминание профиля
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account/profile"))
    assert "account/profile" in driver.current_url


# ====================================================================
# №2 Переход из личного кабинета в конструктор
# ====================================================================
def test_navigate_from_profile_to_constructor_via_button(driver):
    register_and_login_user(driver)
    driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))
    
    driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click() # Кликаем на кнопку «Конструктор» 
    assert driver.current_url == TestData.BASE_URL # Проверяем, что вернулись на главную страницу 


def test_navigate_from_profile_to_constructor_via_logo(driver):
    register_and_login_user(driver)
    driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))
    driver.find_element(*LoginPageLocators.LOGO_BUTTON).click() # Нажимаем на интерактивный логотип
    assert driver.current_url == TestData.BASE_URL # Проверяем, что вернулись на главную страницу 


# ====================================================================
# №3 Выход из аккаунта
# ====================================================================
def test_logout_from_profile_page(driver):
    register_and_login_user(driver)
    driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))
    
    # Дожидаемся появления кнопки на экране и кликаем по ней
    logout_btn = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
    )
    logout_btn.click()
    
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))
    assert "login" in driver.current_url


# ====================================================================
# №4 Раздел «Конструктор» (Переходы к разделам ингредиентов)
# ====================================================================

# Переход к разделу «Соусы»
def test_constructor_navigate_to_sauces(driver):
    driver.get(TestData.BASE_URL) # Открываем главную страницу
    
    # Кликаем на раздел «Соусы»
    driver.find_element(*LoginPageLocators.SECTION_SAUCES).click()
    
    # Проверяем заголовок «Соусы»
    assert driver.find_element(*LoginPageLocators.HEADING_SAUCES).is_displayed()


# Переход к разделу «Начинки»
def test_constructor_navigate_to_fillings(driver):
    driver.get(TestData.BASE_URL)
    
    # Кликаем на раздел «Начинки»
    driver.find_element(*LoginPageLocators.SECTION_FILLINGS).click()
    
    # Проверяем заголовок «Начинки»
    assert driver.find_element(*LoginPageLocators.HEADING_FILLINGS).is_displayed()


# Переход к разделу «Булки»
def test_constructor_navigate_to_buns(driver):
    driver.get(TestData.BASE_URL)
    
    # Переключаемся на Соусы, чтобы убрать фокус с булок
    driver.find_element(*LoginPageLocators.SECTION_SAUCES).click()
    
    # Нажимаем на "Булки"
    driver.find_element(*LoginPageLocators.SECTION_BUNS).click()
    
    # Проверяем заголовок «Булки»
    assert driver.find_element(*LoginPageLocators.HEADING_BUNS).is_displayed()


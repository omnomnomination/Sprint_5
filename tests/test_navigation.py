from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from locators.login_locators import LoginPageLocators
from data import TestData

class TestNavigation:
        
    # ====================================================================
    # №1 Переход в личный кабинет 
    # ====================================================================
    def test_navigate_to_profile_page(self, driver, logged_in_user):
        
        driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click() # Нажимаем "личный кабинет" в шапке сайта

        # Проверяем, что в адресе страницы появилось упоминание профиля
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("account/profile"))
        assert "account/profile" in driver.current_url


    # ====================================================================
    # №2 Переход из личного кабинета в конструктор
    # ====================================================================
    def test_navigate_from_profile_to_constructor_via_button(self, driver, logged_in_user):
        
        driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))
        
        driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click() # Кликаем на кнопку «Конструктор» 
        assert driver.current_url == TestData.BASE_URL # Проверяем, что вернулись на главную страницу 


    def test_navigate_from_profile_to_constructor_via_logo(self, driver, logged_in_user):
        
        driver.find_element(*LoginPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))
        driver.find_element(*LoginPageLocators.LOGO_BUTTON).click() # Нажимаем на интерактивный логотип
        assert driver.current_url == TestData.BASE_URL # Проверяем, что вернулись на главную страницу 


    # ====================================================================
    # №3 Выход из аккаунта
    # ====================================================================
    def test_logout_from_profile_page(self, driver, logged_in_user):
        
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
    def test_constructor_navigate_to_sauces(self, driver):
        driver.get(TestData.BASE_URL) # Открываем главную страницу
        
        # Кликаем на раздел «Соусы»
        driver.find_element(*LoginPageLocators.SECTION_SAUCES).click()
        
        # Проверяем заголовок «Соусы»
        button_class = driver.find_element(*LoginPageLocators.SECTION_SAUCES).get_attribute("class")
        assert "tab_tab_type_current" in button_class


    # Переход к разделу «Начинки»
    def test_constructor_navigate_to_fillings(self, driver):
        driver.get(TestData.BASE_URL)
        
        # Кликаем на раздел «Начинки»
        driver.find_element(*LoginPageLocators.SECTION_FILLINGS).click()
        
        # Проверяем заголовок «Начинки»
        button_class = driver.find_element(*LoginPageLocators.SECTION_FILLINGS).get_attribute("class")
        assert "tab_tab_type_current" in button_class


    # Переход к разделу «Булки»
    def test_constructor_navigate_to_buns(self, driver):
        driver.get(TestData.BASE_URL)
        
        # Переключаемся на Соусы, чтобы убрать фокус с булок
        driver.find_element(*LoginPageLocators.SECTION_SAUCES).click()
        
        # Нажимаем на "Булки"
        driver.find_element(*LoginPageLocators.SECTION_BUNS).click()
        
        # Проверяем заголовок «Булки»
        button_class = driver.find_element(*LoginPageLocators.SECTION_BUNS).get_attribute("class")
        assert "tab_tab_type_current" in button_class



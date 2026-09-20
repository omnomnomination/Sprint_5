from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from data import TestData

# ==================================================
# №1 Успешная регистрация
# ==================================================

def test_successful_registration(driver):
    # Открываем страницу регистрации
    driver.get(f"{TestData.BASE_URL}register")

    # Заводим новую валидную почту
    unique_email = TestData.generate_unique_email()

    # Заполняем форму подходящими данными
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Владимир")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(unique_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    
    # Нажимаем "Зарегистрироваться"
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
    # Ждем, пока URL изменится на страницу авторизации
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))
    
    # Проверяем, что нас перекинуло на страницу авторизации
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

# ==================================================
# №2 Ошибка регистрации при коротком пароле
# ==================================================


def test_registration_with_short_password_shows_error(driver):
    # Открываем страницу регистрации 
    driver.get(f"{TestData.BASE_URL}register")
    
    # Генерируем новый уникальный email
    unique_email = TestData.generate_unique_email()
    
    # Заполняем форму с неподходящим паролем
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Владимир")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(unique_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.INVALID_PASSWORD)
    
    # Нажимаем «Зарегистрироваться»
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
    # Ждем появления элемента с текстом ошибки под полем пароля
    error_element = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
    )
    
    # Проверяем, что элемент с ошибкой отображается на экране
    assert error_element.is_displayed()
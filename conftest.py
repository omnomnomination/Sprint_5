import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.registration_locators import RegisterPageLocators
from locators.login_locators import LoginPageLocators  # Проверьте имя папки (login или login_page_locators)
from data import TestData

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver
    driver.quit()

# Фикстура для тестов входа (регистрирует и отдает email)
@pytest.fixture
def registered_user_email(driver):
    user_email = TestData.generate_unique_email()
    
    driver.get(f"{TestData.BASE_URL}register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Владимир")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))
    
    yield user_email

# Фикстура для навигации (регистрирует и логинит на сайте)
@pytest.fixture
def logged_in_user(driver):
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
    
    yield user_email
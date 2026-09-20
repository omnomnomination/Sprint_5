from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле ввода "email"
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") #Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error') and text()='Некорректный пароль']") # Текст ошибки "Некорректный пароль"
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']") # Ссылка "Войти" под полем регистрации

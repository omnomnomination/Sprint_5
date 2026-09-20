from selenium.webdriver.common.by import By

class LoginPageLocators:
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка войти в аккаунт на стартовой странице
    ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']") # Кнопка личный кабинет на стартовой странице
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']") # Кнопка войти в форме восстановления пароля
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле ввода почты на странице авторизации
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # Поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка войти на странице авторизации 
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка оформить заказ после успешного входа
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']") # Кнопка "Конструктор" на стартовой странице
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a") # Интерактивный логотип в шапке сайта
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка "выход" в личном кбаинете
    SECTION_BUNS = (By.XPATH, ".//div[span[text()='Булки']]") # Переключатель раздела "булки"
    SECTION_SAUCES = (By.XPATH, ".//div[span[text()='Соусы']]") # Переключатель раздела "соусы"
    SECTION_FILLINGS = (By.XPATH, ".//div[span[text()='Начинки']]") # Переключатель раздела "начинки"
    HEADING_BUNS = (By.XPATH, ".//h2[text()='Булки']") # Заголовок блока "Булки"
    HEADING_SAUCES = (By.XPATH, ".//h2[text()='Соусы']") # Заголовок блока "Соусы"
    HEADING_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']") # Заголовок блока "Начинки"

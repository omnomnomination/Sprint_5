import random

class TestData:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    VALID_PASSWORD = "password123" 
    INVALID_PASSWORD = "123"         

    @staticmethod
    def generate_unique_email():
        cohort_number = "52"
        random_digits = random.randint(100, 999)
        return f"name_surname_{cohort_number}_{random_digits}@yandex.ru"

#
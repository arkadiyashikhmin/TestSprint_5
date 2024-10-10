from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Укажите путь к скачанному chromedriver.exe
chromedriver_path = "chromedriver.exe"  # Замените на свой путь

# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Открыть браузер на весь экран

# Инициализация драйвера с явным указанием пути к chromedriver.exe
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открываем сайт Stellar Burgers
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ждем загрузки страницы
    time.sleep(3)

    # Нажимаем на вкладку "Начинки"
    nachinki_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']")
    nachinki_tab.click()
    time.sleep(2)

    # Нажимаем на вкладку "Соусы"
    sousi_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']")
    sousi_tab.click()
    time.sleep(2)

    # Нажимаем на вкладку "Булки"
    bulki_tab = driver.find_element(By.XPATH, "//span[text()='Булки']")
    bulki_tab.click()
    time.sleep(2)

    # Переходим в Личный кабинет
    account_button = driver.find_element(By.XPATH, "//a[@href='/account']")
    account_button.click()
    time.sleep(2)

    # Нажимаем на ссылку "Зарегистрироваться"
    register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
    register_link.click()
    time.sleep(2)

    # Вводим имя
    name_input = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")
    name_input.send_keys("Test123")
    time.sleep(1)

    # Вводим email
    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    email_input.send_keys("test_testov_2024@gmail.com")
    time.sleep(1)

    # Вводим пароль
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("12345678")  # Пример некорректного пароля для проверки
    time.sleep(1)

    # Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()
    time.sleep(3)

    # Проверяем, существует ли сообщение об ошибке "Некорректный пароль"
    try:
        password_error_message = driver.find_element(By.XPATH,
                                                     "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")
        print("Некорректный пароль. Программа завершена.")
        driver.quit()  # Закрываем браузер, если пароль некорректен
        exit()  # Завершаем выполнение программы

    except NoSuchElementException:
        # Сообщение об ошибке не найдено, продолжаем выполнение скрипта
        pass

    # Проверяем, существует ли сообщение об ошибке "Такой пользователь уже существует"
    try:
        error_message = driver.find_element(By.XPATH,
                                            "//p[@class='input__error text_type_main-default' and text()='Такой пользователь уже существует']")
        print("Пользователь уже существует. Переходим на страницу входа.")

        # Нажимаем на ссылку "Войти"
        login_link = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")
        login_link.click()
        time.sleep(3)

    except NoSuchElementException:
        # Сообщение об ошибке не найдено, продолжаем процесс регистрации
        pass

    # Вводим email на странице входа
    login_email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    login_email_input.send_keys("test_testov_2024@gmail.com")
    time.sleep(1)

    # Вводим пароль на странице входа
    login_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    login_password_input.send_keys("12345678")
    time.sleep(1)

    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

    # Ждем загрузки личного кабинета
    time.sleep(5)

    # Переход в Личный кабинет после входа
    account_button_after_login = driver.find_element(By.XPATH, "//a[@href='/account']")
    account_button_after_login.click()
    time.sleep(3)

    # Нажимаем на ссылку "Конструктор"
    constructor_button = driver.find_element(By.XPATH, "//p[text()='Конструктор']")
    constructor_button.click()
    time.sleep(3)

    account_button_after_login = driver.find_element(By.XPATH, "//a[@href='/account']")
    account_button_after_login.click()
    time.sleep(3)

    # Нажимаем на кнопку "Выход"
    logout_button = driver.find_element(By.XPATH,
                                        "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")
    logout_button.click()
    time.sleep(3)

    # Нажимаем на ссылку "Восстановить пароль"
    forgot_password_link = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")
    forgot_password_link.click()
    time.sleep(3)
    # Нажимаем на ссылку "Войти"
    login_link_again = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")
    login_link_again.click()
    time.sleep(3)

    # Вводим email на странице входа
    login_email_input_again = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    login_email_input_again.send_keys("test_testov_2024@gmail.com")
    time.sleep(1)

    # Вводим пароль на странице входа
    login_password_input_again = driver.find_element(By.XPATH, "//input[@type='password']")
    login_password_input_again.send_keys("12345678")
    time.sleep(1)

    # Нажимаем кнопку "Войти"
    login_button_again = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button_again.click()

    time.sleep(20)

finally:
    # Закрываем браузер
    driver.quit()

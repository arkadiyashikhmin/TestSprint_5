В данном скрипте используются локаторы для элементов
на сайте Stellar Burgers. Рассмотрим, какие именно локаторы
 задействованы и какие тесты они проходят:

1. Локаторы элементов:
Вкладки на странице конструктора бургера:

Локатор вкладки "Начинки":

nachinki_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']")
Локатор вкладки "Соусы":

sousi_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']")
Локатор вкладки "Булки":

bulki_tab = driver.find_element(By.XPATH, "//span[text()='Булки']")
Личный кабинет:

Локатор кнопки перехода в личный кабинет:

account_button = driver.find_element(By.XPATH, "//a[@href='/account']")
Регистрация:

Локатор ссылки "Зарегистрироваться":


register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
Локатор поля для ввода имени:

name_input = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")
Локатор поля для ввода email:

email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
Локатор поля для ввода пароля:

password_input = driver.find_element(By.XPATH, "//input[@type='password']")
Локатор кнопки "Зарегистрироваться":

register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
Ошибки при регистрации:

Локатор сообщения об ошибке "Некорректный пароль":


password_error_message = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")
Локатор сообщения об ошибке "Такой пользователь уже существует":

error_message = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Такой пользователь уже существует']")
Вход в аккаунт:

Локатор поля для ввода email:

login_email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
Локатор поля для ввода пароля:

login_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
Локатор кнопки "Войти":

login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
Выход из аккаунта:

Локатор кнопки "Выход":

logout_button = driver.find_element(By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")
Сброс пароля:

Локатор ссылки "Восстановить пароль":


forgot_password_link = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")
2. Какие тесты проходят:
Проверка навигации по вкладкам:

Тестируется, что можно переключаться между вкладками "Начинки",
"Соусы" и "Булки" в конструкторе бургера.
Тест перехода в личный кабинет:

Осуществляется проверка возможности перехода в личный кабинет.
Тест регистрации пользователя:

Проверяется, что можно ввести имя, email и пароль.
Также проверяется работа кнопки "Зарегистрироваться".
Проверка ошибок при регистрации:

Тестируется, что при некорректном пароле (например, слишком коротком)
 выводится сообщение "Некорректный пароль".
Проверяется вывод ошибки, если пользователь с таким email уже существует.
Тест входа в аккаунт:

После регистрации или попытки зарегистрироваться с существующим пользователем проверяется,
 что можно успешно войти в аккаунт, используя email и пароль.
Тест выхода из аккаунта:
После входа в личный кабинет проверяется, что можно выйти из аккаунта.
Тест восстановления пароля:

Проверяется переход на страницу восстановления пароля и возвращение на страницу входа.
Таким образом, этот скрипт проверяет базовые функции сайта Stellar Burgers, включая регистрацию,
 вход, навигацию по вкладкам и личному кабинету.

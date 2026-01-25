import pytest
import time
from playwright.sync_api import sync_playwright, Page

BASE_URL = "https://qauto2.forstudy.space/"

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)


class RegistrationPage(BasePage):
    def open(self):
        self.page.wait_for_selector("text=Sign Up", timeout=15000)
        self.page.click("text=Sign Up")
        self.page.wait_for_selector("input[name='name']", timeout=15000)

    def register(self, name: str, last_name: str, email: str, password: str):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[name='lastName']", last_name)
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.fill("input[name='repeatPassword']", password)

        submit_button = self.page.locator("button:has-text('Register')")
        # Перевіряємо, чи кнопка enabled
        if submit_button.is_enabled():
            submit_button.click()

    def is_registered(self) -> bool:
        self.page.wait_for_timeout(2000)
        return "/panel" in self.page.url

    def logout(self):
        menu_button = self.page.locator("button.user-nav_toggle")
        menu_button.wait_for(state="visible", timeout=10000)
        menu_button.click()
        logout_button = self.page.locator("button.user-nav_link", has_text="Logout")
        logout_button.wait_for(state="visible", timeout=10000)
        logout_button.click()
        self.page.locator("text=Sign In").wait_for(state="visible", timeout=10000)


class LoginPage(BasePage):
    def open(self):
        self.page.locator("text=Sign In").wait_for(state="visible", timeout=15000)
        self.page.click("text=Sign In")
        self.page.locator("input[name='email']").wait_for(state="visible", timeout=15000)
        self.page.locator("input[name='password']").wait_for(state="visible", timeout=15000)

    def login(self, email: str, password: str):
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        submit_button = self.page.locator("button:has-text('Login')")
        submit_button.wait_for(state="visible", timeout=10000)
        submit_button.click()
        self.page.wait_for_url("**/panel/**", timeout=10000)

    def is_logged_in(self) -> bool:
        return "/panel" in self.page.url

    def login_expect_failure(self, email: str, password: str):
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        submit_button = self.page.locator("button:has-text('Login')")
        submit_button.wait_for(state="visible", timeout=10000)
        submit_button.click()
        self.page.wait_for_timeout(1000)  # час для помилки

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            http_credentials={"username": "guest", "password": "welcome2qauto"}
        )
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"testuser{timestamp}@example.com"

def test_registration_login_logout(page: Page):
    unique_email = generate_unique_email()

    reg_page = RegistrationPage(page)
    reg_page.goto(BASE_URL)
    reg_page.open()
    reg_page.register("Test", "User", unique_email, "Password123")
    assert reg_page.is_registered(), "Реєстрація не успішна"

    reg_page.logout()
    page.wait_for_timeout(1000)

    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.open()
    login_page.login(unique_email, "Password123")
    assert login_page.is_logged_in(), "Логін не успішний"

    reg_page.logout()
    page.wait_for_timeout(1000)


def test_registration_with_invalid_name_lastname(page: Page):
    reg_page = RegistrationPage(page)
    reg_page.goto(BASE_URL)
    reg_page.open()

    # Вводимо некоректні дані
    reg_page.page.fill("input[name='name']", "")
    reg_page.page.fill("input[name='lastName']", "")
    reg_page.page.fill("input[name='email']", "invalidtest@example.com")
    reg_page.page.fill("input[name='password']", "Password123")
    reg_page.page.fill("input[name='repeatPassword']", "Password123")

    # Даємо час помилкам з'явитися
    page.wait_for_timeout(500)

    # Перевірка тексту помилок через XPath
    name_error = page.locator(
        "xpath=/html/body/ngb-modal-window/div/div/app-signup-modal/div[2]/app-signup-form/form/div[1]/div/p"
    )
    last_name_error = page.locator(
        "xpath=/html/body/ngb-modal-window/div/div/app-signup-modal/div[2]/app-signup-form/form/div[2]/div/p"
    )

    name_error.wait_for(state="visible", timeout=5000)
    last_name_error.wait_for(state="visible", timeout=5000)

    assert "Name required" in name_error.inner_text()
    assert "Last name required" in last_name_error.inner_text()


def test_registration_with_existing_email(page: Page):
    unique_email = generate_unique_email()

    reg_page = RegistrationPage(page)
    reg_page.goto(BASE_URL)
    reg_page.open()
    reg_page.register("Test", "User", unique_email, "Password123")
    assert reg_page.is_registered()

    reg_page.logout()
    page.wait_for_timeout(1000)

    # Знову відкриваємо форму реєстрації
    reg_page.goto(BASE_URL)
    reg_page.open()

    # Заповнюємо форму з тим же email
    reg_page.page.fill("input[name='name']", "Test")
    reg_page.page.fill("input[name='lastName']", "User")
    reg_page.page.fill("input[name='email']", unique_email)
    reg_page.page.fill("input[name='password']", "Password123")
    reg_page.page.fill("input[name='repeatPassword']", "Password123")

    # Клікаємо Register, щоб тригернути серверну помилку
    submit_button = reg_page.page.locator("button:has-text('Register')")
    submit_button.click()

    # Чекаємо поки з'явиться повідомлення про помилку
    error_message = reg_page.page.locator("p.alert.alert-danger")
    error_message.wait_for(state="visible", timeout=5000)

    # Збираємо текст усіх помилок і перевіряємо, що є повідомлення про існуючого користувача
    errors_text = [e.inner_text() for e in reg_page.page.locator("p.alert.alert-danger").all()]
    assert any("exists" in msg.lower() for msg in errors_text), f"Expected 'exists' in error, got {errors_text}"



def test_login_with_wrong_password(page: Page):
    unique_email = generate_unique_email()

    reg_page = RegistrationPage(page)
    reg_page.goto(BASE_URL)
    reg_page.open()
    reg_page.register("Test", "User", unique_email, "Password123")
    assert reg_page.is_registered()

    reg_page.logout()
    page.wait_for_timeout(1000)

    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.open()
    login_page.login_expect_failure(unique_email, "WrongPassword!")

    error_messages = [e.inner_text() for e in login_page.page.locator("p.alert.alert-danger").all()]
    assert any("wrong email or password" in msg.lower() or "invalid" in msg.lower() for msg in error_messages)


def test_login_with_nonexistent_email(page: Page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.open()
    login_page.login_expect_failure("nonexistent@example.com", "Password123")

    error_messages = [e.inner_text() for e in login_page.page.locator("p.alert.alert-danger").all()]
    assert any("wrong email or password" in msg.lower() or "invalid" in msg.lower() for msg in error_messages)

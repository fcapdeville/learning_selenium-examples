from selenium.webdriver.common.by import By


class Locators():
    # Login page objects
    username_textbox_id = (By.ID, "txtUsername")
    password_textbox_id = (By.ID, "txtPassword")
    login_button_id = (By.ID, "btnLogin")

    # Home page objects
    welcome_link_id = (By.ID, "welcome")
    logout_link_linkText = (By.LINK_TEXT, "Logout")

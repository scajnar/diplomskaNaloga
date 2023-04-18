from avditorij.base_elements.page import Page


class LoginPage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.login_container_xpath = './/div[contains(@class, "login-container")]'
        self.avditorij_title_xpath = './/div[contains(@class, "login-heading")]'
        self.language_dropdown_xpath = './/a[contains(@class, "dropdown-toggle")]'
        self.username_input_xpath = './/input[@id="username"]'
        self.password_input_xpath = './/input[@id="password"]'
        self.remember_username_toggle_xpath = './/input[@id="rememberusername"]'
        self.remember_username_text_xpath = './/label[@for="rememberusername"]'
        self.login_button_xpath = './/button[@id="loginbtn"]'
        self.forgot_username_xpath = './/div[@class="login-form-forgotpassword form-group"]'
        self.some_courses_text_xpath = './/h2[@class="login-heading"]'
        self.login_as_guest_button_xpath = './/button[@class="btn btn-secondary"]'
        self.cookies_must_enabled_text_xpath = './/div[@class="login-cookiemessage"]'
        self.cookies_must_enabled_info_icon_xpath = './/div[@class="login-cookiemessage"]/a'
        self.corner_question_mark_button = './/button[@data-action="footer-popover"]'

        
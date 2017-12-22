from django.core.exceptions import ValidationError


class LoginValidation:
    def __init__(self, username):
        self.username = username
        # print(username)

    def check_username_length(self):
        # pass
        if len(self.username) not in range(5, 26):
            raise ValidationError(
                "Login length should be 5 - 25 symbols")

    def check_username_letters(self):
        # pass
        letters = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
        for i in self.username:
            if i.lower() not in letters:
                raise ValidationError("Login should contain only english letters, numbers & «_»")

    def check_username(self):
        self.check_username_letters()
        self.check_username_length()


class PasswordValidation:

    def __init__(self, password):
        self.password = password
        # print(password)

    def check_pass_length(self):
        # pass
        if len(self.password) not in range(5, 26):
            raise ValidationError("Password length should be 5 - 25 symbols")

    def check_pass_letters(self):
        # pass
        letters = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
        for i in self.password:
            if i.lower() not in letters:
                raise ValidationError("Password should contain only english letters, number & «_»")

    def check_pass(self):
        self.check_pass_length()
        self.check_pass_letters()

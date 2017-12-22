from django.test import TestCase, Client
from .validators import *


class TestAuthentication(TestCase):
    def setUp(self):
        self.client = Client()

    # def test_client_response_true(self):
    #     self.assertEqual(self.client.get('/login').status_code, 200)

    def test_validate_login_bad_data_rises_ValidationError(self):
        with self.assertRaises(ValidationError):
            LoginValidation("bad./=login").check_username_letters()

    def test_validate_login_bad_data_rises_ValidationError2(self):
        with self.assertRaises(ValidationError):
            LoginValidation("Русские буквы").check_username_letters()

    # def test_validate_login_good_data_return_none(self):
    #     self.assertIsNone(LoginValidation("good_login").check_username_letters())

    def test_validate_login_bad_length_rises_ValidationError(self):
        with self.assertRaises(ValidationError):
            LoginValidation("45").check_username_length()

    def test_validate_login_bad_length_rises_ValidationError2(self):
        with self.assertRaises(ValidationError):
            LoginValidation("4" * 26).check_username_length()

    # def test_validate_login_good_length_return_none(self):
    #     self.assertIsNone(LoginValidation("good_login").check_username_length())
        
    def test_validate_password_bad_data_rises_ValidationError(self):
        with self.assertRaises(ValidationError):
            LoginValidation("bad./=pass").check_username_letters()

    def test_validate_password_bad_data_rises_ValidationError2(self):
        with self.assertRaises(ValidationError):
            LoginValidation("Русские буквы").check_username_letters()

    # def test_validate_password_good_data_return_none(self):
    #     self.assertIsNone(LoginValidation("simple_login").check_username_letters())

    def test_validate_password_bad_length_rises_ValidationError(self):
        with self.assertRaises(ValidationError):
            LoginValidation("45").check_username_length()

    def test_validate_password_bad_length_rises_ValidationError2(self):
        with self.assertRaises(ValidationError):
            LoginValidation("4" * 26).check_username_length()

    # def test_validate_password_good_length_return_none(self):
    #     self.assertIsNone(LoginValidation("good_pass").check_username_length())







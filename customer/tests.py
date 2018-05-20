from django.test import TestCase, Client
from django.urls import reverse

from customer.models import Customer


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('/registration')
        self.assertEqual(response.status_code, 200)

    def test_page_template(self):
        """ Проверяет используется ли шаблон register.html """
        response = self.client.get('/registration')
        self.assertTemplateUsed(response, 'myAuth/registration.html')


class LoginViewTest(TestCase):

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_page_template(self):
        """ Проверяет используется ли шаблон login.html """
        response = self.client.get('/login')
        self.assertTemplateUsed(response, 'myAuth/login.html')


class LoginTest(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Pavel',
            'phone': '293291555',
            'address': 'doroshevicha 3'

        }
        # name = models.CharField(max_length=255)
        # phone = models.DecimalField(max_digits=9, decimal_places=0)
        # address = models.TextField()
        # created = models.DateTimeField(auto_now_add=True)
        # avatar = models.ImageField(upload_to="images/avatars/%Y/%m/%d", blank=True)
        self.obj = Customer.objects.create(**self.data)

    def test_customer_exists_name_return_true(self):
        customer = Customer.objects.get(name=self.data['name'])

        self.assertEqual(self.obj, customer)

    def test_customer_exists_phone_return_true(self):
        customer = Customer.objects.get(phone=self.data['phone'])

        self.assertEqual(self.obj, customer)

    def test_customer_exists_address_return_true(self):
        customer = Customer.objects.get(address=self.data['address'])

        self.assertEqual(self.obj, customer)

    def test_customer_exists_return_false(self):
        with self.assertRaises(KeyError):
            Customer.objects.get(phone=self.data['121212'])

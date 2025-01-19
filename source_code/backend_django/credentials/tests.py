from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Credential
from .views import register_view, login_view, logout_view, dashboard_view

# Test for Registration View
class RegistrationViewTest(TestCase):

    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credentials/register.html')

    def test_register_user(self):
        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_authenticated_user_redirect(self):
        self.client.force_login(User.objects.create_user(username='existinguser', password='password'))
        response = self.client.get(reverse('register'))
        self.assertRedirects(response, reverse('dashboard'))

# Test for Login View
class LoginViewTest(TestCase):

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credentials/login.html')

    def test_login_success(self):
        user = User.objects.create_user(username='testuser', password='securepassword123')
        response = self.client.post(reverse('login'), data={
            'username': 'testuser',
            'password': 'securepassword123',
        })
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), data={
            'username': 'wronguser',
            'password': 'wrongpassword',
        })
        self.assertFormError(response, 'form', None, 'Invalid username or password.')

# Test for Dashboard View
class DashboardViewTest(TestCase):

    def test_dashboard_access_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='securepassword123')
        self.client.force_login(user)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credentials/dashboard.html')

    def test_dashboard_redirect_unauthenticated_user(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('dashboard'))

# Test for Logout View
class LogoutViewTest(TestCase):

    def test_logout_user(self):
        user = User.objects.create_user(username='testuser', password='securepassword123')
        self.client.force_login(user)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(response.context['user'].is_authenticated)

# Test for Credential Model
class CredentialModelTest(TestCase):

    def test_create_credential(self):
        user = User.objects.create_user(username='testuser', password='securepassword123')
        credential = Credential.objects.create(user=user, credential_value="TestCredential123")
        self.assertEqual(credential.user, user)
        self.assertEqual(credential.credential_value, "TestCredential123")

    def test_unique_constraint_on_credentials(self):
        user = User.objects.create_user(username='testuser', password='securepassword123')
        Credential.objects.create(user=user, credential_value="TestCredential123")
        with self.assertRaises(Exception):
            Credential.objects.create(user=user, credential_value="TestCredential123")  # Duplicate value

# Test for URL Configuration
class URLConfigurationTest(TestCase):

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_view)

    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard_view)

from bx_django_utils.test_utils.html_assertion import HtmlAssertionMixin
from django.conf import LazySettings, settings
from django.test.testcases import TestCase
from django.urls.base import reverse


class DjangoYnhTestCase(HtmlAssertionMixin, TestCase):
    def setUp(self):
        super().setUp()

        # Always start a fresh session:
        self.client = self.client_class()

    def test_settings(self):
        self.assertIsInstance(settings, LazySettings)
        self.assertTrue(settings.configured)
        self.assertEqual(settings.SETTINGS_MODULE, 'scovie.settings.test')
        self.assertEqual(settings.ROOT_URLCONF, 'scovie.urls')
        self.assertFalse(settings.DEBUG)

    def test_auth(self):
        self.assertEqual(reverse('admin:index'), '/admin/')

        # SecurityMiddleware should redirects all non-HTTPS requests to HTTPS:
        assert settings.SECURE_SSL_REDIRECT is True
        response = self.client.get('/admin/', secure=False)
        self.assertRedirects(
            response,
            status_code=301,  # permanent redirect
            expected_url='https://testserver/admin/',
            fetch_redirect_response=False,
        )

        response = self.client.get('/admin/', secure=True)
        self.assertRedirects(
            response,
            expected_url='/admin/login/?next=%2Fadmin%2F',
            fetch_redirect_response=False,
        )

from bx_django_utils.test_utils.html_assertion import HtmlAssertionMixin
from bx_django_utils.test_utils.users import make_test_user
from django.test.testcases import TestCase
from django.urls.base import reverse


class LoginRequiredViewTestCase(HtmlAssertionMixin, TestCase):
    def test_urls(self):
        self.assertEqual(reverse('login-required-view'), '/login-required/')

        ###############################################################################
        # Test as anonymous user

        with self.assertLogs('scovie') as logs:
            response = self.client.get(path='/login-required/', secure=True)
            self.assertRedirects(
                response,
                expected_url='/admin/login/?next=%2Flogin-required%2F',
                fetch_redirect_response=False,
            )
        self.assertEqual(
            logs.output,
            [
                'INFO:scovie.views:'
                'User: "AnonymousUser" do not pass the "LoginRequired" check'
            ],
        )

        ###############################################################################

        user = make_test_user(username='Mr. Test User')
        self.client.force_login(user)

        with self.assertLogs('scovie') as logs:
            response = self.client.get(path='/login-required/', secure=True)
            self.assertRedirects(
                response,
                expected_url='/admin/',
                fetch_redirect_response=False,
            )
        self.assertEqual(
            logs.output,
            [
                'INFO:scovie.views:'
                'User: "Mr. Test User" pass the "LoginRequired" check, ok.'
            ],
        )
        self.assert_messages(
            response, expected_messages=['You pass the "LoginRequired" check, ok.']
        )

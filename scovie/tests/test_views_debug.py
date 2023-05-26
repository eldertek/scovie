import os

from bx_django_utils.test_utils.html_assertion import (
    HtmlAssertionMixin,
    assert_html_response_snapshot,
)
from bx_django_utils.test_utils.users import make_test_user
from django.test.testcases import TestCase
from django.urls.base import reverse

from scovie import __version__


class DemoViewTestCase(HtmlAssertionMixin, TestCase):
    def test_urls(self):
        self.assertEqual(reverse('admin:index'), '/admin/')
        self.assertEqual(reverse('debug-view'), '/')

        ###############################################################################
        # Test as anonymous user

        with self.assertLogs('scovie') as logs:
            response = self.client.get(path='/', secure=True)
        self.assert_html_parts(
            response,
            parts=(
                f'<h2>YunoHost Django Example Project v{__version__}</h2>',
                '<a href="/admin/">Django Admin</a>',
                '<p>Log in to see more information</p>',
                '<tr><td>User:</td><td>AnonymousUser</td></tr>',
                '<tr><td>META:</td><td></td></tr>',
            ),
        )
        self.assertEqual(
            logs.output, ['INFO:scovie.views:DebugView request from user: AnonymousUser']
        )
        assert_html_response_snapshot(response, query_selector='#container', validate=False)

        ###############################################################################

        user = make_test_user(username='Mr. Test User')
        self.client.force_login(user)

        with self.assertLogs('scovie') as logs:
            response = self.client.get(path='/', secure=True)
        self.assert_html_parts(
            response,
            parts=(
                f'<h2>YunoHost Django Example Project v{__version__}</h2>',
                '<a href="/admin/">Django Admin</a>',
                '<tr><td>User:</td><td>Mr. Test User</td></tr>',
                f'<tr><td>Process ID:</td><td>{os.getpid()}</td></tr>',
            ),
        )
        self.assertEqual(
            logs.output, ['INFO:scovie.views:DebugView request from user: Mr. Test User']
        )

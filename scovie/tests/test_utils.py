from unittest.case import TestCase

from django_yunohost_integration.test_utils import generate_basic_auth


class TestUtilsTestCase(TestCase):
    def test_generate_basic_auth(self):
        assert generate_basic_auth(username='test', password='test123') == 'basic dGVzdDp0ZXN0MTIz'

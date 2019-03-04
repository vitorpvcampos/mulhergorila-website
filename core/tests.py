from django.test import RequestFactory, TestCase, Client

from .views import index


class HomeViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_view_status_code_is_ok(self):
        request = self.factory.get('/')

        response = index(request)
        self.assertEqual(response.status_code, 200)

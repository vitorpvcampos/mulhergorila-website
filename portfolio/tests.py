from django.test import RequestFactory, TestCase, Client

from .models import Project
from .views import portfolio, portfolio_detail


class PortfolioViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Portfolio projects
        self.portfolio_web_01 = Project.objects.create(title='Projeto Web 01',
                                                       description='Projeto web Teste')

    def test_portfolio_view_status_code_is_ok(self):
        request = self.factory.get('/portfolio/')

        response = portfolio(request)
        self.assertEqual(response.status_code, 200)

    def test_portfolio_detail_view_status_code_is_ok(self):
        request = self.factory.get('/portfolio/projeto/projeto-web-01')

        response = portfolio_detail(request, slug=self.portfolio_web_01.slug)
        self.assertEqual(response.status_code, 200)

    # def test_portfolio_detail_view_does_not_exist(self):
    #     request = self.factory.get('/portfolio/projeto/projeto-nao-existe')
    #
    #     response = portfolio_detail(request, slug='projeto-nao-existe')
    #     self.assertEqual(response.status_code, 500)

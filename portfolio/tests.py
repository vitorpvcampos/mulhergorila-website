from django.test import RequestFactory, TestCase, Client

from .models import Project, Category
from .views import portfolio, portfolio_detail


class PortfolioViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Test Category
        self.category_sample = Category.objects.create(name='Sample')

        # Portfolio projects
        self.portfolio_web_01 = Project.objects.create(title='Projeto Web 01',
                                                       description='Projeto web Teste',
                                                       category=self.category_sample)

    def test_portfolio_view_status_code_is_ok(self):
        request = self.factory.get('/portfolio/')

        response = portfolio(request)
        self.assertEqual(response.status_code, 200)

    def test_portfolio_detail_view_status_code_is_ok(self):
        request = self.factory.get('/portfolio/projeto/projeto-web-01')

        response = portfolio_detail(request, slug=self.portfolio_web_01.slug)
        self.assertEqual(response.status_code, 200)

    def test_project_title_returns(self):
        projeto = self.portfolio_web_01
        self.assertEquals('Projeto Web 01', projeto.title)

    def test_project_str_returns(self):
        projeto_str = self.portfolio_web_01
        self.assertEquals('Projeto Web 01', projeto_str.__str__())

    def test_category_name_returns(self):
        categoria = self.category_sample
        self.assertEquals('Sample', categoria.name)

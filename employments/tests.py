from django.contrib.auth.models import User
from django.test import TestCase, Client
from bs4 import BeautifulSoup

# Create your tests here.
from employments.models import EmploymentsPost, Company


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.obama = User.objects.create(username="obama", password='helloworld')
        self.mike = User.objects.create(username='mike', password='helloworld')

    def test_search(self):
        # 채용공고 세팅
        company1 = Company.objects.create(
            id=1,
            company_name="samsung",
            company_nationality="korea",
            company_address="서울시",

            user=self.mike

        )

        employmentsPost1 = EmploymentsPost.objects.create(
            employments_position='position1',
            employments_compensation=100000,
            employments_text='text 하이',
            employments_tech_to_use='python',
            employments_author=self.obama,
            company_id=company1,
        )

        employmentsPost2 = EmploymentsPost.objects.create(
            employments_position='position1',
            employments_compensation=100000,
            employments_text='text 헬로',
            employments_tech_to_use='python',
            employments_author=self.obama,
            company_id=company1,
        )

        response = self.client.get('/employments/search/하이/')
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual(response.status_code, 200)
        print(soup.body.text)
        # self.assertIn(employmentsPost1, soup.body.text)
        # self.assertNotIn(employmentsPost2, soup.body.text)

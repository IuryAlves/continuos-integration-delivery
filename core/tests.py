from django.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse

class IndexTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_index_should_return_status_code_200(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response=response,
            template_name='index2.html'
        )

from django.test import TestCase
from django.shortcuts import reverse 

class PerformancePageTest(TestCase):

    def test_status_code(self):
        # TODO some sort of test
        response = self.client.get(reverse('performance-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "performance.html")

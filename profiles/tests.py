from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_home_page(self):
        """ Test profile page renders correct page """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'profiles/profile.html')

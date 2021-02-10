from django.test import TestCase


class TestViews(TestCase):
    def test_chat_rooms_redirect_when_not_logged_in(self):
        """ Test chat rooms home page renders correct page """
        response = self.client.get('/chat_rooms/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'home/index.html')

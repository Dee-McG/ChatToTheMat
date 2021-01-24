from django.test import TestCase


class TestViews(TestCase):
    def test_chat_rooms_home_page(self):
        """ Test chat rooms home page renders correct page """
        response = self.client.get('/chat_rooms/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'chat_rooms/chat_home.html')
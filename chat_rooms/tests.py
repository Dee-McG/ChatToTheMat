from django.test import TestCase


class TestViews(TestCase):
    def test_chat_rooms_redirect_when_not_logged_in(self):
        """ Test chat rooms redirects when not logged in """
        response = self.client.get('/chat_rooms/room/general')
        self.assertEqual(response.status_code, 302)

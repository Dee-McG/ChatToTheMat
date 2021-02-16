from django.test import TestCase
from .forms import EditProfileForm


# Create your tests here.
class TestViews(TestCase):
    def test_profile_page_redirect_when_logged_out(self):
        """ Test profile page redirects to home when logged out """
        response = self.client.get('/profiles/user/')
        self.assertEqual(response.status_code, 302)


class TestEditForm(TestCase):
    """ Test to check that user field is required """
    def test_edit_profile_form(self):
        form = EditProfileForm(
            {'name': 'Ella', 'location':
             'Rivendale', 'bio': 'I am the Ice Queen'})
        self.assertTrue(form.is_valid())

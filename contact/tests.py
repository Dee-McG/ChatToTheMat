from django.test import TestCase
from .forms import ContactForm


class TestViews(TestCase):
    def test_contact_page(self):
        """ Test contact page template renders correct page """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'contact/contact.html')


class TestContactForm(TestCase):
    def test_required_fields(self):
        """ Test to validate name, contact_reason and 
        comments fields are required """
        form = ContactForm({'name': '', 'contact_reason': '', 'comments': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('contact_reason', form.errors.keys())
        self.assertIn('comments', form.errors.keys())
        self.assertEquals(form.errors['name'][0], 'This field is required.')
        self.assertEquals(form.errors['contact_reason'][0], 'This field is required.')
        self.assertEquals(form.errors['comments'][0], 'This field is required.')
    
    def test_email_field_is_not_required(self):
        """ Test to check that email field is not required """
        CONTACT_CHOICES = (
            ('breach_of_tos', 'BREACH OF TOS'),
            ('general_query', 'GENERAL QUERY'),
            ('technical_issue', 'TECHNICAL ISSUE'),
            ('subscription_query', 'SUBSCRIPTION QUERY'),
)
        form = ContactForm({'contact_reason': 'general_query', 'name': 'Test', 'comments': 'Test'})
        self.assertTrue(form.is_valid())

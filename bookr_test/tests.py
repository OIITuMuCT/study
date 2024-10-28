from django.test import TestCase, Client
from .models import Publisher


# Create your tests here.
class TestPublisherModel(TestCase):
    """Test the publisher model."""

    def setUp(self):
        self.p = Publisher(
            name="Packt", website="www.packt.com", email="contact@pact.com"
        )

    def test_create_publisher(self):
        self.assertIsNotNone(self.p, Publisher)
        print("Test create p")

    def test_str_representation(self):
        self.assertEqual(str(self.p), "Packt")
        print("Test representation {}".format(self.p))


class TestGreetingView(TestCase):
    """ Test the greeting view. """
    def setUp(self):
        self.client = Client()
    
    def test_greeting_view(self):
        response = self.client.get('/test/greeting')
        self.assertEqual(response.status_code, 200)


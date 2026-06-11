from django.test import SimpleTestCase
from django.urls import reverse

class HealthCheckTests(SimpleTestCase):
    def test_health_check_endpoint(self):
        """Test that the health check API returns a 200 status and valid JSON."""
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'healthy')

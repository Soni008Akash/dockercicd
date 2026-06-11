from django.test import SimpleTestCase
from django.urls import reverse

class HealthCheckTests(SimpleTestCase):
    def test_health_check_endpoint(self):
        """Test that the health check API returns a 200 status and valid JSON."""
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'healthy')


class CalculationTests(SimpleTestCase):
     def test_addition(self):
        """Test that our addition math logic works perfectly."""
        calc = Calculation()
        result = calc.add()
        self.assertEqual(result, 30)

class Calculation():
    a = 10
    b = 20
    def add(self):
        return self.a + self.b        
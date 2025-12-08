"""
Tests unitaires pour l'application calculator.
Ces tests démontrent comment tester les fonctions et les vues Django.
"""
from django.test import TestCase, Client
from django.urls import reverse
from .utils import add, subtract, multiply, divide


class CalculatorUtilsTests(TestCase):
    """Tests pour les fonctions utilitaires de la calculatrice."""

    def test_add_positive_numbers(self):
        """Test de l'addition de deux nombres positifs."""
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test de l'addition de deux nombres négatifs."""
        result = add(-5, -3)
        self.assertEqual(result, -8)

    def test_subtract(self):
        """Test de la soustraction."""
        result = subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        """Test de la multiplication."""
        result = multiply(4, 5)
        self.assertEqual(result, 20)

    def test_divide(self):
        """Test de la division."""
        result = divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero(self):
        """Test de la division par zéro (doit lever une exception)."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Division par zéro", str(context.exception))


class CalculatorViewsTests(TestCase):
    """Tests pour les vues de l'application calculator."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.client = Client()

    def test_index_view(self):
        """Test de la page d'accueil."""
        response = self.client.get(reverse('calculator:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Calculatrice CI/CD Demo')

    def test_calculate_addition(self):
        """Test de l'endpoint de calcul avec addition."""
        response = self.client.get(
            reverse('calculator:calculate'),
            {'operation': 'add', 'a': '5', 'b': '3'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 8)
        self.assertEqual(data['operation'], 'add')

    def test_calculate_division(self):
        """Test de l'endpoint de calcul avec division."""
        response = self.client.get(
            reverse('calculator:calculate'),
            {'operation': 'divide', 'a': '10', 'b': '2'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 5.0)

    def test_calculate_division_by_zero(self):
        """Test de la division par zéro via l'endpoint."""
        response = self.client.get(
            reverse('calculator:calculate'),
            {'operation': 'divide', 'a': '10', 'b': '0'}
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_calculate_invalid_operation(self):
        """Test avec une opération invalide."""
        response = self.client.get(
            reverse('calculator:calculate'),
            {'operation': 'invalid', 'a': '5', 'b': '3'}
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

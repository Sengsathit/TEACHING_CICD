"""
Fonctions utilitaires pour la calculatrice.
Ce module sera utilisé pour démontrer les tests unitaires.
"""


def add(a, b):
    """
    Additionne deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        La somme de a et b
    """
    return a + b


def subtract(a, b):
    """
    Soustrait b de a.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        La différence de a et b
    """
    return a - b


def multiply(a, b):
    """
    Multiplie deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Le produit de a et b
    """
    return a * b


def divide(a, b):
    """
    Divise a par b.

    Args:
        a: Premier nombre (dividende)
        b: Deuxième nombre (diviseur)

    Returns:
        Le quotient de a et b

    Raises:
        ValueError: Si b est égal à zéro
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

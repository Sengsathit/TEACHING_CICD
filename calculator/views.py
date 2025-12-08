from django.shortcuts import render
from django.http import JsonResponse
from .utils import add, subtract, multiply, divide


def index(request):
    """Page d'accueil de la calculatrice."""
    return render(request, 'calculator/index.html')


def calculate(request):
    """
    Endpoint pour effectuer des calculs.

    Paramètres GET:
        - operation: add, subtract, multiply, divide
        - a: premier nombre
        - b: deuxième nombre
    """
    try:
        operation = request.GET.get('operation')
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))

        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
        }

        if operation not in operations:
            return JsonResponse({
                'error': 'Opération invalide'
            }, status=400)

        result = operations[operation](a, b)

        return JsonResponse({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        })

    except ValueError as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': f"Erreur lors du calcul: {str(e)}"
        }, status=500)

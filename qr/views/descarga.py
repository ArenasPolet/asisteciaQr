# En qr/views/descarga.py
from django.shortcuts import render

def descarga(request):
    # Lógica de la vista aquí
    return render(request, 'descarga.html', {})
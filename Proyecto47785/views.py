from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
	return HttpResponse("Hola Django - Coder")


def saludo_html(request):
	return HttpResponse("<b>Hola Django</b> - Coder")


def saludo_nombre(request, nombre):
	return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Django</b> - Coder")

def saludo_plantilla(request):
	# logica del negocio
	contexto = {
		"nombre": "Luis",
		"edad": 35,
		"hijos": [
			{
				"nombre": "Hijo1",
				"edad": 1
			},
			{
				"nombre": "Hijo2",
				"edad": 2
			},
		]
	}
	return render(request, "index.html", contexto)


from django.http import HttpResponse


def saludo(request):
	return HttpResponse("Hola Django - Coder")


def saludo_html(request):
	return HttpResponse("<b>Hola Django</b> - Coder")


def saludo_nombre(request, nombre):
	return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Django</b> - Coder")

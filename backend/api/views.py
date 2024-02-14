from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Olá, esta é a resposta da sua API."})

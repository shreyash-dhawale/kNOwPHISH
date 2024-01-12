from django.http import JsonResponse
from .utils import detect_phishing

def detect_phishing_view(request):
    if request.method == 'GET':
        url = request.GET.get('url', '')
        result = detect_phishing(url)
        response_data = {
            'url': url,
            'result': result
        }
        return JsonResponse(response_data)

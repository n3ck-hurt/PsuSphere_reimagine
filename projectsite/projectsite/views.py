from django.conf import settings
from django.http import HttpResponse


def service_worker(request):
    sw_path = settings.BASE_DIR / 'static' / 'service-worker.js'
    try:
        with open(sw_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='application/javascript')
    except FileNotFoundError:
        return HttpResponse('// Service worker not found', content_type='application/javascript', status=404)

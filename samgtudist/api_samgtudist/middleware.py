from django.db.models import F

from hitcount.models import HitCount


class HitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            material_id = request.resolver_match.kwargs.get('pk')
            HitCount.objects.filter(
                    object_pk=int(material_id)).update(hits=F('hits')+1)
        except Exception:
            pass
        return response

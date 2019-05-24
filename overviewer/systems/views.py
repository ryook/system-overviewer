from django.views.generic import View
from django.http.response import JsonResponse

from .models import System


class SystemAPIView(View):

    def get(self, request, *args, **kwargs):
        layer = self.request.GET.get("layer")
        if not layer:
            layer = 1
        systems = System.objects.filter(layer=layer)
        data = {}
        nodes = []
        links = []
        for s in systems:
            nodes.append({
                "id": s.id,
                "label": s.name
            })

            for c in s.connect_to.values():
                links.append({
                    "source": s.id, 
                    "target": c["id"]
                })
            
        data["nodes"] = nodes
        data["links"] = links
        return JsonResponse(data)

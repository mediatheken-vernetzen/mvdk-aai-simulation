from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    z = [1, 2, 3, 4]
    context = {
        'z': z,
    }
    return render(request, "wayf/index.html", context)
    # return HttpResponse(template.render(context, request))
    
    """
    auth_queryset = {"TU Berlin", "Frankfurt am Main"}
    return HttpResponse("WAYF index")
    """

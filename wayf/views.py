from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings

def index(request):
    universities = ["Goethe-Universität", "Freie Universität Berlin", "Technische Universiät Berlin"]
    universities_abr = ["ffm", "fub", "tub"]
    context = {
        'universities': universities,
        'universities_abr': universities_abr,
    }

    return render(request, "wayf/index.html", context)

def redirect_uni(request):
    uni = request.POST.get("uni_select")
    return redirect('/eduroam_' + uni + '/login/')

@login_required(login_url='/eduroam_ffm/login/')
def success(request):
    return redirect(settings.AAI_REDIRECT_URL)

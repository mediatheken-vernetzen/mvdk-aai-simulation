from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from cryptography.fernet import Fernet

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
    redir = redirect('/eduroam_' + uni + '/login/')
    return redir

@login_required(login_url='/eduroam_ffm/login/')
def success(request):
    keyVar = Fernet.generate_key()
    ferVar = Fernet(keyVar)
    encString = ferVar.encrypt(str(request.user).encode())
    redir = redirect(settings.AAI_REDIRECT_URL)
    redir.headers["token"] = encString
    return redir

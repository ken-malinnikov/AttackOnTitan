from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

MAIN_PAGE_TITLE = "Main page"
TITAN_COLOSS_TITLE = "Armored Titan & Titan Coloss"


# Create your views here.
def index(request):
    contentTamplate = loader.get_template('main_page_content.html')
    context = {
        'title': MAIN_PAGE_TITLE,
        'linkAddress': "titan",
        'linkName': TITAN_COLOSS_TITLE,
        'content': contentTamplate.render(),
    }
    return createPage(context, request)


def titan(request):
    contentTamplate = loader.get_template('titan.html')
    context = {
        'title': TITAN_COLOSS_TITLE,
        'linkAddress': "/",
        'linkName': MAIN_PAGE_TITLE,
        'content': contentTamplate.render(),
    }
    return createPage(context, request)


def login(request):
    return signUp(request, "none")


def signUp(request, display=''):
    contentContext = {'display': display}
    contentTamplate = loader.get_template('auth.html')
    context = {
        'title': TITAN_COLOSS_TITLE,
        'linkAddress': "/",
        'linkName': MAIN_PAGE_TITLE,
        'content': contentTamplate.render(contentContext),
    }
    return createPage(context, request)


def createPage(context, request):
    template = loader.get_template('wrapper.html')
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template 
from django.template import Context

def params(request):
    body = 'Hello, world!<br>'

    body += '<br>Method: ' + request.method + '<br>'
    if request.method == "GET":
        body += '<br>Params:<br>' + parse_query_string(request.GET.urlencode())
    if request.method == "POST":
        body += '<br>Params:<br>' + parse_query_string(request.POST.urlencode())
    return HttpResponse([ body ])

def parse_query_string(query_string):
    query_string_array = query_string.split('&')
    query_string = ''
    for param in query_string_array:
        query_string += param + '<br>'
    return query_string

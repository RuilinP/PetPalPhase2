from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest



def hello(request, name, age):
    return HttpResponse(f"Greeting, {name} is {age} years old")


def myclass(request, code, year, semester):
    if semester.lower() not in ["fall", "winter", "summer"]:
        return HttpResponseBadRequest(f"unknown semester: {semester}")
    return HttpResponse(f"""
    <html>
    <body>
    <h1>{code.upper()}, {semester.capitalize()} {year}</h1>
    </body>
    </html>
    """)
    
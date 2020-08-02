from django.shortcuts import render, HttpResponse


html_base= """
    <h1>***mi web personal***</h1>
    <u1>
        <li><a href="/">portada</a></li>
        <li><a href="/about/">acerca de</a></li>
        <li><a href="/portfolio/">portafolio</a></li>
        <li><a href="/contact/">contacto</a></li>
    </u1>
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")

    

def contact(request):
    return render(request, "core/contact.html")

from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "test" : "Ceci est un test",
        "fake_dict": {"key1": "valeur de la clé 1"}
        }
    return render(request, 'main/home_page.html', context=context)


def about(request):
    return render(request, 'main/about.html')
from django.shortcuts import render


def location(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    return render(request, 'location/location.html')

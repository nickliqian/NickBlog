from django.shortcuts import render


def api_index(request):

    context = {

    }

    return render(request, "apiModel/status.html", context=context)

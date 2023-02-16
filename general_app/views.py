from django.shortcuts import render

# Create your views here.
def advertisment(request):
    return render(request, 'bannerad.html')

def terms(request):
    return render(request, 'terms.html')

def reach(request):
    return render(request, 'reach.html')

def safety(request):
    return render(request, 'safety.html')

def userhelp(request):
    return render(request, 'userhelp.html')
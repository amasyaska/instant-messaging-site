from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def static(request, my_id):
    print("here")
    # if filename contains "/" abort: Django excludes "/" automatically
    return HttpResponse(my_id)
    '''
    static_path = os.path.join(os.path.join(os.path.abspath(__file__), "..", "..", "..", "static"))
    with open(os.path.join(static_path, filename), 'r') as f:
        file_data = f.read()
        response = HttpResponse(file_data)
        response['Content-Type'] = 'application/javascript; charset=utf-8'
    return response
    '''

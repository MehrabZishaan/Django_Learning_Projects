from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
# set Cookie, get cookie, delete cookie
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=60*3)
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name= request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

# Django Session
# Session vs cookie
# Cookie save thake client er browser/database
# Cookie authentication er jnne use kora jay
# dark mode/ light mode, bang/eng language, remember me egular jnne cookie
# Session backend theke save kora hoy
# Session shopping cart er jnne use kora jay

def set_session(request):
    data = {
        'name': 'rahim',
        'age': 23,
        'language': 'Bangle'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    data = request.session
    if 'name' in data:
        request.session.modified = True # 10sec er por expired hoye jay, but ekhn 10sec er majhe joto bar request korbe toto bar 10 sec kore time barbe
        return render(request, 'get_session.html', {'data': data})
    else:
        return HttpResponse("Your session has been expired. Login again.")
        
    
def del_session(request):
    # # To delete a single data
    # data = request.session
    # if 'name' in data:
    #     del data['name']
    #To delete the full session
    data = request.session
    data.flush()
    data.clear_expired()
    return render(request, 'get_session.html', {'data': data})
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse('''
                        <h1>This is courses page</h1>
                        <a href= '/first_app/about/' style="text-decoration: none;"> About &emsp;</a>
                        <a href= '/first_app/contact/' style="text-decoration: none;"> Contact &emsp;</a>
                        <a href= '/second_app/feedback/' style="text-decoration: none;"> Feedback &emsp;</a>
                        
                        ''')
def feedback(request):
    return HttpResponse('''
                        <h1>This is feedback page</h1>
                        <a href= '/first_app/about/' style="text-decoration: none;"> About &emsp;</a>
                        <a href= '/first_app/contact/' style="text-decoration: none;"> Contact &emsp;</a>
                        <a href= '/second_app/courses/' style="text-decoration: none;"> Courses </a>
                        ''')
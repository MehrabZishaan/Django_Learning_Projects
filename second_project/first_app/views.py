from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse('''
                        <h1>This is contact page</h1>
                        <a href= '/first_app/about/' style="text-decoration: none;"> About &emsp;</a>
                        <a href= '/second_app/courses/' style="text-decoration: none;"> Courses &emsp;</a>
                        <a href= '/second_app/feedback/' style="text-decoration: none;"> Feedback </a>
                        ''')
def about(request):
    return HttpResponse('''
                        <h1>This is about page</h1>
                        <a href= '/first_app/contact/' style="text-decoration: none;"> Contact &emsp;</a>
                        <a href= '/second_app/courses/' style="text-decoration: none;"> Courses &emsp;</a>
                        <a href= '/second_app/feedback/' style="text-decoration: none;"> Feedback </a>
                        ''')
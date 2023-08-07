from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1>This is my Homepage</h1>
                        <a href= '/first_app/about/' style="text-decoration: none;"> About &emsp;</a>
                        <a href= '/first_app/contact/' style="text-decoration: none;"> Contact &emsp;</a>
                        <a href= '/second_app/courses/' style="text-decoration: none;"> Courses &emsp;</a>
                        <a href= '/second_app/feedback/' style="text-decoration: none;"> Feedback </a>
                        ''')
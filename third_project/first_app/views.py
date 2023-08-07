from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, './first_app/index.html', context= {'author':'Phitron', 'age': 19, 'marks': 69, 'courses': [
        {
            'id': 1,
            'course': 'C',
            'teacher': 'Rahim'
        },
        {
            'id': 2,
            'course': 'C++',
            'teacher': 'Kahim'
        },
        {
            'id': 3,
            'course': 'Python',
            'teacher': 'Bahim'
        }
    ], 'name': 'I am Mehrab', 'number':96, 'lst': [24,3,10,5], 'blog': 'Lorem ipsum shvbd csdf sdaf sdfsdf asdfgdfg sdfsdfs dfsadfadsf . H dssdfjsdn sdfsdfg sdfgsdfsdfsdf.'})
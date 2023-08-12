from django.shortcuts import render
from first_app.forms import StudentForm
from . models import Teacher, Student
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})

def showData(request):
    # students list for One Teacher
    teacher = Teacher.objects.get(name ='Abdur Rouf')
    students = teacher.student.all()
    for stud in students:
        print(f"{stud.name} {stud.roll} {stud.class_name}")
        
    # teachers list for One Student
    student = Student.objects.get(name ='Ashiq')
    teachers = student.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name} {teacher.subject} {teacher.mobile_number}")
    return render(request, 'show_data.html')

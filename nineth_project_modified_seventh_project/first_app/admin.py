from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel, Friend, Me, Person, Passport, Post, Student, Teacher
# Register your models here.
admin.site.register(StudentModel)

# For Abstract Base class
admin.site.register(StudentInfoModel)
admin.site.register(TeacherInfoModel)

# For Multitable inheritance
# admin.site.register(EmployeeModel)
# admin.site.register(ManagerModel)

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation']
    
@admin.register(ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation', 'take_interview', 'hiring']
    
# For Proxy Model
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'hw']
    
@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'hw']

# For One To One Relation
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'email']
    
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pass_number', 'page', 'validity']

# For One To Many Relation
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post_cap', 'post_details']
    
# For Many To Many Relation
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'class_name']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'student_list', 'mobile_number']
from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f"Roll: {self.roll} Name: {self.name}"
    
# Model inheritance
# 1- Abstract base class
# 2- Multitable inheritance
# 3- Proxy model

# Abstract Base class
class CommonInfo(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfo):
    roll = models.IntegerField()
    section = models.CharField(max_length=30)
    payment = models.IntegerField()
    
class TeacherInfoModel(CommonInfo):
    salary = models.IntegerField()
    
    
# Multitable inheritance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)
    
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# Proxy Model
class Friend(models.Model): # amar friend class e preset ache
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)

# Jekono table ja add kori ta same to same dui ta table e thakbe
class Me(Friend): # ami ajke school e jai nai, tai proxy dibe
    class Meta: # jar jnne proxy dibe tar jnne proxy = True
        proxy = True
        ordering = ['id'] # table data gulo choto theke boro dekhanor jnne ordering kora hoise 

# One To One Relation
class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    
    def __str__(self) -> str:
        return f"Name: {self.name} - Email: {self.email}"
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# One To Many Relation
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True)
    # SET_NULL dewar karone jodi Person delete kori tobuo Post delete hobe na, tokhon user null dekhabe
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=150)
    
# Many to Many Relation
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"Name: {self.name}"
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name= 'teachers')
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=11)
    
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
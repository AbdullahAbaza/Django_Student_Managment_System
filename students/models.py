from django.db import models

# Create your models here.

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField(default=0.0)
    department = models.ForeignKey('Department', related_name='Fk_Student_Department', null=True, on_delete=models.CASCADE)
    register_date_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'student: {self.first_name} {self.last_name}'
    
    class Meta:
        db_table = "Students"
    
    



departments = ['Computer Science', 'Electirical Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Business Administration']
department_choices = sorted([(item, item) for item in departments])
class Department(models.Model):
    department_id = models.PositiveIntegerField(primary_key=True, auto_created=False)
    deparment_name = models.CharField(max_length=100,  choices=department_choices)
    class Meta:
        db_table = "departments"
    
    def __str__(self):
        return f'Department: {self.deparment_name}, Dept_ID: {self.department_id}'
    
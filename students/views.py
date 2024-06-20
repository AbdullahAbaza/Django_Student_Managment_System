from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods


from .models import Student, Department
from .forms import StudentForm
# Create your views here.

def index(request):
    students = Student.objects.select_related('department').all()
    return render(request, 'students/index.html', {'students': students})
    
def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))



def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            new_department = form.cleaned_data['department']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name, 
                last_name = new_last_name, 
                email = new_email, 
                field_of_study = new_field_of_study, 
                gpa = new_gpa, 
                department = new_department
            )
            
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })
        
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
        })
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })


# def edit(request, id):
#     student = get_object_or_404(Student, id=id)  
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the student list or any other page
#     else:
#         form = StudentForm(instance=student)    
#     return render(request, 'students/edit.html', {'form': form, 'student': student})


def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
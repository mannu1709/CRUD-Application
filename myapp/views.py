from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q 
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.

#-------> add data form to database <------------

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'myapp/home.html', {'form': form,})

#--------> for edit student data <---------------
def edit_student(request,id):
    student= get_object_or_404(Student,id=id)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=StudentForm(instance=student)

    return render(request, 'myapp/edit.html', {'form': form})

#--------> for delete student data <---------------
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')

#--------> for view all student data <---------------
def all_students(request):
    query = request.GET.get('q', '')  # Get search input
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query)
        )

    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/students_list.html', {
        'page_obj': page_obj,
        'query': query,  # Pass search input back to template
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .form import StudentForm

def add_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})



def student_list(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(full_name__icontains=search)
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html',
                  {'students': students})



def update_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request,
                  'update_student.html',
                  {'form': form})


def delete_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request,
                  'delete_student.html',
                  {'student': student})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Groups, Students, Marks


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone_number = request.POST.get('phone_number')
        group_id = request.POST.get('group_id')
        student = Students.objects.create(name=name, surname=surname, phone_number=phone_number, group_id=group_id)
    edu_groups = Groups.objects.all()
    edu_students = Students.objects.all()

    contex = {'groups': edu_groups, 'students': edu_students}

    return render(request, 'index.html', context=contex)


def group(request):
    groups = Groups.objects.all()

    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        students = Students.objects.filter(group_id=group_id)
        context = {'groups': groups, 'students': students}

        return render(request, 'index.html', context=context)

    context = {'groups': groups}

    return render(request, 'imdex.html', context=context)


def mark(request):
    students = Students.objects.all()
    marks = Marks.objects.all()
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        mark = request.POST.get('mark')
        student_mark = Marks.objects.create(student_id=student_id, mark=mark)
        marks = Marks.objects.all()
        students = Students.objects.all()

        context = {'marks': marks, 'students': students}
        return render(request, 'mark.html', context=context)

    context = {'students': students, "marks": marks}
    return render(request, 'mark.html', context=context)


def edit_student(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone_number = request.POST.get('phone_number')
        group_id = request.POST.get('group_id')
        groups = Groups.objects.get(id=group_id)
        student = Students.objects.get(id=pk)

        student.name = name
        student.surname = surname
        student.phone_number = phone_number
        student.group = group
        student.save()

    edu_groups = Groups.objects.all()
    context = {'groups':edu_groups, 'students': student}



# def delete_student(request, pk):
#     students = Students.objects.get(id=pk)
#     students.delete()
#
#     context = {'students': students}
#
#     return render(request, 'delete_student.html', context)



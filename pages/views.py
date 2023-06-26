from django.shortcuts import render
from students import models as student_moduls
from grants import models as grants_models


def HomePageView(request):
    return render(request, 'index.html')


def GrantListView(request):
    all_grants = grants_models.Grant.objects.all()

    context = {
        'all_grants': all_grants
    }
    return render(request, 'grant_list.html', context)


def GrantDetailView(request, pk):
    grant = grants_models.Grant.objects.filter(pk=pk).first()
    context = {'grant': grant}
    return render(request, 'grant_detail.html', context)


def StudentListView(request, grant_id=None):
    print('#'*10)
    print(grant_id)
    if grant_id != 0:
        sc_items = grants_models.ScienceDirection.objects.filter(
            grant=grants_models.Grant.objects.last()).all()
        return render(request, 'grant_student_list.html', {'sc_items': sc_items})
    students = student_moduls.Student.objects.all()
    print("et biyaq ishlab ketdi")
    context = {'students': students}
    return render(request, 'grant_student_list.html', context)


def StudentDetailView(request, pk):
    student = student_moduls.Student.objects.filter(pk=pk).first()
    articles = student_moduls.Article.objects.filter(student=student)
    wins = student_moduls.Win.objects.filter(student=student)
    context = {
        'student': student,
        'articles': articles,
        'wins': wins
    }
    print(articles)
    return render(request, 'grant_student_detail.html', context)


def FacultyListView(request):
    faculties = student_moduls.Faculty.objects.all()
    print(faculties.first().students_count)
    return render(request, 'faculty_list.html', {'faculties': faculties})

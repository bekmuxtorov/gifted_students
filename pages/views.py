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
    if grant_id:
        permitted = grants_models.ScienceDirection.objects.filter(
            grant=grant_id)
        print(permitted)
        students = student_moduls.Student.objects.filter()
    students = student_moduls.Student.objects.all()
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

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from students import models as student_moduls
from grants import models as grants_models
from grants.forms import GrantForm


@login_required(login_url='/accounts/login/')
def HomePageView(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def GrantListView(request):
    all_grants = grants_models.Grant.objects.all()

    context = {
        'all_grants': all_grants
    }
    return render(request, 'grant_list.html', context)


@login_required(login_url='/accounts/login/')
def GrantDetailView(request, pk):
    grant = grants_models.Grant.objects.filter(pk=pk).first()
    context = {'grant': grant}
    return render(request, 'grant_detail.html', context)


@login_required(login_url='/accounts/login/')
def StudentListView(request, grant_id=None):
    if grant_id != 0:
        sc_items = grants_models.ScienceDirection.objects.filter(
            grant=grants_models.Grant.objects.last()).all()
        return render(request, 'grant_student_list.html', {'sc_items': sc_items})
    students = student_moduls.Student.objects.all()
    context = {'students': students}
    return render(request, 'grant_student_list.html', context)


@login_required(login_url='/accounts/login/')
def StudentDetailView(request, pk):
    student = student_moduls.Student.objects.filter(pk=pk).first()
    articles = student_moduls.Article.objects.filter(student=student)
    wins = student_moduls.Win.objects.filter(student=student)

    # student = student_moduls.Student.objects.get(id=pk)
    text = request.POST.get('letter')
    message_student = student_moduls.Student.objects.get(id=pk)
    messages = student_moduls.Message.objects.all().filter(student=message_student).order_by('-create_at')
    print(message_student)
    context = {
        'student': student,
        'articles': articles,
        'wins': wins,
        'message_student': message_student,
        'messages': messages
    }
    try:
        letter = student_moduls.Message.objects.create(student=student, letter=text)
        letter.save()
    except Exception as err:
        
        return render(request, "grant_student_detail.html", context)
    

    return render(request, 'grant_student_detail.html', context)


@login_required(login_url='/accounts/login/')
def create_grant(request):
    form = GrantForm(request.POST or None)
    if request.method == "POST":
        form = GrantForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            print(obj)
            return redirect('grants')
    context = {
        "form":form
    }
    return render(request, 'grant_form.html', context)


@login_required(login_url='/accounts/login/')
def update_grant(request, pk):
    context = {}

    obj = grants_models.Grant.objects.get(id=pk)
    form = GrantForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('grants')
    
    context["form"] = form
    return render(request, "grant_form.html", context)


@login_required(login_url='/accounts/login/')
def delete_grant(request, pk):
    context = {}

    obj = grants_models.Grant.objects.get(id=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('grants')
    context["obj"] = obj
    return render(request, "grant_delete.html", context)

@login_required(login_url='/accounts/login/')
def FacultyListView(request):
    faculties = student_moduls.Faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})


def logout_view(request):
    logout(request)
    return redirect('home')
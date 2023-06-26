from django.contrib import admin
from django.utils.html import format_html

from .models import Faculty, SubFaculty, Student, Article, Win, Message

# Register your models here.


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', "id", 'create_at', 'student_count')
    search_fields = ('name',)

    def student_count(self, obj):
        return obj.students.count()
    student_count.short_description = 'Studentlar soni'


@admin.register(SubFaculty)
class SubFacultyAdmin(admin.ModelAdmin):
    list_display = ('name', "id", 'faculty', 'create_at', 'student_count')
    list_filter = ('faculty',)
    search_fields = ('name',)

    def student_count(self, obj):
        return obj.students.count()
    student_count.short_description = 'Studentlar soni'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', "id", 'faculty', 'articles_count',
                    'group', 'course', 'region')
    search_fields = ('get_full_name', 'region', 'district', 'street')
    list_filter = ('faculty', 'course')

    def articles_count(self, obj):
        return obj.articles.count()
    articles_count.short_description = 'Maqolalari soni'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id', 'student__base_student__first_name',
                     'student__base_student__last_name')
    list_display = ('student', 'name', 'download_article')
    ordering = ('create_at',)

    def download_article(self, obj):
        return format_html(f"<a href='{obj.file.url}'>Ko'rish</a>")
    download_article.short_description = 'Ko\'rish'


@admin.register(Win)
class WinAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id', 'student__base_student__first_name',
                     'student__base_student__last_name')
    list_display = ('student', 'name', 'download_article')
    ordering = ('create_at',)

    def download_article(self, obj):
        return format_html(f"<a href='{obj.file.url}'>Ko'rish</a>")
    download_article.short_description = 'Ko\'rish'



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('student', 'letter', 'create_at')
    list_filter = ('letter',)
    search_fields = ('student',)

    def message_count(self, obj):
        return obj.letter.count()
    message_count.short_description = 'Xabarlar soni'
from django.contrib import admin

# Register your models here.
from vege.models import *

admin.site.register(Receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)


admin.site.register(Subject)
# admin.site.register(SubjectMaks)

class SubjectMaksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMaks, SubjectMaksAdmin)     

# ////////////////////////////////////////////////////////////////
from django.db.models import Sum

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_report_card_generation'] 
    ordering = ['-student_rank']

    def total_marks(self , obj):
        subject_marks = SubjectMaks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        return 0

admin.site.register(ReportCard , ReportCardAdmin)
from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5 #This right here is what makes it a list

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline] #An option to add 5 lessons will appear when adding a course

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
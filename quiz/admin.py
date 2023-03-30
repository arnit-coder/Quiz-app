from django.contrib import admin
from quiz.models import Question

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)


admin.site.register(Question, QuizAdmin)
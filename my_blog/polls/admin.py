from django.contrib import admin
from .models import Choice, Question, Answer

# admin.site.register(Question)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
   list_display = ('get_question', 'choice_text', 'votes')       # pkt 6
   list_filter = ('question', 'votes')
   search_fields = ('choice_text', 'question__question_text',)
   # raw_id_fields = ('question',)                                 # pkt 7

   @admin.display(description='Question text', )                 # pkt 6
   def get_question(self, obj):
       return obj.question.question_text


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
   list_display = ('question_text', 'pub_date', 'is_open_question')       # pkt 6
   list_filter = ('question_text', 'is_open_question')
   search_fields = ('pub_date', 'question_text')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
   list_display = ('get_question', 'answer_text', 'number_of_appearances')       # pkt 6
   list_filter = ('question', 'answer_text')
   search_fields = ('question__question_text', 'answer_text')
   # raw_id_fields = ('question',)                                 # pkt 7

   @admin.display(description='Question text', )                 # pkt 6
   def get_question(self, obj):
       return obj.question.question_text
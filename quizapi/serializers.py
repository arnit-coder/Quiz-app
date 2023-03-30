from rest_framework import serializers
from quiz.models import Question

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = Question
		fields = '__all__'
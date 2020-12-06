from rest_framework import serializers
from .models import Quiz, Category, Question, Progress
from django.conf import settings

class CategorySerializers(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = '__all__'

class QuizSerializers(serializers.ModelSerializer):
    categeory = serializers.CharField(source=Category.category)
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializers(serializers.ModelSerializer):

    categeory = serializers.CharField(source = Category.category)

    class Meta:
        model = Question
        fields = '__all__'

class ProgressSerializers(serializers.ModelSerializer):
    user = serializers.CharField(source=settings.AUTH_USER_MODEL)

    class Meta:
        model = Progress
        fields = '__all__'
from .serilalizers import CategorySerializers, QuizSerializers, QuestionSerializers, ProgressSerializers
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Quiz, Category, Question, Progress
from.utils import UttilGeneriViews


# List ------> GET
# Create ------> POST
# Upadte ------->POST
# Delete ------->POST

class QuestionView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, UttilGeneriViews):

    model = Question
    serializer_class = QuestionSerializers

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            serilalizer = QuestionSerializers(Question.objects.all(), many=True)
            response = serilalizer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            msg = "Only Admin can Post the data"
            response = {"result": msg}
            return (response)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            data = request.data
            if data.is_valid():
                que = Question()
                que.quiz = data['quiz']
                que.category = data['category']
                que.figure = data['figure']
                que.content = data['content']
                que.explanation = data['explanation']
                que.save()
                msg = "Success"
                response = {"Result ": msg}
                return Response(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            que = Question.objects.all().get('id')
            self.perform_destroy(que)
            response = {"msg": "deleted"}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail":e})
    def update(self, request, *args, **kwargs):
        question_program = Question.objects.all().get('id')
        serializer = QuizSerializers(question_program, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, UttilGeneriViews):
    model = Quiz
    serializer_class = QuestionSerializers

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            serilalizer = QuizSerializers(Quiz.objects.all(), many=True)
            response = serilalizer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            msg = "Only Admin can Post the data"
            response = {"result": msg}
            return (response)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            data = request.data
            if data.is_valid():
                que = Quiz()
                que.title = data['title']
                que.description = data['description']
                que.category = data['category']
                que.random_order = data['random_order']
                que.max_questions = data['max_questions']
                que.exam_paper = data['exam_paper']
                que.single_attempt = data['single_attempt']
                que.pass_mark = data['pass_mark']
                que.success_text = data['success_text']
                que.fail_text = data['fail_text']
                que.draft = data['draft']
                que.save()
                msg = "Success"
                response = {"Result ": msg}
                return Response(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            que = Quiz.objects.all().get('id')
            self.perform_destroy(que)
            response = {"msg": "deleted"}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail":e})

    def update(self, request, *args, **kwargs):
        quiz_program = Quiz.objects.all().get('id')
        serializer = QuizSerializers(quiz_program, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CateogeoryView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
               UttilGeneriViews):
    model = Category
    serializer_class = CategorySerializers

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            serilalizer = CategorySerializers(Category.objects.all(), many=True)
            response = serilalizer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            msg = "Only Admin can Post the data"
            response = {"result": msg}
            return (response)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            data = request.data
            if data.is_valid():
                que = Category()
                que.category = data['category']
                que.save()
                msg = "Success"
                response = {"Result ": msg}
                return Response(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            que = Category.objects.all().get('id')
            self.perform_destroy(que)
            response = {"msg": "deleted"}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": e})

    def update(self, request, *args, **kwargs):
        quiz_program = Category.objects.all().get('id')
        serializer = CategorySerializers(quiz_program, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgressView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
               UttilGeneriViews):
    model = Progress
    serializer_class = ProgressSerializers

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            serilalizer = ProgressSerializers(Progress.objects.all(), many=True)
            response = serilalizer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            msg = "Only Admin can Post the data"
            response = {"result": msg}
            return (response)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            data = request.data
            if data.is_valid():
                que = Progress()
                que.user = data['user']
                que.score = data['score']
                que.correct_answer = data['correct_answer']
                que.wrong_answer = data['wrong_answer']
                que.save()
                msg = "Success"
                response = {"Result ": msg}
                return Response(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            que = Progress.objects.all().get('id')
            self.perform_destroy(que)
            response = {"msg": "deleted"}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": e})

    def update(self, request, *args, **kwargs):
        quiz_program = Progress.objects.all().get('id')
        serializer = ProgressSerializers(quiz_program, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










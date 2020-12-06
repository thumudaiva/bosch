"""boschproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from quizapp.api_view import QuestionView, CateogeoryView, QuizView, ProgressView
from django.conf.urls import url
from quizapp.views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user
from django.urls import path
router = routers.DefaultRouter()
router.register(r'question', views.QuestionView,
router.register(r'cateogeory', views.CateogeoryView,
router.register(r'quiz', views.QuizView,
router.register(r'progress', views.ProgressView

urlpatterns = [url(regex=r'^$', view=index, name='index'),
               url(regex=r'^login/$', view=login_user, name='login'),
               url(regex=r'^logout/$', view=logout_user, name='logout'),
               url(regex=r'^quizzes/$',
               view=QuizListView.as_view(),
                 name='quiz_index'),

                url(regex=r'^category/$',
                    view=CategoriesListView.as_view(),
                    name='quiz_category_list_all'),
                url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                     view=ViewQuizListByCategory.as_view(),
                    name='quiz_category_list_matching'),
                 url(regex=r'^progress/$',
                    view=QuizUserProgressView.as_view(),
                    name='quiz_progress'),

                 url(regex=r'^marking/$',
                    view=QuizMarkingList.as_view(),
                    name='quiz_marking'),

                url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                     view=QuizMarkingDetail.as_view(),
                    name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                url(regex=r'^(?P<slug>[\w-]+)/$',
                    view=QuizDetailView.as_view(),
                    name='quiz_start_page'),

                url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                    view=QuizTake.as_view(),
                    name='quiz_question'),
               url(r'^api/', include(router.urls)),
]




from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('add/', views.AddProjects.as_view()),
    path('', views.ViewProjects.as_view()),
    path('proapi/', views.ProjectsApi.as_view()),
    path('project/<id>', views.Project.as_view(), name='project'),
    path('donate/', views.Donate.as_view(), name='donate'),
    path('comment/', views.Comment.as_view(), name='comment'),
    path('reply/', views.Reply.as_view(), name='reply'),
    path('cancel/', views.Cancel.as_view(), name='cancel'),
    path('report/<typ>/<id>', views.Report.as_view(), name='report'),
]

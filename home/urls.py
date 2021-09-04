from home.models import Content
from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView

urlpatterns = [
    path('',views.index, name="index" ),
    path('addsubject',views.addSubject, name="addsubject" ),
    path('update/<int:id>',views.updateSubject, name="updatesubject"),
    path('delete/<int:id>',views.deleteSubject, name="deletesubject"),
    path('addclass',views.addClass, name="addclass" ),
    path('deleteclass/<int:id>',views.deleteClass, name="deleteclass"),
    path('updateclass/<int:id>',views.updateClass, name="updateclass"),
    path('assignsubject',views.assignSubject, name="assignsubject"),
    path('updateassignsubject/<int:id>',views.updateAssignSubject, name="updateassignsubject"),
    path('deleteassignsubject/<int:id>',views.deleteAssignSubject, name="deleteassignsubject"),
    path('addchapter',views.addChapter, name="addchapter" ),
    path('updatechapter/<int:id>',views.updateChapter, name="updatechapter"),
    path('deletechapter/<int:id>',views.deleteChapter, name="deletechapter"),
    path('uploadcontent',views.uploadContent, name="uploadcontent"),
    path('ajax/load-subject/', views.load_subject, name='ajax_load_subject'),
    path('ajax/load-chapter/', views.load_chapter, name='ajax_load_chapter'),
    path('selectclass',views.selectClass, name="selectclass" ),
    path('viewcontent/<int:id>',views.viewContent, name="viewcontent"),
    path('archive/',ArchiveIndexView.as_view(model=Content, date_field="added"),name="content_archive"),
    path('demo',views.demo, name="demo" ),
    path('viewcontent',views.viewContent, name="viewcontent" ),
    path('relatedcontent/<str:std>/<str:sub>/<str:ch>',views.relatedContent, name="relatedcontent" ),
    path('deletecontent/<int:id>',views.deleteContent, name="deletecontent"),
    path('updatecontent/<int:id>',views.updateContent, name="updatecontent"),
]


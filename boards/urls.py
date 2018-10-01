from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='boards-home'),
    path('<int:pk>/', views.TopicListView.as_view(), name='boards-topics'),
    path('<int:pk>/new/',views.new_topic, name='boards-new_topic'),
    path('<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='boards-topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='boards-reply_topic'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',views.PostUpdateView.as_view(), name='boards-edit_post'),
    ]

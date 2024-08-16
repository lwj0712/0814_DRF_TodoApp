from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoCompleteView, TodoDeleteView, TodoOverdueView, TodoUpdateView, TodoCommentCreateView, TodoCompletionStatsView, TodoCloneView, todo_list, todo_complete, todo_delete

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todos/<int:pk>/complete/', TodoCompleteView.as_view(), name='todo-complete'),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('todos/overdue/', TodoOverdueView.as_view(), name='todo-overdue'),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todos/<int:pk>/comments/', TodoCommentCreateView.as_view(), name='todo-comment-create'),
    path('todos/completion-stats/', TodoCompletionStatsView.as_view(), name='todo-completion-stats'),
    path('todos/<int:pk>/clone/', TodoCloneView.as_view(), name='todo-clone'),
    path('', todo_list, name='todo-list'),
    path('complete/<int:pk>/', todo_complete, name='todo-complete'),
    path('delete/<int:pk>/', todo_delete, name='todo-delete'),
]
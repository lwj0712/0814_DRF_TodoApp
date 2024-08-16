from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Todo, TodoStatusHistory, TodoComment
from .serializers import TodoSerializer, TodoCommentSerializer


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        previous_status = instance.completed
        updated_instance = serializer.save()
        TodoStatusHistory.objects.create(
            todo=updated_instance,
            previous_status=previous_status,
            new_status=updated_instance.completed
        )

class TodoCompleteView(APIView):
    def post(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.is_completed = True
            todo.save()
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    lookup_field = 'pk'


class TodoOverdueView(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(due_date__lt=timezone.now(), completed=False)

    def patch(self, request, *args, **kwargs):
        overdue_todos = self.get_queryset()
        overdue_todos.update(completed=True)
        return Response({"message": "Overdue todos marked as completed."}, status=status.HTTP_200_OK)
    
class TodoCommentCreateView(generics.CreateAPIView):
    queryset = TodoComment.objects.all()
    serializer_class = TodoCommentSerializer


class TodoCompletionStatsView(APIView):

    def get(self, request, *args, **kwargs):
        total = Todo.objects.count()
        completed = Todo.objects.filter(completed=True).count()
        completion_rate = (completed / total) * 100 if total > 0 else 0
        return Response({"completion_rate": completion_rate})
    
class TodoCloneView(APIView):

    def post(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(pk=pk)
        todo.pk = None  # 새로운 객체로 복사
        todo.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
    

def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
        return redirect('todo-list')

    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('todo-list')

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo-list')

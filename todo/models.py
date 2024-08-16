from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)  # 우선순위 필드 추가
    due_date = models.DateTimeField(null=True, blank=True)  # 마감일 필드 추가

    def __str__(self):
        return self.title
    

class TodoStatusHistory(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    previous_status = models.BooleanField()
    new_status = models.BooleanField()
    changed_at = models.DateTimeField(auto_now_add=True)


class TodoComment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

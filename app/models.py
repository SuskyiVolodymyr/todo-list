from django.db import models


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created"]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

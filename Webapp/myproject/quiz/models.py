from django.db import models

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_content = models.TextField()
    question_opt1 = models.CharField(max_length=200)
    question_opt2 = models.CharField(max_length=200)
    question_opt3 = models.CharField(max_length=200)
    question_opt4 = models.CharField(max_length=200)
    question_ans = models.CharField(max_length=200)
    question_solution = models.TextField(default="solution")

    def __str__(self):

        return self.question_title


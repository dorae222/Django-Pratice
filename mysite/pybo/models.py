from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField() # 제한없음
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # Question을 지우면, 해당 답변들도 함께 지운다.
    # 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
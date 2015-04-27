from django.db import models

# Create your models here.
class Expression(models.Model):
    expression_string = models.CharField('Expression',max_length=1000)
    expression_result = models.CharField('Result',max_length=1000)
    expression_time = models.DateTimeField('Date of Evaluation',auto_now_add=True)

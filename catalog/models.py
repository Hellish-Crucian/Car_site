from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
	mark = models.ForeignKey('dictionary.Mark', on_delete=models.CASCADE)
    model = models.ForeignKey('dictionary.Model', on_delete=models.CASCADE)
    state = models.ForeignKey('dictionary.State', on_delete=models.CASCADE)
    color = models.ForeignKey('dictionary.Color', on_delete=models.CASCADE)
    prise = models.IntegerField()
    year = models.IntegerField()
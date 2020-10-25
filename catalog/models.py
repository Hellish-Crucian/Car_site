from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
	model = models.ForeignKey('dictionary.Mark', on_delete=models.CASCADE)
    model = models.ForeignKey('dictionary.Model', on_delete=models.CASCADE)
    model = models.ForeignKey('dictionary.State', on_delete=models.CASCADE)
    model = models.ForeignKey('dictionary.Color', on_delete=models.CASCADE)
    prise = models.IntegerField()
    year = models.IntegerField()
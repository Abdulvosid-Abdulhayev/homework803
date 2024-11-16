from django.db import models

class Klass(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi

class Mehmonxona(models.Model):
    nomi = models.CharField(max_length=100)
    yulduzlar_soni = models.IntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi

class Travel(models.Model):
    nomi = models.CharField(max_length=100)
    izoh = models.TextField()
    muddati = models.IntegerField()  # kunlarda
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name="travels")
    mehmonxona = models.ForeignKey(Mehmonxona, on_delete=models.CASCADE, related_name="travels")

    def __str__(self):
        return self.nomi

from django.db import models

# Create your models here.
class abs_immigration(models.Model):
    migration_type = models.CharField(max_length=100,choices=[("Arriving","Arriving"),("Departing","Departing"),("Net Migration","Net Migration")],default="Arrival")
    gender = models.CharField(max_length=100,choices=[("Males","Males"),("Females","Females"),("Persons","Persons")],default="Persons")
    region= models.CharField(max_length=100,choices=[("Australia","Australia"),("Victoria","Victoria")],default="Australia")
    pub_date= models.DateTimeField(auto_now_add=True)




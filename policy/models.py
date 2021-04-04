from django.db import models
#from utils.constants import fuel_choices, gender_choices, region_choices 

# Create your models here.

class Customer(models.Model):
    Customer_id=models.IntegerField(primary_key=True)
    Customer_Gender=models.CharField(max_length=50)
    Customer_Income_group=models.CharField(max_length=50)
    Customer_Region=models.CharField(max_length=50)
    Customer_Marital_status=models.BooleanField()

class Policy_tbl(models.Model):
    Policy_id=models.IntegerField(primary_key=True)
    Date_of_Purchase=models.DateField(blank=True)
    Customer_id=models.ForeignKey(Customer,on_delete=models.PROTECT, related_name='customer')
    Fuel=models.CharField(max_length=50)
    Vehicle_Segment=models.CharField(max_length=1)
    Premium=models.IntegerField()
    
class Policy_feature(models.Model):
    Policy_id=models.ForeignKey(Policy_tbl, on_delete=models.CASCADE, related_name='policy_id')
    bodily_injury_liability=models.BooleanField()
    personal_injury_protection=models.BooleanField()
    property_damage_liability=models.BooleanField()
    collision=models.BooleanField()
    comprehensive=models.BooleanField()
    
    




from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Landlord(models.Model) :
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)   
    management_company = models.CharField(max_length=30)

    def __str__(self) :
        return (self.management_company)
    
    class Meta:
        db_table = "ratemylandlord_landlord"

class Property(models.Model) :
    landlord = models.ForeignKey(Landlord, on_delete = models.DO_NOTHING)
    property_name = models.CharField(max_length = 50)
    street_address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 10)

    def __str__(self) :
        return (self.property_name)
    
    class Meta:
        db_table = "ratemylandlord_property"

class User(models.Model) :
    nickname = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    def __str__(self) :
        return (self.nickname)

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)

    def save(self) :
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(User, self).save()

    class Meta:
        db_table = "ratemylandlord_user"

class Rating(models.Model) :
    rating = models.IntegerField(default = 0, validators = [MaxValueValidator(10), MinValueValidator(0)])
    poor_management = models.BooleanField(default=False)
    hidden_fees = models.BooleanField(default=False)
    lack_of_privacy = models.BooleanField(default=False)
    unreturned_funds = models.BooleanField(default=False)
    property_condition = models.CharField(max_length = 50)
    utilities = models.BooleanField(default=False)
    safety_concerns = models.BooleanField(default=False)
    appliance_issues = models.BooleanField(default=False)
    mold = models.BooleanField(default=False)
    pests = models.BooleanField(default=False)
    neighborhood_problems = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    bad_contracts = models.BooleanField(default=False)
    change_in_rent = models.BooleanField(default=False)
    other_notes = models.CharField(max_length = 5000)
    date_submitted = models.DateField(default = datetime.today, blank = True)
    properties = models.ForeignKey(Property, on_delete = models.DO_NOTHING)
    users =  models.ForeignKey(User, on_delete = models.DO_NOTHING)


    
    def __str__(self) :
        return '%s %s' % (self.properties.property_name, self.rating)

    class Meta:
        db_table = "ratemylandlord_rating"

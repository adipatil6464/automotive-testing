from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class userRegister(models.Model):
    DROPBOX_CHOICES = (
        ('option1', 'India'),
        ('option2', 'US'),
        ('option3', 'Autralia'),
        # Add more options as needed
    )
    company_name = models.CharField(max_length=100, primary_key=True)
    CIN_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=7)
    country = models.CharField(max_length=50, choices=DROPBOX_CHOICES)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.company_name
    

class ApplicationRegistration(models.Model):
    DROPBOX_CHOICES_VEHICLE_OR_PART = (
        ('option1', 'vehicle'),
        ('option2', 'part'),
    )

    DROPBOX_CHOICES_VEHICLE_TYPE = (
        ('option1', 'four wheeler'),
        ('option2', 'two wheeler'),
    )

    DROPBOX_CHOICES_CERTIFICATE_TYPE = (
        ('option1', 'TAC'),
        ('option2', 'CoP'),
        ('option3', 'Coc'),
        ('option4', 'R&D Certificate'),
        # Add more options as needed
    )

    company_name = models.ForeignKey(userRegister, on_delete = models.CASCADE)
    model_name = models.CharField(max_length=50, primary_key=True)
    certificate_type = models.CharField(max_length=50, choices=DROPBOX_CHOICES_CERTIFICATE_TYPE)
    vehicle_or_part = models.CharField(max_length=50, choices=DROPBOX_CHOICES_VEHICLE_OR_PART)
    vehicle_type = models.CharField(max_length=50, choices = DROPBOX_CHOICES_VEHICLE_TYPE)
    description = models.TextField()
    specification = models.FileField(upload_to="document")
    design = models.FileField(upload_to="design")
    blueprint = models.FileField(upload_to="blueprint")

    def __str__(self) -> str:
        return str(self.company_name)+" "+str(self.model_name)



class FourWheelerParameter(models.Model):

    DROPBOX_CHOICES_ENGINE = (
        ('option1', 'Inline engine'),
        ('option2', 'Cylinder configuration'),
        ('option3', 'V engine'),
        ('option4', 'Diesel engine'),
        ('option5', 'Four'),
        ('option6', 'OPOC engine'),
        ('option7', 'Petrol engine'),
        ('option8', 'Single cylinder engine'),
        ('option9', 'Six-cylinder'),
        ('option10', 'Stroke engine'),
        ('option11', 'V8'),
        ('option12', 'Compression ignition'),
        ('option13', 'Electric motor'),
        ('option14', 'Straight-five engine'),
        ('option15', 'Gas engine'),
    )

    DROPBOX_CHOICES_CAR_TYPE = (
        ('option1', 'Sedan'),
        ('option2', 'SUV'),
        ('option3', 'Pickup'),
        ('option4', 'Wagon'),
        ('option5', 'Minivan'),
        ('option6', 'Sports car'),
        ('option7', 'Utility vehicle'),
        ('option8', 'MPV'),
        ('option9', 'MUV'),
        ('option10', 'Van'),
        ('option11', 'Electric'),
        ('option12', 'Hybrid'),
    )


    DROPBOX_CHOICES_INFOTAINMENT_SYSTEM = (
        ('option1', 'manual'),
        ('option2', 'touch'),
    )
    
    DROPBOX_CHOICES_ADAS_SYSTEM = (
        ('option1', 'YES'),
        ('option2', 'NO'),
    )

    company_name = models.ForeignKey(userRegister,on_delete=models.CASCADE)
    model_name = models.ForeignKey(ApplicationRegistration,on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=200)
    # built_type = models.CharField(max_length=50)
    passenger = models.IntegerField()
    engine_type = models.CharField(max_length=50, choices = DROPBOX_CHOICES_ENGINE)
    fuel_consumpsion = models.CharField(max_length=50)
    alternate_fuel_consumption = models.CharField(max_length=50, default="NA")
    airbags_count = models.IntegerField(default=0)
    infotainment_system = models.CharField(max_length=50, choices = DROPBOX_CHOICES_INFOTAINMENT_SYSTEM)
    gears_type = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices = DROPBOX_CHOICES_CAR_TYPE)
    ADAS = models.CharField(max_length=50, choices = DROPBOX_CHOICES_ADAS_SYSTEM)
    Safety_Ratings = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    environment_safety = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    Performance_Ratings = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    Fuel_Efficiency_Ratings = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )


    def __str__(self) -> str:
        return str(self.model_name)
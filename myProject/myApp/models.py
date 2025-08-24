# ORM
#MODELS ARE USED FOR DATABSE LIK THIS MODEL WILL HANDLE 
# AND TALKE TO THE SQLITE OR ANY DB THAT WE USE WE IN DJANGO INTERACT WITH MODEL AND NOT DIRECTLY WITH THE DATABSE
# THIS MODEL IS CALLED THE ORM LAYER OBJECT RELATION MODEL

#evertime you change something in model make migrations for that means run [python manage.py makemigrations myApp] and after that [python manage.py migrate]

from django.db import models
from django.utils import timezone # to give the date the correct time like set default as now time and date

# default models given to us by django
from django.contrib.auth.models import User

# create your own model(for DB)
class myUsers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UserImages/') #you need to tell that where means in which folder you wanna upload or store your images to And pillow is needed to upload the image and also you need to tell the settings.py that yes we have images so it needs to know as well
    date_added = models.DateTimeField(max_length=500, default=timezone.now)
    # create enum for gender choices because we want only 3 genders not any choice that user can select
    GENDER = [
        ('M', 'MALE'), #tuples because we want it to be immutable
        ('F', 'FEMALE'),
        ('GAYYY', 'GAY')
    ]
    gender = models.CharField(max_length=5, choices=GENDER)
    discription = models.CharField(default='')
    
    
    
    # i want that if any user gets added to my app their name show as name the entered rather than myUserObject1 so for that
    def __str__(self):
        return self.name
    
#one to many relation - 1 user->many reviews
class myUserReview(models.Model):
    user = models.ForeignKey(myUsers, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.name


'''
    SIMILARLY YOU CAN MAKE OTHER RELATIONS LIKE
    ONT TO MANY -> use foreign key [ user = models.ForeignKey(myUsers, on_delete=models.CASCADE, related_name='reviews') ]
    MANY TO MANY [ [chai  = models.ManyToManyField(chaivariety, on_delete = cascade, related_name = 'stores')] ONE PRODUCT CAN BE IN MULTIPLE STORES AND MULTIPLE STORES CAN HAVE THE SAME PRODUCT]
    ONE TO ONE [chai  = models.OneToOneField(chaivariety, on_delete = cascade, related_name = 'certifiacte')]
    ETC
'''


from django.db import models
from datetime import datetime

# Create your models here.


class Data(models.Model):
    end_year = models.CharField(max_length=100, blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.CharField(max_length=100, blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField()
    published = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True)
    pestle = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField(blank=True, null=True)

    def convert_added_date(self, date_string):
        # Convert date string to a valid datetime object
        try:
            date_object = datetime.strptime(date_string, "%B, %d %Y %H:%M:%S")
            return date_object
        except ValueError:
            return None

    


    def convert_intensity(self, intensity):
        # Convert intensity to a valid integer or None
        if intensity =='':
            try:
                intensity=int(intensity)
                
            except :
                intensity=None
                
            

    def save(self, *args, **kwargs):
        # Convert the added date before saving
        if self.added and isinstance(self.added, str):
            self.added = self.convert_added_date(self.added)

        # Convert intensity before saving
        if self.intensity and isinstance(self.intensity, str):
            self.intensity = self.convert_intensity(self.intensity)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    




    

    


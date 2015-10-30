from django.db import models

class Currency(models.Model):
    identifier = models.CharField(max_length=3) #USD,EUR etc.
    long_name = models.CharField(max_length=50) #United States Dollar etc.
    date_added = models.DateTimeField() #When added to database
    def __str__(self):
        return self.identifier + " " + self.long_name

from datetime import datetime,timezone

class Rates(models.Model):
    id_1 = models.ForeignKey(Currency) #A link to a Currency object
    id_2 = models.CharField(max_length=3) #Identifier for currency 2
    rate = models.FloatField(default=1.0) #exchange rate
    last_update_time = models.DateTimeField() #last time updated

    def __str__(self):
        return self.id_1.identifier + " " + self.id_2 + " " + str(self.rate)

    def time_since_last_update(self):
        now = datetime.now(timezone.utc)
        try:
            time_diff = now - self.last_update_time
        except:
            return "None"
        return time_diff
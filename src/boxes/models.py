from django.db import models
from django.db.models import Avg,Max
from assets.models import Box
from partners.models import BusinessPartner


class BoxReservationRequest(models.Model):
    ForBusinessPartner = models.ForeignKey(BusinessPartner,on_delete=models.DO_NOTHING)
    RESERVATION_STATUS = (
        ('ReservationMade','Reservation made'),
       ('Agreed','Agreed'),
       ('Rejected','Rejected'),
       ('Requested','Requested'),   
       ('Searching','Searching')
    )
    ResevationStatus = models.CharField(max_length=20,choices=RESERVATION_STATUS,default='Requested')
    comments = models.TextField()
    StartDay = models.DateField()
    EndDay   = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

class BoxConfirmedReservation(models.Model):
    ForBox = models.ForeignKey(Box,on_delete=models.CASCADE)
    ForBusinessPartner = models.ForeignKey(BusinessPartner,on_delete=models.CASCADE)
    StartDay = models.DateField()
    EndDay   = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

class BoxOccupied(models.Model):
    ForBox = models.ForeignKey(Box,on_delete=models.CASCADE)
    ForBusinessPartner = models.ForeignKey(BusinessPartner,on_delete=models.CASCADE)
    Comments = models.TextField()
    StartDay = models.DateField()
    EndDay   = models.DateField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)    

class BoxOccupiedLog(models.Model):
    ForBoxOccupied = models.ForeignKey(BoxOccupied,on_delete=models.CASCADE)
    LogSequence = models.IntegerField()

    def save(self):
        data = BoxOccupiedLog.objects.filter(ForBoxOccupied__id = self.ForBoxOccupied.id)
        if (data.count() == 0):
            self.LogSequence = 1
        else:
            self.LogSequence = data.aggregate(models.Max('LogSequence'))['LogSequence__max'] + 1

        return super().save()







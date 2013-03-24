from django.db import models
import datetime

MOVIE = 'MOV'
AUDIO = 'AUD'
PICTURE = 'PIC'
TEXT = 'TXT'
SIMPLEEMOTION_JSON = 'SEJ'
ASSET_TYPE = (
    (MOVIE, 'movie'),
    (AUDIO, 'audio'),
    (PICTURE, 'picture'),
    (TEXT, 'text'),
    (SIMPLEEMOTION_JSON, 'simpleemotion')
)


# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patientslikeme_id = models.IntegerField()
    description = models.TextField()
    youtube_channel = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.first_name + self.last_name

class Session(models.Model):
    player = models.ForeignKey('Player')
    score = models.IntegerField()
    audio_url = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    started_at = models.DateTimeField(auto_now_add = True)
    ended_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return unicode(self.started_at)

class SessionData(models.Model):
    session = models.ForeignKey('Session')
    data_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=3,
                                choices=ASSET_TYPE,
                                default=TEXT)
    url = models.CharField(max_length=6000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.data_name

class Asset(models.Model):
    player = models.ForeignKey('Player')
    data_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=3,
                                choices=ASSET_TYPE,
                                default=TEXT)
    url = models.FileField(upload_to="assets/parents/")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.data_name

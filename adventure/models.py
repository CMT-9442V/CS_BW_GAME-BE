from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

# class Room(models.Model):
#     title = models.CharField(max_length=50, default="DEFAULT TITLE")
#     description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
#     n_to = models.IntegerField(default=0)
#     s_to = models.IntegerField(default=0)
#     e_to = models.IntegerField(default=0)
#     w_to = models.IntegerField(default=0)
#     def connectRooms(self, destinationRoom, direction):
#         destinationRoomID = destinationRoom.id
#         try:
#             destinationRoom = Room.objects.get(id=destinationRoomID)
#         except Room.DoesNotExist:
#             print("That room does not exist")
#         else:
#             if direction == "n":
#                 self.n_to = destinationRoomID
#             elif direction == "s":
#                 self.s_to = destinationRoomID
#             elif direction == "e":
#                 self.e_to = destinationRoomID
#             elif direction == "w":
#                 self.w_to = destinationRoomID
#             else:
#                 print("Invalid direction")
#                 return
#             self.save()
#     def playerNames(self, currentPlayerID):
#         return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
#     def playerUUIDs(self, currentPlayerID):
#         return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
class Channel(models.Model):
    channel = models.IntegerField(default=0)
    background = models.CharField(max_length=500, default="")
    geometry = models.CharField(max_length=500, default="")
    glitchtype = models.CharField(max_length=500, default="")
    audio = models.CharField(max_length=500, default="")
    text = models.CharField(max_length=500, default="")
    up_to = models.IntegerField(default=0)
    down_to = models.IntegerField(default=0)
    def connectChannels(self, destinationChannel, direction):
        destinationChannelID = destinationChannel.id
        try:
            destinationChannel = Channel.objects.get(id=destinationChannelID)
        except Channel.DoesNotExist:
            print("That channel does not exist")
        else:
            if direction == "u":
                self.n_to = destinationChannelID
            elif direction == "d":
                self.s_to = destinationChannelID
            else:
                print("Invalid direction")
                return
            self.save()
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentChannel=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentChannel=self.id) if p.id != int(currentPlayerID)]
    # def __repr__(self):
    #     return f"Channel:{self.channel}, Background:{self.background}, geometry:{self.geometry}, glitchtype:{self.glitchtype}, audio:{self.audio}"
    def __str__(self):
        return f"Channel:{self.channel}, Background:{self.background}, geometry:{self.geometry}, glitchtype:{self.glitchtype}, audio:{self.audio}"

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentChannel = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
        if self.currentChannel== 0:
            self.currentChannel = Channel.objects.first().id
            self.save()
    def channel(self):
        try:
            return Channel.objects.get(id=self.currentChannel)
        except Channel.DoesNotExist:
            self.initialize()
            return self.channel()

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()


# STUFF

import random

Channel.objects.all().delete()
backgrounds=['https://i.imgur.com/WU4JRaN.jpg', 'https://i.imgur.com/fF1TtUz.jpg', 'https://i.imgur.com/u59oC5P.png']
audio=['tv_static', 'glitched_tones', 'radio_static']
glitchtype=['static', 'DeafultTextGlitch', 'ComicBook']
geometry=[100,200,300]
text=['23423', 'please', '--.-333.999----9v', '55.7558', '37.6173']
def channel_maker(num_channels):
    tot_channels=0
    prev_channel=0
    curr_channel=0
    next_channel=1
    while tot_channels > num_channels:
        if next_channel <= num_channels:
            new_channel=Channel(channel=curr_channel, background=random.choice(backgrounds), audio=random.choice(audio), glitchtype=random.choice(glitchtype), geometry=random.choice(geometry), text=random.choice(text), up_to=next_channel, down_to=prev_channel)
            new_channel.save()
        else:
            next_channel=curr_channel
            new_channel=Channel(channel=curr_channel, background=random.choice(backgrounds), audio=random.choice(audio), glitchtype=random.choice(glitchtype), geometry=random.choice(geometry), text=random.choice(text), up_to=next_channel, down_to=prev_channel)
            new_channel.save()
    prev_channel=curr_channel
    curr_channel += 1
    next_channel += 1
channel_maker(10)



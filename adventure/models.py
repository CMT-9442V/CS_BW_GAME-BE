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






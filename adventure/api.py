from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    # user = request.user
    # player = user.player
    # player_id = player.id
    # uuid = player.uuid
    # room = player.room()
    # players = room.playerNames(player_id)
    return JsonResponse({'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    channel_id = str(request.data["id"])
    direction = str(request.data["direction"])
    curChannel = Channel.objects.get(id=channel_id)
    nextChannelID = None
    if direction == "u"
        nextChannelID = curChannel.up_to
    elif direction == "d":
        nextChannelID = curChannel.down_to
    if nextChannelID is not None and nextChannelID > 0:
        nextChannel = Channel.objects.get(id=nextChannelID)
        return JsonResponse({'id': nextChannel.id, 'channel':nextChannel.channel, 'background': nextChannel.background, 'audio': nextChannel.audio, 'geometry': nextChannel.geometry, 'glitchtype': nextChannel.glitchtype, 'text':nextChannel.text, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'id': nextChannel.id, 'channel':nextChannel.channel, 'background': nextChannel.background, 'audio': nextChannel.audio, 'geometry': nextChannel.geometry, 'glitchtype': nextChannel.glitchtype, 'text':nextChannel.text, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

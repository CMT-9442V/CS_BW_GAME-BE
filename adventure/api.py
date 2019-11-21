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
    channel=Channel.objects.get(channel=00)
    return JsonResponse({'id': channel.id, 'channel':channel.channel, 'background': channel.background, 'audio': channel.audio, 'geometry': channel.geometry, 'glitchtype': channel.glitchtype, 'text':channel.text, 'error_msg':""}, safe=True)

# @api_view(["GET"])
# def channels(request):
#     channels = Channel.objects.all()
#     result = {
#       "channel": 0,
#       "background": "someUrl",
#       "geometry": "squarr",
#       "glitchtype": "banana",
#       "audio": "banananana",
#       "text": "anabana",
#       "up_to": 2,
#       "down_to": 0
#     }
#     # for channel in channels:
#     #     result.append(chann)
#     # json.loads(result)
#     return JsonResponse(result, safe=True)
# ==========================================
@api_view(["GET"])
def channels(request):
    channels = Channel.objects.all()
    # result = ''
    # for channel in channels:
    #     result += channel.__repr__() + ', '
    # return JsonResponse({'channels': result}, safe=True)
    results = [obj.to_dict() for obj in channels]
    results.sort(key=lambda obj: obj["channel"])
    # print("------------------STUFF------------------", results)
    jsdata = json.dumps({"results": results})
    return JsonResponse(results, safe=False)
# ==========================================

# @csrf_exempt
@api_view(["POST"])
def move(request):
    channel_id = str(request.data["id"])
    direction = str(request.data["direction"])
    curChannel = Channel.objects.get(id=channel_id)
    nextChannelID = None
    if direction == "u":
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

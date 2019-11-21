
from adventure.models import Channel
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
            new_channel=Channel(channel=cur_channel, background=random.choice(backgrounds), audio=random.choice(audio), glitchtype=random.choice(glitchtype), geometry=random.choice(geometry), text=random.choice(text), up_to=next_channel, down_to=prev_channel)
            new_channel.save()
        else:
            next_channel=cur_channel
            new_channel=Channel(channel=cur_channel, background=random.choice(backgrounds), audio=random.choice(audio), glitchtype=random.choice(glitchtype), geometry=random.choice(geometry), text=random.choice(text), up_to=next_channel, down_to=prev_channel)
            new_channel.save()
    prev_channel=cur_channel
    cur_channel += 1
    next_channel +=1
channel_maker(10)
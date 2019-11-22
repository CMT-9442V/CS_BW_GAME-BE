from adventure.models import Channel
import random

backgrounds=['https://i.imgur.com/WU4JRaN.jpg', 'https://i.imgur.com/fF1TtUz.jpg', 'https://i.imgur.com/u59oC5P.png']
audio=['tv_static', 'glitched_tones', 'radio_static']
glitchtype=['static', 'DeafultTextGlitch', 'ComicBook']
geometry=[100,200,300]
text=['23423', 'please', '--.-333.999----9v', '55.7558', '37.6173']
name=['cat', 'tina']


def channel_maker(num_channels): 
    tot_channels=0
    prev_channel=0
    curr_channel=0
    next_channel=1
    print("beginning")
    while tot_channels < num_channels:
        if next_channel <= num_channels:
            print("hi")
            new_channel=Channel(channel=curr_channel, 
            name=random.choice(name), next_channel=next_channel, prev_channel=prev_channel)
            new_channel.save()
            prev_channel=curr_channel
            curr_channel += 1
            next_channel += 1
            tot_channels += 1
        else:
            next_channel=curr_channel
            new_channel=Channel(channel=curr_channel,
            name=random.choice(name),
            next_channel=curr_channel, prev_channel=prev_channel)
            new_channel.save()
            prev_channel=curr_channel
            curr_channel += 1
            next_channel += 1
            tot_channels += 1

channel_maker(100)

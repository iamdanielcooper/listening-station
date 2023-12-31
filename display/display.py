#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
from spotipy_helpers.spotipy_helpers import *
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd3in52
import time
from PIL import Image,ImageDraw,ImageFont

def display_album_data(albums):
    
    epd = epd3in52.EPD()
    epd.init()
    epd.display_NUM(epd.WHITE)
    epd.lut_GC()
    epd.refresh()

    epd.send_command(0x50)
    epd.send_data(0x17)
    time.sleep(2)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)

    for index, album in enumerate(albums):
        height = epd.width / 5
        draw.text((10, height * index), display_formatted_album_information(index, album), font = font24, fill = 0, align = "center")
        draw.line((0, height * index, epd.height, height * index), fill = 0)



    epd.display(epd.getbuffer(Himage))
    epd.lut_GC()
    epd.refresh()
    time.sleep(2)

def display_loading():
    
    epd = epd3in52.EPD()
    epd.init()
    epd.display_NUM(epd.WHITE)
    epd.lut_GC()
    epd.refresh()

    epd.send_command(0x50)
    epd.send_data(0x17)
    time.sleep(2)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)

    draw.text((10, 10), get_loading_wording(), font = font24, fill = 0, align = "center")

    epd.display(epd.getbuffer(Himage))
    epd.lut_GC()
    epd.refresh()
    time.sleep(2)
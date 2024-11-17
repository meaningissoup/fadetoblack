import screen_brightness_control as sbc
from PIL import Image, ImageStat, ImageGrab
import numpy as np
import sched, time

def FindBrightLevel():
    x = ImageGrab.grab()

    levels = np.linspace(0, 255, num=10)

    image_stats = ImageStat.Stat(x)

    red_channel_mean, green_channel_mean, blue_channel_mean, a = image_stats.mean

    image_bright_value = np.sqrt(0.299 * (red_channel_mean ** 2)
                                + 0.587 * (green_channel_mean ** 2)
                                + 0.114 * (blue_channel_mean ** 2))

    image_bright_level = np.digitize(image_bright_value, levels, right=True)
    return image_bright_level

def DarkenScreen():
    x = sbc.get_brightness()
    sbc.set_brightness(0, force=True)
    time.sleep(1)
    sbc.fade_brightness(x, logarithmic=True)
    return

formerbright=FindBrightLevel()

def ScanScreen():
    global formerbright 
    while True:
        currentbright = FindBrightLevel()
        print(currentbright)
        if currentbright-formerbright >= 2:
            DarkenScreen()
        formerbright=currentbright

ScanScreen()
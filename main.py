import screen_brightness_control as sbc
import brightnessdetection as bd

print(bd.calculate_level())

def DarkenScreen():
    x = sbc.get_brightness()
    sbc.set_brightness(0)
    sbc.fade_brightness(x)
    return
from machine import Pin, Timer
from neopixel import NeoPixel

class EnhancedNeoPixel:
    PRESET_COLORS = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'yellow': (255, 255, 0),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'black': (0, 0, 0),
    }

    def __init__(self, pin):
        self.np = NeoPixel(Pin(pin), 1)
        self.clear()
        self.timer = Timer(0)
        self.blinking = False

    def set_color(self, color, brightness=1.0):
        if isinstance(color, str):
            color = self.PRESET_COLORS.get(color, (0, 0, 0))
        color = tuple(int(c * brightness) for c in color)
        self.np[0] = color
        self.np.write()

    def clear(self):
        self.set_color('black')

    def blink(self, color, times, interval, brightness=1.0):
        self.blink_count = 0
        self.blink_times = times
        self.blink_color = color
        self.blink_interval = interval
        self.blink_brightness = brightness
        self.blinking = True
        self.timer.init(period=int(interval * 1000), mode=Timer.PERIODIC, callback=self._blink_callback)

    def _blink_callback(self, timer):
        if self.blink_count >= self.blink_times * 2:
            self.timer.deinit()
            self.clear()
            self.blinking = False
            return

        if self.blink_count % 2 == 0:
            self.set_color(self.blink_color, self.blink_brightness)
        else:
            self.clear()

        self.blink_count += 1

    def start_blinking(self, color, interval, brightness=1.0):
        self.blink_color = color
        self.blink_interval = interval
        self.blink_brightness = brightness
        self.blinking = True
        self.timer.init(period=int(interval * 1000), mode=Timer.PERIODIC, callback=self._continuous_blink_callback)

    def stop_blinking(self):
        self.timer.deinit()
        self.clear()
        self.blinking = False

    def _continuous_blink_callback(self, timer):
        if self.blinking:
            if self.np[0] == (0, 0, 0):
                self.set_color(self.blink_color, self.blink_brightness)
            else:
                self.clear()

from kivy_garden.mapview import MapMarker
from kivy.animation import Animation

class GpsBlinker(MapMarker):
    def blink(self):
        """ animaation that changes the blink size opacity"""
        anim = Animation(outer_opacity=0, blink_size=50)
        """when animation is completed, reset it and repeat"""
        anim.bind(on_complete=self.reset)
        anim.start(self)
    
    def reset(self, *args):
        self.outer_opacity = 1
        self.blink_size = self.default_blink_size
        self.blink()
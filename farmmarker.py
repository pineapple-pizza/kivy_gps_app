# from kivy.garden.mapview import MapMarkerPopup
from kivy_garden.mapview import MapMarker
from locationpopupmenu import LocationPopupMenu

class FarmMarker(MapMarker):
    farm_data = []
    
    def on_release(self):
        source = ''
        #open location dialog
        menu = LocationPopupMenu(self.farm_data)
        menu.size_hint = [.8, .9]
        menu.open()
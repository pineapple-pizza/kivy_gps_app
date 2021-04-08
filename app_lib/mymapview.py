# from kivy.garden.mapview import MapView
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from .farmmarker import FarmMarker
from kivymd.uix.dialog import MDInputDialog

class MyMapView(MapView):
    getting_timer = None
    farm_names = []
    
    def start_getting_infos(self):
        """after 1sec get the markups in the field of view"""
        try:
            self.getting_timer.cancel()
        except:
            pass
        
        self.getting_timer = Clock.schedule_once(self.get_infos_in_fov, 1)
        
    def get_infos_in_fov(self, *args):
        """get reference to main app and the db cursor"""
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_stmt = "SELECT * FROM Dog_farms WHERE X > %s AND X < %s AND Y > %s AND Y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_stmt)
        
        list_farms = app.cursor.fetchall()
        print(list_farms)
        
        for item in list_farms:
            name = item[1]
            if name in self.farm_names:
                continue
            else:
                self.add_dog_farm(item)
            
    def add_dog_farm(self, item):
        lat, lon = item[8], item[7]
        print(lat, lon)
        source='assets/marker_teal.png'
        marker = FarmMarker(lat=lat, lon=lon)
        marker.source = source
        marker.farm_data = item
        self.add_widget(marker)
        
        name = item[1]
        self.farm_names.append(name)
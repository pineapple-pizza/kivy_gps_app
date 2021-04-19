from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from decouple import config
from kivy.utils import get_color_from_hex

class SearchPopupMenu(MDInputDialog):
    markup = True
    # teal_color = '#84CDCF'
    title = 'Via une adresse'
    # text_button_ok = '[color=%s]Chercher[/color]' %teal_color
    hint_text = "écris une adresse ici"
    text_button_ok="Chercher"
    
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback
        
    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
        
    def geocode_get_lat_lon(self, address):
        """connect to here api with coordinates (address)"""
        
        api_key = config('API_KEY')
        address = parse.quote(address)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey=%s&searchtext=%s"%(api_key, address)
        
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)
        
    def success(self, urlrequest, result):
        """get latitude and longitude"""
        
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)
        
    def failure(self, urlrequest, result):
        print('fail', result)
        
    def error(self, urlrequest, result):
        print('error', result)
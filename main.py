from kivymd.app import MDApp
from app_lib.mymapview import MyMapView
from app_lib.searchpopupmenu import SearchPopupMenu
import sqlite3

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    add_farm_popup = None
    icon = 'assets/dogs_icon_teal.png'
    markup = False
    
    def on_start(self):
        """initialize GPS"""

        """connect to database"""
        self.connection = sqlite3.connect("db_utils/dogs_database.db")
        self.cursor = self.connection.cursor()

        """init search pop menu"""
        self.search_menu = SearchPopupMenu()
        
        self.markup = True
        
if __name__ == '__main__':
    MainApp().run()
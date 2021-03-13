from kivymd.app import MDApp
from mymapview import MyMapView
from searchpopupmenu import SearchPopMenu
import sqlite3

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    
    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect("db_utils/dogs_database.db")
        self.cursor = self.connection.cursor()

        #init search pop menu
        self.search_menu = SearchPopMenu()
        
if __name__ == '__main__':
    MainApp().run()
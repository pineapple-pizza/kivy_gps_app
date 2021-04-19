import unittest
from  unittest.mock import patch
from test_mock import GeocodeMock
from functools import partial
from kivy.clock import Clock
from kivy.app import App
import os.path as op
import sys
import time
import os
import sqlite3

main_path = op.dirname(op.dirname(op.abspath(__file__)))
sys.path.append(main_path)

from main import MainApp

class AppTestCase(unittest.TestCase):
        
    def pause(*args):
        time.sleep(0.000001)
        
        # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        db = "db_utils/dogs_database.db"
        
        if not db:
            self.skipTest("No database set")
        self.assertTrue(sqlite3.connect(db))
        
        from app_lib.mymapview import MyMapView
        
        conn = sqlite3.connect(db)
        
        c = conn.cursor()
        c.execute('SELECT * FROM Dog_farms')
        
        list_farms = c.fetchall()
        index_address = list_farms[0]
        self.assertEqual(index_address[6], '6 Ruelle du Bois des Vaux  02120  Lesquielles-Saint-Germain  France')
        
        fake_data = [{'latitude': '48.53333', 'longitude': '2.66667'}]

        with patch('test_mock.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_data

            obj = GeocodeMock()
            response = obj.get

            print(response.status_code)
            print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_data)
        
        app.stop() 
        
    def test_main(self):
        app = MainApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()
        
if __name__ == '__main__':
    unittest.main()
import unittest
import sys
import time
import os
import os.path as op
from functools import partial
from kivy.clock import Clock
from kivy.app import App

main_path = op.dirname(op.dirname(op.abspath(__file__)))
sys.path.append(main_path)

from mymapview import MyMapView

class AppTestCase(unittest.TestCase):
    def pause(*args):
        time.sleep(0.000001)
        
        # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)
        
        self.assertEqual('assets/marker.png', app.source)
        self.assertTrue(sqlite3.connect(db))
        
        app.stop() 
        
    def test_main(self):
        app = App.get_running_app()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        # app.run()
        
if __name__ == '__main__':
    unittest.main()
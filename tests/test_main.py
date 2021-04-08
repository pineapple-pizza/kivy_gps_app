import unittest
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

        # Do something
        # self.assertEqual('assets/dogs_icon.png', app.icon)
        db = "db_utils/dogs_database.db"
        
        if not db:
            self.skipTest("No database set")
        self.assertTrue(sqlite3.connect(db))
        
        # conn = sqlite3.connect(db)
        
        # c = conn.cursor()
        # c.execute('SELECT * FROM Dog_farms')
        
        # # # self.assertTrue()
        
        # list_farms = c.fetchall()
        # self.assertTrue(c.fetchall())
        # self.assertEqual(list_farms)
        # print(list_farms)

        # Comment out if you are editing the test, it'll leave the
        # Window opened.
        app.stop() 
        
    def test_main(self):
        app = MainApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()
        
if __name__ == '__main__':
    unittest.main()
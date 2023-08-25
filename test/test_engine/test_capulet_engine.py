import unittest

from car_module.car_parts.engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_service_true(self):
        curr_mil = 300001
        last_service_mil = 0
        engine = CapuletEngine(curr_mil,last_service_mil)
        self.assertTrue(engine.needs_service())
    
    def test_service_false(self):
        curr_mil = 30000
        last_serivce_mil = 0
        engine = CapuletEngine(curr_mil,last_serivce_mil)
        self.assertFalse(engine.needs_service())
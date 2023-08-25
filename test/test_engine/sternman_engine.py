import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_service_true(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_service_false(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())
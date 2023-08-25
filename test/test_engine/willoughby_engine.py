import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_service_true(self):
        current_mil = 60001
        last_service_mil = 0
        engine = WilloughbyEngine(current_mil, last_service_mil)
        self.assertTrue(engine.needs_service())

    def test_service_false(self):
        current_mil = 60000
        last_service_mil = 0
        engine = WilloughbyEngine(current_mil, last_service_mil)
        self.assertFalse(engine.needs_service())
import unittest
from datetime import date

from car_module.car_parts.battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_service_true(self):
        curr_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(curr_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        curr_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(curr_date, last_service_date)
        self.assertFalse(battery.needs_service())
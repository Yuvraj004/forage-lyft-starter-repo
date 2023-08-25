import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_service_true(self):
        curr_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(curr_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        curr_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(curr_date, last_service_date)
        self.assertFalse(battery.needs_service())
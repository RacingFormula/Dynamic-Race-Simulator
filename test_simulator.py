import unittest
from src.simulator import RaceSimulator
from src.track_model import Track, Segment
from src.vehicle_dynamics import Vehicle

class TestRaceSimulator(unittest.TestCase):
    def test_single_lap(self):
        segments = [Segment(100, 30, 0), Segment(200, 50, 5)]
        track = Track(segments)
        vehicle = Vehicle(mass=1200, power=150000, drag_coefficient=0.3, tyre_grip=1.2)

        simulator = RaceSimulator(track, vehicle)
        lap_time = simulator.run_lap()

        self.assertGreater(lap_time, 0)
        self.assertEqual(len(simulator.lap_data), len(segments))

    def test_multiple_laps(self):
        segments = [Segment(150, 40, 2)] * 5
        track = Track(segments)
        vehicle = Vehicle(mass=1000, power=200000, drag_coefficient=0.25, tyre_grip=1.3)

        simulator = RaceSimulator(track, vehicle)
        race_results = simulator.run_race(3)

        self.assertEqual(len(race_results), 3)
        self.assertTrue(all(time > 0 for time in race_results))

if __name__ == '__main__':
    unittest.main()
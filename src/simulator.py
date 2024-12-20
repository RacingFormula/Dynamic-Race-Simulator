import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from track_model import Track, Segment
from vehicle_dynamics import Vehicle


class RaceSimulator:
    def __init__(self, track, vehicle):
        self.track = track
        self.vehicle = vehicle
        self.time = 0.0
        self.lap_data = []

    def run_lap(self):
        self.vehicle.reset()
        lap_time = 0.0
        for segment in self.track.segments:
            segment_time = self.vehicle.simulate_segment(segment)
            lap_time += segment_time
            self.lap_data.append({
                'segment': segment,
                'time': segment_time,
                'speed': self.vehicle.current_speed
            })
        self.time += lap_time
        return lap_time

    def run_race(self, num_laps):
        race_results = []
        for lap in range(num_laps):
            lap_time = self.run_lap()
            race_results.append(lap_time)
        return race_results

if __name__ == "__main__":
    from src.track_model import Segment, Track
    from src.vehicle_dynamics import Vehicle

    segments = [
        Segment(100, 50, 0),
        Segment(200, 40, 5),
        Segment(300, 30, -2)
    ]
    track = Track(segments)
    vehicle = Vehicle(mass=1200, power=150000, drag_coefficient=0.3, tyre_grip=1.2)

    simulator = RaceSimulator(track, vehicle)

    print("Running single lap simulation...")
    lap_time = simulator.run_lap()
    print(f"Lap time: {lap_time:.2f} seconds")

    print("Running race simulation for 3 laps...")
    race_times = simulator.run_race(3)
    for i, time in enumerate(race_times, start=1):
        print(f"Lap {i}: {time:.2f} seconds")
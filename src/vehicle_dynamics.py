import math

class Vehicle:
    def __init__(self, mass, power, drag_coefficient, tyre_grip):
        self.mass = mass  # in kg
        self.power = power  # in watts
        self.drag_coefficient = drag_coefficient
        self.tyre_grip = tyre_grip
        self.current_speed = 0.0

    def reset(self):
        self.current_speed = 0.0

    def simulate_segment(self, segment):
        # Simplistic model for acceleration and braking
        max_speed = math.sqrt(self.tyre_grip * segment.curvature * self.mass)
        acceleration = self.power / self.mass

        time_to_reach_max_speed = (max_speed - self.current_speed) / acceleration
        time_on_segment = min(segment.length / max_speed, time_to_reach_max_speed)

        # Update speed
        self.current_speed = min(max_speed, self.current_speed + acceleration * time_on_segment)

        return time_on_segment
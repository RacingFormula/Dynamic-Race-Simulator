class Segment:
    def __init__(self, length, curvature, elevation_change):
        self.length = length  # in meters
        self.curvature = curvature  # radius of curvature in meters
        self.elevation_change = elevation_change  # in meters

class Track:
    def __init__(self, segments):
        self.segments = segments

    @staticmethod
    def create_circular_track(num_segments, radius, segment_length):
        segments = []
        for _ in range(num_segments):
            segments.append(Segment(segment_length, radius, 0))
        return Track(segments)
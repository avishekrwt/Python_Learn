class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_mercury(self):
        self.time = 31557600 * 0.2408467
        return round(self.seconds/self.time,2)

    def on_venus(self):
        time = 31557600 * 0.61519726
        return round(self.seconds/time,2)

    def on_earth(self):
        time = 31557600 * 1
        return round(self.seconds/time,2)

    def on_mars(self):
        time = 31557600 * 1.8808158
        return round(self.seconds/time,2)

    def on_jupiter(self):
        time = 31557600 * 11.862615
        return round(self.seconds/time,2)

    def on_saturn(self):
        time = 31557600 *29.447498
        return round(self.seconds/time,2)

    def on_uranus(self):
        time = 31557600 * 84.016846
        return round(self.seconds/time,2)

    def on_neptune(self):
        time = 31557600 * 164.79132
        return round(self.seconds/time,2)
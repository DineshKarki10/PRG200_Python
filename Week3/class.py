class Area:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
area1 = Area(5)
print(area1.calculate_area())
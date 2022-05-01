from city import City

class Map:
    def __init__(self, list):
        self.cities = []
        for city in list:
            self.cities.append(City(city[0],city[1],city[2]))

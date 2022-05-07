from city import City

class Map:
    def __init__(self, list):
        self.cities = []
        for city in list:
            #self.cities.append(City(city[0],city[1],city[2]))
            self.cities.append(City(name=city[0],color=city[1],pos=city[2]))

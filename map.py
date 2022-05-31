from city import City

class Map:
    def __init__(self, list):
        self.cities = []
        for city in list:
            #self.cities.append(City(city[0],city[1],city[2]))
            self.cities.append(City(name=city[0],color=city[1],pos=city[2]))
    
    def draw(self, screen):
        for city in self.cities:
            city.draw(screen)
    
    def get_city_by_name(self,name):
        for c in self.cities:
            if c.name == name:
                return c

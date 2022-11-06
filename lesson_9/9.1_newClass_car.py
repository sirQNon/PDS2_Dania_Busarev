class properties_car:
    def __init__(self, brand,color, engine_volume):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume

    def go_ahead(self):
        return f" {self.brand} go ahead in {self.color} with power {self.engine_volume}"

    def rides_back(self):
        return f" {self.brand} rides_back {self.color} with power {self.engine_volume}"


class car_2(properties_car):
     def turn_left(self):
         return f" turned left {self.brand} in {self.color} color "

     def turn_right(self):
         return f" turned right {self.brand} in {self.color} color "


impreza = properties_car( "Subaru", "Blue", 250)
goahead_impreza = impreza.go_ahead()
print(goahead_impreza)

fiesta = car_2("Ford", "Green", 187)
turn_left_fiesta = fiesta.turn_left()
print(turn_left_fiesta)
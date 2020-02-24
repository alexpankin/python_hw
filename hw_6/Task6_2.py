class Road:
    _lenght_ = 200
    _width_ = 200
    mass_on_one_sm = 100
    size = 10
    full_mass = _lenght_ * _width_ * mass_on_one_sm * size

    def mass_on_road(self):
        print("Full Mass objekt")


r = Road()
r.mass_on_road()
print(r.full_mass)

# full_mass = 0

# def mass_on_road(self, _lenght_, _width_, mass_on_one_sm, size):
#     print("Full Mass objekt")
#     self._lenght_ = _lenght_
#     self._width_ = _width_
#     self.mass_on_one_sm = mass_on_one_sm
#     self.size = size
#     Road.full_mass = _lenght_ * _width_ * mass_on_one_sm * size


# r = Road()
# r.mass_on_road(200, 200, 100, 10)
# print(r.full_mass)

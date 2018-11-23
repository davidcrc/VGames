
class Piedra:
    def __init__(self):
        self.x = 250
        self.y = 10
        self.dx = 0
        self.dy = 1
        self.AnchoP = 36
        self.AltoP = 31
        
    def get_x(self): return self.x

    def get_y(self): return self.y

    def get_dx(self): return self.dx

    def get_dy(self): return self.dy

    def get_AnchoP(self): return self.AnchoP

    def get_AltoP(self): return self.AltoP

    def set_x(self, xf): self.x = xf

    def set_y(self, yf): self.y = yf

    def set_dx(self, dxf): self.dx = dxf

    def set_dy(self, dyf): self.dy = dyf

    def temporizador(self, tiempo):
        return

if __name__ == '__main__':
    piedra = Piedra()
    print piedra.get_AltoP()
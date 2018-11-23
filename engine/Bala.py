class Bala:
    def __init__(self):
        self.x = 150
        self.y = 150
        self.dx = 0
        self.dy = -1
        self.AnchoB = 12
        self.AltoB = 16
        
    def get_x(self): return self.x

    def get_y(self): return self.y

    def get_dx(self): return self.dx

    def get_dy(self): return self.dy

    def get_AnchoB(self): return self.AnchoB

    def get_AltoB(self): return self.AltoB

    def set_x(self, xf): self.x = xf

    def set_y(self, yf): self.y = yf

    def set_dx(self, dxf): self.dx = dxf

    def set_dy(self, dyf): self.dy = dyf

if __name__ == '__main__':
    bala = Bala()
    print bala.get_AnchoB()
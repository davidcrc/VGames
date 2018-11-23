class Nave:
    def __init__(self):
        self.x = 150
        self.y = 150
        self.dir = 1
        self.dx = 0
        self.dy = -1
        self.AnchoN = 59
        self.AltoN = 83
        self.balas = 0
        self.pBala = []
        self.vidas = 10
        self.puntos = 0

    def get_x(self): return self.x

    def get_y(self): return self.y

    def get_dx(self): return self.dx

    def get_dy(self): return self.dy

    def get_dir(self): return self.dir

    def get_AnchoN(self): return self.AnchoN

    def get_AltoN(self): return self.AltoN

    def get_bala(self): return self.balas

    def get_vida(self): return self.vidas

    def get_punto(self): return self.puntos

    def set_x(self, xf): self.x = xf

    def set_y(self, yf): self.y = yf

    def set_dir(self, dirf): self.dir = dirf

    def set_bala(self, nb): self.balas = nb

    def set_vida(self, nv): self.vidas = nv

    def set_punto(self, np): self.puntos = np

    def moverN(self):
        return


if __name__ == '__main__':
    navePrueba = Nave()
    print navePrueba.get_AltoN()
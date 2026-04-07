import pygame
import random
import math


class mian:
    def __init__(self):
        self.viewportsize = 1000
        self.grade_perlin = 100

        self.grade = []
        self.tela = None
        self.tela = pygame.display.set_mode((self.viewportsize,self.viewportsize))


        self.lista_vector = [
            (-1, -1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (0, 1),
            (0, -1),
            (1, 0),
            (-1,0)
        ]
        self.perlin_noise()
        self.pygame()


    def pygame(self):
        pygame.init
        self.rodando = True
        while self.rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
            


            pygame.display.update()
        pygame.quit()

    def perlin_noise(self):
        self.grade = []
        for x in range(self.grade_perlin):
            self.lista = []
            for y in range(self.grade_perlin):
                self.lista.append(self.lista_vector[random.randint(0, len(self.lista_vector)-1)])
            self.grade.append(self.lista)
        for x in range(self.viewportsize):
            for y in range(self.viewportsize):
                self.value = self.noise((x,y))
                self.pintar(x,y,self.value)

            
    def noise(self, x : tuple):
        self.x , self.y = x
        self.rx = int(self.x / self.grade_perlin)
        self.ry = int(self.y / self.grade_perlin)
        self.list_adjacent = []
        self.lista_nadave = [
            (0,0),
            (1,0),
            (0,1),
            (1,1)
        ]
        for i in self.lista_nadave:
            self.list_adjacent.append((self.rx + i[0], self.ry + i[1]))

        self.lista_vectorptocanto = []

        self.gx = (self.x % self.grade_perlin) / self.grade_perlin
        self.gy = (self.y % self.grade_perlin) / self.grade_perlin

        self.lista_vectorptocanto = [
            (self.gx, self.gy),
            (self.gx - 1, self.gy),
            (self.gx, self.gy - 1),
            (self.gx - 1, self.gy - 1)
        ]

        self.lista_produtorescalar = []
        self.lista_vectoradjacent = []

        for i in self.list_adjacent:
            self.lista_vectoradjacent.append(self.grade[i[0]][i[1]])

        for i in range(4):
            self.lista_produtorescalar.append(self.lista_vectorptocanto[i][0] * self.lista_vectoradjacent[i][0] + self.lista_vectorptocanto[i][1] * self.lista_vectoradjacent[i][1])
        
        self.sx = self.fade(self.gx)
        self.sy = self.fade(self.gy)
        self.ix0 = self.lerp(self.lista_produtorescalar[0], self.lista_produtorescalar[1], self.sx)
        self.ix1 = self.lerp(self.lista_produtorescalar[2], self.lista_produtorescalar[3], self.sx)

        return self.lerp(self.ix0, self.ix1, self.sy)

        


        
    
    

    def fade(self, x):
        return 6*x**5 - 15*x**4 + 10*x**3
    
    def lerp(self, a,b, x):
        return a + x*(b-a)
    
    def pintar(self,x,y,value):

        cor = int((value + 1) * 127)*0.78

        cor = max(0, min(255, cor))

        self.tela.set_at((x, y), (cor, cor, cor))
    
    

mian()
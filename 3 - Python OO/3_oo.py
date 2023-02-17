class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'A máquina {self.nome} já esta filmando.')
            return

        print(f'{self.nome} está filmando.')
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'Não está filmando')
            return
        
        print(f'{self.nome} parando de filmar')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f'Não é possível fotogragar filmando!')
            return

        print(f'{self.nome} está fotografando.')
    
    
        


c1 = Camera('Sony')
c2 = Camera('Cannon')


c1.filmar()
c1.filmar()
print(c1.filmando)
print(c2.filmando)


class Ibehavior():
    def ataque(self):
        pass
    def movimiento(self):
        pass
    def vida(self):
        pass
    def escudo(self):
        pass

class Unidad_soldado(Ibehavior):
    def ataque(self):
        print("Ataque soldado: 50 dmg")

    def movimiento(self):
        print("Movimiento soldado: 50 speed")

    def vida(self):
        print("Vida soldado: 55 hp")

    def escudo(self):
        print("Escudo soldado: 25 armor")

class Unidad_arquero(Ibehavior):
    def ataque(self):
        print("At arquero: 30 dmg")

    def movimiento(self):
        print("Movimiento arquero: 75 speed")

    def vida(self):
        print("Vida arquero: 35 hp")

    def escudo(self):
        print("Escudo arquero: 17 armor")

class Unidad_caballeros(Ibehavior):
    def ataque(self):
        print("Ataque caballeros: 90 dmg")

    def movimiento(self):
        print("Movimiento caballeros: 20 speed")

    def vida(self):
        print("Vida caballero: 110 hp")

    def escudo(self):
        print("Escudo caballero: 55 armor")

class Tropa():
    def __init__(self, tipo_unidad: Ibehavior):
        self.tipo = tipo_unidad

    def performUnit(self):
        self.tipo.ataque()
        self.tipo.movimiento()
        self.tipo.vida()
        self.tipo.escudo()
    
class Soldado(Tropa):
    def __init__(self):
        super().__init__(Unidad_soldado())
    
class Aquero(Tropa):
    def __init__(self):
        super().__init__(Unidad_arquero())

class Caballero(Tropa):
    def __init__(self):
        super().__init__(Unidad_caballeros())


if __name__ == "__main__":
    warrior = Soldado()
    warrior.performUnit()






class frutas:
    def __init__(self, color, sabor, tamaño, peso):
        self.color=color
        self.sabor=sabor
        self.tamaño=tamaño
        self.peso=peso
        
manzana= frutas("roja","dulce","mediana","180g")
naranja=frutas("anaranjado","acido","grande","250g")

print(type(manzana))
print(type(naranja))

print(manzana.color, manzana.sabor, manzana.tamaño, manzana.peso)
print(naranja.color, naranja.sabor, naranja.tamaño, naranja.peso)

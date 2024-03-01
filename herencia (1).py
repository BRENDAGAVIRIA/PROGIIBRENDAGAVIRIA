class lote:
    def __init__(self,largo,ancho,constructora):
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora
        
    def calculararea(self):
        print (self.largo * self.ancho)
            
    def printconstructora(self):
        print(self.constructora)
        
class casa(lote):
    
    def __init__(self,largo,ancho,constructora,propietario,telefono):
        super().__init__(largo,ancho,constructora)
            
        self.propietario = propietario
        self.telefono = telefono

    def printpropietario(self):
        
        print(self.propietario)

    def printtelefono(self):
        print(self.telefono)


x = casa(500,1200,"Tecnar","Brenda Gaviria",3202892496)
x.calculararea()
x.printconstructora() 
x.printpropietario()
x.printtelefono()
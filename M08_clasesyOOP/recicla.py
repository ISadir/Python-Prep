class Recicla:
    def __init__(self, lista):
        self.lista=lista

    def verific_primo(self):
        for i in self.lista:
            if self.__verific_primo(i):
                print(i, "es primo")
            else:
                print(i, "no es primo")
    
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print("el valor {} {} en {} es {}".format(i, origen, destino, self.__conversion_grados(i, origen, destino)))
            
    def factorial(self):
        for i in self.lista:
            print("el factorial de {} es {}". format(i, self.__factorial(i)))
    
    def maximo(self):
        c,v =self.__maximo(self.lista)
        print("el numero que mas se repite ({} veces) es {}".format(v,c))
    

    def __verific_primo(self, numero):
        primo = True
        for i in range(1, numero):
            if numero != i and numero%i ==0 and i != 1:
                primo = False
                break
        return primo
    
    def __maximo (self, lista):
        cant={}
        for a in lista:
            if a in cant:
                cant[a]+=1
            else:
                cant[a]=1
        for c, v in cant.items():
            if v == max(cant.values()):
                return c, v
            
    def __conversion_grados(self, valor, origen, destino):
        if origen == "celsius":
            if destino == "kelvin":
                return valor+273.15
            elif destino == "farenheit":
                return ((valor)*9/5)+32
            else: 
                return valor 
        if origen == "kelvin":
            if destino =="celsius":
                return valor-273.15
            elif destino == "farenheit":
                return ((valor-273.15)*9/5)+32
            else: 
                return valor 
        if origen == "farenheit":
            if destino == "kelvin":
                return ((valor-32)*5/9)+273.15
            elif destino == "celsius":
                return ((valor-32)*5/9)
            else: 
                return valor 

    def __factorial(self, num):
        if type(num)!=int or num<=0:
            print("valor incorrecto", num)
        elif num == 1:
            return num
        else:
            num = num*self.__factorial(num-1)
            return num
   
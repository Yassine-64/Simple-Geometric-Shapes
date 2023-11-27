class Rectangle:
    count = 0
    def __init__(self, longueur = 0, largeur = 0):
        self.longueur = longueur
        self.largeur = largeur
        Rectangle.count += 1



    def get_longueur(self):
        return self.longueur
    
    def set_longueur(self, value):
        self.longueur = value

    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, value):
        self.largeur = value 

    
    def Equals(self,other):
        if self.longueur == other.longueur and self.largeur == other.largeur:
            return True
        else:
            return False
    
    def Perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
        return (self.longueur * self.largeur)
    
    def Tostring(self):
        return f"rectangle : longueur={self.longueur} largueur ={self.largeur} "
    

class Paralle (Rectangle):
    n_para = 0

    def __init__(self, longueur=0 , largeur=0, hauteur=0 ):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        Paralle.n_para+= 1

    def get_hauteur(self):
        return self.hauteur
    
    def set_hauteur(self, value):
        self.hauteur = value



    def surface(self):
        return 2*(self.longueur * self.largeur) + (self.longueur * self.hauteur)*2 +(self.largeur * self.hauteur)*2
    
    def volume(self):
        return  self.longueur * self.largeur * self.hauteur
      
    def Tostring(self):
        return f"Parallélepipède : longueur={self.longueur} largueur ={self.largeur} hauteur={self.hauteur} "
    



Rect1 = Rectangle(1,5)
Rect2 = Rectangle(2,7)
Rect3 = Rectangle(2,8)

print(f"le nombre d'objet est : {Rectangle.count}")
print(Rect1.Perimetre())
print(Rect1.Tostring())
print(Rect1.surface())


pr1 = Paralle(1,5,8)
pr2 = Paralle(1,4,6)
pr3 = Paralle(1,7,9)
print(f"le nombre d'objet est : {Paralle.n_para}")

print(pr1.Tostring())
print(pr2.surface())
print(pr3.volume())




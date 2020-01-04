#from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
from matplotlib.image import imsave


class Parametre:
    def __init__(self, filename):
        self.filename = filename

    def getDocumentElement(self):
        dom1 = xml.dom.minidom.parse(self.filename)  # ouvert .xml
        return dom1.documentElement

    def getLongDeToile(self):
        return int(self.getDocumentElement().getAttribute("longDeToile"))

    def gethautDeToile(self):
        return  int(self.getDocumentElement().getAttribute("hautDeToile"))

    def getnbrDeFourmis(self):
        return  int(self.getDocumentElement().getAttribute("nbrDeFourmis"))

    def getnbrIteration(self):
        return  int(self.getDocumentElement().getAttribute("nbrIteration"))

    def getfourmi(self):
        return self.getDocumentElement().getElementsByTagName("fourmis")


class Fourmis :
    def __init__(self, positionInit, direction, typeMouvment, prob, probDeSuivre, couleurDeposee, couleurSuivi):
        self.positionActuelle = positionInit
        self.direction = direction
        self.voisins=[]
        self.positionVoisins=[]
        self.prob=prob
        self.typeMouvment=typeMouvment
        self.probDeSuivre=probDeSuivre
        self.couleurDeposee=couleurDeposee
        self.couleurSuivi=couleurSuivi

    #sous fonction de getVoisins
    def videVoisin(self):
        self.voisins.clear()
        self.positionVoisins.clear()

    #sous fonction de getVoisins
    def getSousVoisins(self,gauche, direction, droit):
        dircGauche=self.positionActuelle+dic_direction[gauche]
        self.positionVoisins.append(dircGauche)
        self.voisins.append(pic[dircGauche[0],dircGauche[1]])

        dirc=self.positionActuelle+dic_direction[direction]
        self.positionVoisins.append(dirc)
        self.voisins.append(pic[dirc[0],dirc[1]])

        dircDroit = self.positionActuelle + dic_direction[droit]
        self.positionVoisins.append(dircDroit)
        self.voisins.append(pic[dircDroit[0], dircDroit[1]])

    def getVoisins(self):
        self.videVoisin()
        if self.direction == 1:  # ↑
            self.getSousVoisins(7,1,3)
        elif self.direction == 5:  # ↓
            self.getSousVoisins(3,5,7)
        elif self.direction == 7:  # ←
            self.getSousVoisins(5,7,1)
        elif self.direction == 3:  # →
            self.getSousVoisins(1,3,5)
        elif self.direction == 8:  # ↖
            self.getSousVoisins(7,8,1)
        elif self.direction == 2:  # ↗
            self.getSousVoisins(1,2,3)
        elif self.direction == 6:  # ↙
            self.getSousVoisins(5,6,7)
        elif self.direction == 4:  # ↘
            self.getSousVoisins(3,4,5)

    #sous fonction de determinerDirection
    def directionParType(self,typeProb): #  int: typeProb
        if typeProb==0:
            self.direction -= (self.typeMouvment + 1)
            if self.direction <= 0:
                self.direction = 8 - self.typeMouvment
        elif typeProb==1:
            pass
        elif typeProb==2:
            self.direction += (self.typeMouvment + 1)
            if self.direction > 8 - self.typeMouvment:
                self.direction = 1

    def determinerDirection(self):
        randomProb = np.random.random()
        if randomProb < self.prob[0]:  #gauche
            self.directionParType(0)
            return 0
        elif randomProb >= (self.prob[0] + self.prob[1]):   #tout droit
            self.directionParType(1)
            return 1
        else:  #droite
            self.directionParType(2)
            return 2


    def limiteFourmis(self):
        if self.positionActuelle[0] < 0:
            self.positionActuelle[0] = longDeToile - 1
        elif self.positionActuelle[0] >= longDeToile:
            self.positionActuelle[0] = 0
        if self.positionActuelle[1] < 0:
            self.positionActuelle[1] = longDeToile - 1
        elif self.positionActuelle[1] >= longDeToile:
            self.positionActuelle[1] = 0


    def calculLuminance(self,directionDetermi):
        for i, n in enumerate(self.voisins):
            # Lum(R,G, B) = 0,242 6 · R + 0,715 2 · V + 0,072 2 · B
            lum = 0.2426 * n[0] + 0.7152 * n[1] + 0.0722 * n[2]
            lumDeposee = 0.2426 * self.couleurSuivi[0] + 0.7152 * self.couleurSuivi[1] + 0.0722 * self.couleurSuivi[2]
            diffLum = np.absolute(lum - lumDeposee)  #Δ(S R, S V, S B, R, V, B) = |Lum(S R, S V, S B) − Lum(R, V, B)|.
            if diffLum < 40:

                pic[self.positionActuelle[0]][self.positionActuelle[1]] = self.couleurSuivi
                print("test")
                self.positionActuelle = self.positionVoisins[i]
                if i == 0:
                    self.direction -= (self.typeMouvment + 1)
                    if self.direction <= 0:
                        self.direction = 8 - self.typeMouvment
                if i == 2:
                    self.direction += (self.typeMouvment + 1)
                    if self.direction > 8 - self.typeMouvment:
                        self.direction = 1
            else:
                pic[self.positionActuelle[0]][self.positionActuelle[1]] = self.couleurDeposee
                self.positionActuelle = self.positionVoisins[directionDetermi]

    def lancer(self):
        self.getVoisins()
        directionDetermi = self.determinerDirection()
        probsuiv=np.random.random() #suivre selon la probabilité
        if probsuiv<self.probDeSuivre:
            self.calculLuminance(directionDetermi)
        else:
            pic[self.positionActuelle[0]][self.positionActuelle[1]] = self.couleurDeposee
            self.positionActuelle = self.positionVoisins[directionDetermi]
        self.limiteFourmis()


if __name__ == '__main__':

    # Clés dans l'ordre de la direction
    dic_direction = {
        1: [1, 0],  # ↑
        5: [-1, 0],  # ↓
        7: [0, -1],  # ←
        3: [0, 1],  # →
        8: [1, -1],  # ↖
        2: [1, 1],  # ↗
        6: [-1, -1],  # ↙
        4: [-1, 1]  # ↘
    }

    parametre = Parametre("parametre.xml")
    objFourmis = parametre.getfourmi()

    longDeToile=parametre.getLongDeToile()
    hautDeToile=parametre.gethautDeToile()
    pic = np.full((longDeToile + 1, hautDeToile + 1, 3), 255, dtype=np.uint8)

    fourmisList = []
    iteration=parametre.getnbrIteration()

    for f in objFourmis:
        positionInit = np.random.randint(1, longDeToile-1, 2)
        direction = np.random.randint(1, 9)

        couleurDeposee = f.getElementsByTagName('couleurDeposee')[0]
        couleurDeposee = couleurDeposee.childNodes[0].data.split(',')
        for i in range(0, len(couleurDeposee)):
            couleurDeposee[i] = int(couleurDeposee[i].strip())

        couleurSuivi = f.getElementsByTagName('couleurSuivi')[0]
        couleurSuivi = couleurSuivi.childNodes[0].data.split(',')
        for i in range(0, len(couleurSuivi)):
            couleurSuivi[i] = int(couleurSuivi[i].strip())

        prob = f.getElementsByTagName('prob')[0]
        prob = prob.childNodes[0].data.split(',')
        for i in range(0, len(prob)):
            prob[i] = float(prob[i].strip())

        typeMouvment = f.getElementsByTagName('type')[0]
        typeMouvment = int(typeMouvment.childNodes[0].data)

        probDeSuivre = f.getElementsByTagName('probDeSuivre')[0]
        probDeSuivre = float(probDeSuivre.childNodes[0].data)

        fourmi = Fourmis(positionInit, direction, typeMouvment, prob, probDeSuivre, couleurDeposee, couleurSuivi)
        fourmisList.append(fourmi)

    for i in range(1, iteration):
        for fourmi in fourmisList:
            fourmi.lancer()

    imsave('paintingants.png', pic)
    print("fini de peinture")


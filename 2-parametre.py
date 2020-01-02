from xml.dom.minidom import parse
import xml.dom.minidom

class parametre:
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
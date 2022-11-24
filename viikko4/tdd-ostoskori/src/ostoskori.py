"""Shopping basket."""
from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    """Stores items during shopping."""
    def __init__(self):
        self.sisalto = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        """Returns total amount of items in the basket."""
        total_amount = 0
        for item in self.sisalto.values():
            total_amount += item.lukumaara()
        return total_amount
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        """Returns total price of items in basket."""
        total_price = 0
        for item in self.sisalto.values():
            total_price += item.hinta()
        return total_price

    def lisaa_tuote(self, lisattava: Tuote):
        """Adds the item to basket."""
        if lisattava.nimi in self.sisalto:
            self.sisalto[lisattava.nimi].muuta_lukumaaraa(1)
        else:
            self.sisalto[lisattava.nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        """Returns all Ostos objects in the basket."""
        return list(self.sisalto.values())

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
        """Removes one item from the basket."""
        self.sisalto[poistettava.nimi].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        """Returns all Ostos objects in the basket."""
        return list(self.sisalto.values())

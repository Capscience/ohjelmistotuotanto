"""Moduuli IntJoukko-luokalle."""
KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    """Joukko, joka käsittelee kokonaislukuja."""
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError('Virheellinen kapasiteetti')
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError('Virheellinen kasvatuskoko')
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, tarkastettava: int) -> bool:
        """Kertoo kuuluuko luku joukkoon."""
        for luku in self.joukko:
            if luku == tarkastettava:
                return True
        return False

    def lisaa(self, lisattava: int) -> bool:
        """Lisää luku joukkoon, jos se ei vielä ole siellä."""
        if not self.kuuluu(lisattava):
            self.joukko[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm == len(self.joukko):
                self.kasvata()
            return True
        return False

    def kasvata(self) -> None:
        """Kasvata joukon tilaa kasvatuskoon verran."""
        vanha_joukko = self.joukko
        self.joukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(vanha_joukko, self.joukko)

    def poista(self, poistettava: int) -> bool:
        """Poista luku joukosta jos se sieltä löytyy."""
        poistettu = False
        for kohta, luku in enumerate(self.joukko):
            if luku == poistettava:
                self.joukko[kohta] = 0
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                poistettu = True
            if poistettu:  # Siirtää tyhjän kohdan joukon loppuun
                self.joukko[kohta] = self.joukko[kohta + 1]
                self.joukko[kohta + 1] = 0
                if kohta >= len(self.joukko) - 2:
                    # Välttää index out of range errorin
                    return True
        return False

    def mahtavuus(self) -> int:
        """Kertoo alkioiden määrän."""
        return self.alkioiden_lkm

    def to_int_list(self):
        """Hae joukon alkiot listana."""
        return [self.joukko[kohta] for kohta in range(self.alkioiden_lkm)]

    @staticmethod
    def kopioi_taulukko(kopioitava: list, kohde: list):
        """Kopioi taulun sisällön toiseen tauluun."""
        for kohta, alkio in enumerate(kopioitava):
            kohde[kohta] = alkio

    @staticmethod
    def yhdiste(joukko1, joukko2):
        """Luo joukkojen yhdisteen."""
        tulos = IntJoukko()
        for alkio in joukko1.to_int_list():
            tulos.lisaa(alkio)
        for alkio in joukko2.to_int_list():
            tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def leikkaus(joukko1, joukko2):
        """Luo joukkojen leikkauksen."""
        tulos = IntJoukko()
        for alkio in joukko1.to_int_list():
            if joukko2.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def erotus(joukko1, joukko2):
        """Luo annettujen joukkojen erotuksen."""
        tulos = IntJoukko()
        for alkio in joukko1.to_int_list():
            if not joukko2.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    def __str__(self):
        return str(self.to_int_list()).replace('[', '{').replace(']', '}')

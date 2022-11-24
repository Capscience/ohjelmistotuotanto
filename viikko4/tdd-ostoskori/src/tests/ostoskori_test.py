"""Tests for class Ostoskori."""
import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    """Test object for Ostoskori."""
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        """Tests initial values of basket."""
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        """Tests adding single item to basket."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        """Tests basket price after adding one item."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        """Tests adding 2 different item to basket."""
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        """Tests basket price after adding 2 different items."""
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        """Tests item count after adding 2 same items."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        """Tests basket price after adding 2 same items."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        """Tests length of return val of ostokset with 1 item."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        """Tests contents of return val of ostokset with 1 item."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_ostosta(self):
        """Test method ostokset with 2 different items."""
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

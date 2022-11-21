import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )

    def varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        if tuote_id == 2:
            return 5
        if tuote_id == 3:
            return 0

    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "leipä", 2)
        if tuote_id == 3:
            return Tuote(3, "peruna", 1)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )

    def test_tilisiirto_kutsutaan_oikein_2_tuotteella(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            7
        )

    def test_tilisiirto_oikein_2_samalla_tuotteella(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            10
        )

    def test_tilisiirto_oikein_kun_toista_tuotetta_ei_ole(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )

    def test_aloita_asiointi_tyhjentaa_ostoskorin(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )

    def test_uusi_viite_joka_tapahtumalle(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        varasto_mock = Mock()

        varasto_mock.saldo.side_effect = self.varasto_saldo
        varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(
            varasto_mock,
            pankki_mock,
            viitegeneraattori_mock
        )

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            2,
            "12345",
            "33333-44455",
            ANY
        )

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            3,
            "12345",
            "33333-44455",
            ANY
        )

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            4,
            "12345",
            "33333-44455",
            ANY
        )

    def test_tuotteen_poisto_toimii_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )

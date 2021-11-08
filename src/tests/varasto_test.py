import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_enemman_kuin_mita_varastossa(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(11)

        # testataan, että varastosta liikaa ottaminen ei laske saldoa negatiiviseksi
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def virheellinen_alustus(self, tilavuus, saldo):
        varasto2 = Varasto(tilavuus, saldo)
        self.assertGreaterEqual(varasto2.tilavuus, 0)
        self.assertGreaterEqual(varasto2.saldo, 0)
        self.assertGreaterEqual(varasto2.tilavuus, varasto2.saldo)

    def test_virheellinen_alustus(self):
        self.virheellinen_alustus(-1, -1)
        self.virheellinen_alustus(10,11)

    def test_virheellinen_otto(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_virheellinen_lisays(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_varaston_ylivuoto(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_tulostus(self):
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 1, vielä tilaa 9")

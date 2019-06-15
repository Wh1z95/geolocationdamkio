import unittest
from geolocdamkio.models import Localization


class LocalizationTestCase(unittest.TestCase):
    def setUp(self):
        self.bialystok = Localization.objects.create(name='Park', location=(), address='Branickiego 5', city='Bialystok')
        self.warsaw = Localization.objects.create(name='LotniskoModlin', location=(), address='Generała Wiktora Thommée 1a', city='Warsaw')



from geolocdamkio import models
import unittest
from selenium import webdriver


class LocalizationTestCase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()


        def testaddloc(self):
            self.driver.get("http://localhost:8000/add/")
            self.driver.find_element_by_id('name').send_keys("Magnus Carlsen")
            self.driver.find_element_by_id('localization').send_keys("Norwegia")
            self.driver.find_element_by_id('address').send_keys("sniezna 39")
            self.driver.find_element_by_id('city').send_keys("oslo")
            self.assertIn(("http://localhost:8000/", self.driver.current_url)


        def tearDown(self):
            self.driver.quit


if __name__ == '__main__':
    unittest.main()



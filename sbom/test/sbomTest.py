import unittest
import sbom.info as sbom

class AppTest(unittest.TestCase):


    def test_sbom_010_shouldReturnDeveloperName(self):
        myName = 'umphrda'
        self.assertIn(myName, sbom.info())
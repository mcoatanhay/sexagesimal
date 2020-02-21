#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_sexag.py
# Auteur: Marc COATANHAY

"""
    Tests pour la class Sexag.
"""

# Import des modules
from sexag import *
import unittest

# Définitions constantes et variables globales
a = Sexag(1, 1, 30, 36)

# Définitions fonctions et classes
class SexagTest(unittest.TestCase):
    def test_dec(self):
        self.assertEqual(todec(a), 1.51)

    def test_add(self):
        self.assertEqual(todec(a + a), 3.02)

    def test_lt(self):
        self.assertTrue(a < 1.511)

    def test_mul(self):
        self.assertEqual(todec(a*10), 15.1)

if (__name__ == "__main__"):
    unittest.main()
﻿#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: readme_sexag_compose.py
# Auteur: Marc COATANHAY

"""
    Module pour écrire un fichier d'aide du module.
"""

# Import des modules
import mes_modules_path
from repertoire import filerep
import sexag
import sys

# Définitions constantes et variables globales
filerep()
file = open('readme.txt', 'w')
sys.stdout = file
help(sexag)
file.close()
sys.stdout = sys.__stdout__

# Définitions fonctions et classes


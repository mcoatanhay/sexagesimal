#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: sexag.py
# Auteur: Marc COATANHAY

"""
    Module python pour effectuer les calculs au format sexagesimal.
"""

# Import des modules

# Définitions constantes et variables globales
signes = {-1: "-", 1: " "}

def todec(terme):
    """transforme un terme sexagésimal en décimal"""
    return (terme.u + terme.m/60 + terme.s/3600)*terme.sgn

def tosexag(terme):
    """transforme un terme au format sexagésimal"""
    if(terme != 0):
        sgn = int(terme/abs(terme))
        terme *= sgn
        u = int(terme)
        m = int((terme - u)*60)
        s = (terme - u - m/60)*3600
    else:
        sgn = 1
        u = 0
        m = 0
        s = 0
    return Sexag(sgn, u, m, s)

class Sexag:
    """ Class pour traiter les nombres sexagésimaux"""
    def __add__(self, terme2):
        """Additionne deux termes Sexag."""
        return tosexag(todec(self) + todec(terme2))

    def __format__(self,chaine):
        return self.__repr__()

    def __init__(self,sgn=1, u=0 , m=0 , s=0):
        """Initialise un élément Sexag."""
        self.sgn = sgn
        self.u = u
        self.m = m
        self.s = s

    def __lt__(self, terme):
        """Compare un élément Sexag avec un nombre"""
        return(todec(self) < terme)

    def __mul__(self, terme):
        """Multiplie un terme Sexag par un nombre."""
        return tosexag(todec(self)*terme)

    def __neg__(self):
        """Calcule l'opposé d'un terme Sexag."""
        self.sgn = - self.sgn
        return self

    def __repr__(self):
        """Affichage d'un terme Sexag."""
        chaine = "{}{}:{}:{}".format(signes[self.sgn], self.u, self.m, self.s)
        return chaine

    def __rmul__(self, terme2):
        """Multiplication à gauche d'un terme Sexag."""
        return self * terme2

    def __truediv__(self, terme2):
        """Division de deux termes Sexag."""
        return todec(self)/todec(terme2)






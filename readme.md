Help on module sexag:

NAME
    sexag - Module python pour effectuer les calculs au format sexagesimal.

CLASSES
    builtins.object
        Sexag
    
    class Sexag(builtins.object)
     |  Class pour traiter les nombres sexag�simaux
     |  
     |  Methods defined here:
     |  
     |  __add__(self, terme2)
     |      Additionne deux termes Sexag.
     |  
     |  __format__(self, chaine)
     |  
     |  __init__(self, sgn=1, u=0, m=0, s=0)
     |      Initialise un �l�ment Sexag.
     |  
     |  __lt__(self, terme)
     |      Compare un �l�ment Sexag avec un nombre
     |  
     |  __mul__(self, terme)
     |      Multiplie un terme Sexag par un nombre.
     |  
     |  __repr__(self)
     |      Affichage d'un terme Sexag.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    todec(terme)
        transforme un terme sexag�simal en d�cimal
    
    tosexag(terme)
        transforme un terme au format sexag�simal

DATA
    signes = {-1: '-', 1: '+'}

FILE
    c:\users\mc\mu_code\_mes_modules\sexagesimal\sexag.py



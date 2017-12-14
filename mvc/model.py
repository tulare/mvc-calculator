# -*- encoding: utf-8 -*-

# python 2/3 compatibility
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
    )

from mvc.observer import Observable
import math

def convertir(chaine) :
    try :
        nombre = float(chaine)
        if nombre.is_integer() :
            nombre = int(chaine)
    except ValueError :
        nombre = 0

    return nombre

class CalculatorModel(Observable) :

    result = 0
    operande = ""
    operateur = ''

    def __init__(self) :
        # super().__init__()
        # ensure python 2/3 compatibility
        super(CalculatorModel, self).__init__()
        
    def reset(self) :
        self.result = 0
        self.operande = ""
        self.operateur = ''
        self.notify('display', value=self.result)
        
    def setNombre(self, digit) :
        # entrée d'un nouveau nombre après calcul résultat
        if self.operateur == '=' :
            self.reset()
            
        try :
            float(self.operande + digit)
            self.operande += digit
        except :
            if self.operande + digit == "." :
                self.operande = "0."
                
        self.notify('display', value=self.operande)

    def setOperateur(self, operateur) :
        # calcul intermédiaire
        self.calcul()

        # nouvel operateur
        self.operateur = operateur

        # on réinitialise l'opérande si opérateur
        if operateur in ('+','-','*','/') :
            self.operande = ""

    def calcul(self) :

        # si pas d'operateur on renvoie l'operande
        if self.operateur == '' :
            self.result = convertir(self.operande)
                            
        elif self.operande != "" :

            if self.operateur == '+' :
                self.result += convertir(self.operande)
                
            if self.operateur == '-' :
                self.result -= convertir(self.operande)

            if self.operateur == '*' :
                self.result *= convertir(self.operande)
                
            if self.operateur == '/' :
                try :
                    self.result /= convertir(self.operande)
                except ZeroDivisionError :
                    self.result = math.nan

        self.operande = ""
        self.notify('display', value=self.result)

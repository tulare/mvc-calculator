# -*- encoding: utf-8 -*-

from mvc.model import CalculatorModel
from mvc.view import CalculatorView
from mvc.controller import CalculatorController

def main() :
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    controller.run()

if __name__ == '__main__' :
    main()

# -*- encoding: utf-8 -*-

from mvc.model import CalculatorModel
from mvc.view import CalculatorView
from mvc.controller import CalculatorController

model = CalculatorModel()
view = CalculatorView()
controller = CalculatorController(model, view)
controller.run()

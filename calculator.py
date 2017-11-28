# -*- encoding: utf-8 -*-

from mvc_model import CalculatorModel
from mvc_view import CalculatorView
from mvc_controller import CalculatorController

model = CalculatorModel()
view = CalculatorView()
controller = CalculatorController(model, view)
controller.run()

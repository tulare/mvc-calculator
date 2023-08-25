print('mvc\\__init__.py')

__all__ = [
    'CalculatorModel', 'CalculatorView', 'CalculatorController',
    'calculatorRun'
]

from .model import CalculatorModel
from .view import CalculatorView
from .controller import CalculatorController

def calculatorRun() :
    m = CalculatorModel()
    v = CalculatorView()
    c = CalculatorController(m,v)
    c.run()



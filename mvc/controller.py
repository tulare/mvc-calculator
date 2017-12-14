# -*- encoding: utf-8 -*-

# python 2/3 compatibility
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
    )

KEY_TRANS = str.maketrans({'<' : '', '>' : ''})

class CalculatorController(object) :
    """A controller that manages events between calculator view and model"""

    def __init__(self, model, view) :
        """Creates a controller that behaves as a medium between model and view"""
        
        self.model, self.view = model, view

        # configure calculator display to observe model
        self.model.add_observer(self.view.display)

        # connect calculator buttons to controller
        self.view.bind('<<CalculatorButton>>', self.key_action)

    def run(self) :
        """Starts the controller"""
        self.view.mainloop()

    def key_action(self, event) :
        """Controller action for each calculator key"""
        widget = event.widget
        print('key_action :', widget.tag)
        key = widget.tag.translate(KEY_TRANS)
        
        if key in "0123456789." :
            self.model.setNombre(key)

        if key in "+-*/=" :
            self.model.setOperateur(key)


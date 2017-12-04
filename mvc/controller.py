# -*- encoding: utf-8 -*-

# python 2/3 compatibility
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
    )

class CalculatorController(object) :
    """A controller that manages events between calculator view and model"""

    def __init__(self, model, view) :
        """Creates a controller that behaves as a medium between model and view"""
        
        self.model, self.view = model, view

        # register calculator display to observe model
        self.model.register(self.view.display)

        # connect calculator buttons to controller
        for button in self.view.buttons :
            button.config(command=self.bind(button))

    def run(self) :
        """Starts the controller"""
        self.view.mainloop()

    def bind(self, button) :
        """Callback for binding calculator buttons with controller actions"""
        return lambda : self.action(button['text'])

    def action(self, key) :
        """Controller action for each calculator key"""
        if key in "0123456789." :
            self.model.setNombre(key)

        if key in "+-*/=" :
            self.model.setOperateur(key)


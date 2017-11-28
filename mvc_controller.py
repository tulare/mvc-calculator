# -*- encoding: utf-8 -*-

class CalculatorController :

    def __init__(self, model, view) :
        self.model, self.view = model, view
        self.bind_model()
        self.bind_view()

    def run(self) :
        self.view.mainloop()

    def bind_model(self) :
        self.model.register(self.view.display)
    
    def bind_view(self) :
        for button in self.view.buttons :
            self.view.buttons[button].config(command=self.bind(button))
        
    def bind(self, button) :
        return lambda : self.action(button)

    def action(self, button) :
        if button in '0123456789.' :
            self.model.setNombre(button)

        if button in '+-*/=' :
            self.model.setOperateur(button)


# -*- encoding: utf-8 -*-

# python 2/3 compatibility
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
    )

from zope.interface import implementer
from .observer import IObserver
import six.moves.tkinter as Tk

class CalculatorView(Tk.Tk) :

    def __init__(self, *args, **kwargs) :
        super(CalculatorView, self).__init__(*args, **kwargs)
        self.title("Tkinter MVC Caculator")
        self.frame = CalculatorFrame(self)
        self.deiconify()

    @property
    def display(self) :
        return self.frame.display
        
    @property
    def buttons(self) :
        return CalculatorButton.instances
        

class CalculatorFrame(Tk.Frame) :

    def __init__(self, parent, *args, **kwargs) :
        super(CalculatorFrame, self).__init__(*args, **kwargs)
        self.pack(fill=Tk.BOTH, expand=1)
        self.display = DisplayPanel(self)
        self.keyboard = KeyboardPanel(self)


@implementer(IObserver)
class DisplayPanel(Tk.LabelFrame) :

    def __init__(self, parent, *args, **kwargs) :
        super(DisplayPanel, self).__init__(parent, *args, **kwargs)
        self.pack(side=Tk.TOP, fill=Tk.BOTH)
        self.result = Tk.Label(
                            self,
                            text="0",
                            bg='black', fg='lime',
                            width=24, height=2,
                            font=("Arial", 12),
                            anchor=Tk.E, justify=Tk.RIGHT
                        )
        self.result.pack(fill=Tk.X, expand=1, padx='0.5m', pady='0.5m')

    def update(self, *args, **kwargs) :
        self.result.config(text=str(kwargs['display']))


class KeyboardPanel(Tk.LabelFrame) :

    def __init__(self, parent, *args, **kwargs) :
        super(KeyboardPanel, self).__init__(parent, *args, **kwargs)
        self.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        
        self.numbers = NumbersPanel(self)
        self.operators = OperatorsPanel(self)


class LayoutPanel(object) :

    layout = []

    def placement(self, bg=None, fg=None, width=4, height=2, padx='0.5m', pady='0.5m') :

        for button_group in self.layout :
            group = Tk.Frame(self)
            group.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            for button in button_group :
                CalculatorButton(
                    group,
                    text=button,
                    bg=bg, fg=fg,
                    width=width, height=height
                ).pack(
                    side=Tk.LEFT,
                    fill=Tk.BOTH, expand=1,
                    padx=padx, pady=pady
                )

        
class NumbersPanel(Tk.Frame, LayoutPanel) :

    layout = [
        ('7', '8', '9'),
        ('4', '5', '6'),
        ('1', '2', '3'),
        ('0', '.', '=')
    ]

    def __init__(self, parent) :
        super(NumbersPanel, self).__init__(parent)
        self.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.placement(bg='purple', fg='white')

                
class OperatorsPanel(Tk.LabelFrame, LayoutPanel) :

    layout = [
        ('/',),
        ('*',),
        ('-',),
        ('+',)
    ]

    def __init__(self, parent) :
        super(OperatorsPanel, self).__init__(parent)
        self.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)
        self.placement(bg='white', fg='purple')
        

class CalculatorButton(Tk.Button) :

    instances = []

    def __init__(self, parent, *args, **kwargs) :
        super(CalculatorButton, self).__init__(parent, *args, **kwargs)
        CalculatorButton.instances.append(self)

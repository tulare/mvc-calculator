# -*- encoding: utf-8 -*-

import tkinter as Tk
from zope.interface import implementer
from .observer import IObserver

class CalculatorView :

    def __init__(self) :
        self.root = Tk.Tk()
        self.root.title("Tkinter MVC Caculator")

        self.frame = Tk.Frame(self.root)
        self.frame.pack(fill=Tk.BOTH, expand=1)
        self.display = DisplayPanel(self.frame)
        self.keyboard = KeyboardPanel(self.frame)

    def mainloop(self) :
        self.root.deiconify()
        self.root.mainloop()

    @property
    def buttons(self) :
        return self.keyboard.buttons
        

@implementer(IObserver)
class DisplayPanel :

    def __init__(self, parent) :

        self.frame = Tk.LabelFrame(parent)
        self.frame.pack(side=Tk.TOP, fill=Tk.BOTH)
        self.result = Tk.Label(self.frame,
                               text="0",
                               bg='black', fg='lime',
                               width=24, height=2,
                               font=("Arial", 12),
                               anchor=Tk.E,
                               justify=Tk.RIGHT
                               )
        self.result.pack(fill=Tk.X, expand=1, padx='0.5m', pady='0.5m')


    def update(self, *args, **kwargs) :
        self.result.config(text=str(kwargs['display']))


class KeyboardPanel :

    def __init__(self, parent) :
        self.frame = Tk.LabelFrame(parent)
        self.frame.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        
        self.numbers = NumbersPanel(self.frame)
        self.operators = OperatorsPanel(self.frame)

    @property
    def buttons(self) :
        return { **self.numbers.buttons, **self.operators.buttons }


class LayoutPanel :

    layout = []
    frame = None

    def placement(self, bg=None, fg=None, width=4, height=2, padx='0.5m', pady='0.5m') :

        self.buttons = {}

        for button_group in self.layout :
            group = Tk.Frame(self.frame)
            group.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
            for button in button_group :
                self.buttons[button] = Tk.Button(group,
                                                 text=button,
                                                 bg=bg, fg=fg,
                                                 width=width, height=height
                                        )
                self.buttons[button].pack(side=Tk.LEFT,
                                          fill=Tk.BOTH, expand=1,
                                          padx=padx, pady=pady)
        
class NumbersPanel(LayoutPanel) :

    layout = [
        ('7', '8', '9'),
        ('4', '5', '6'),
        ('1', '2', '3'),
        ('0', '.', '=')
    ]

    def __init__(self, parent) :
        self.frame = Tk.Frame(parent)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.placement(bg='purple', fg='white')

                
class OperatorsPanel(LayoutPanel) :

    layout = [
        ('/',),
        ('*',),
        ('-',),
        ('+',)
    ]

    def __init__(self, parent) :
        self.frame = Tk.LabelFrame(parent)
        self.frame.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)
        self.placement(bg='white', fg='purple')
        

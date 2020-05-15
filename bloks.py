# -*- coding: utf-8 -*-

"""
This class is created by Tiina Ferm
"""

from abc import ABC, abstractmethod
from tkinter import ttk

class Block(ttk.Frame, ABC):

    def __init__(self, parent):
        '''
        call Fram'se init method
        '''
        ttk.Frame.__init__(self, parent) #parent element e.g. TK or Frame where this Frame is in

    @abstractmethod
    def disable(self, nro):
        pass

    def disableAll(self):
        '''
        disable all buttons (self.buttons is assumed)
        '''
        for i in range(len(self.buttons)):
            self.buttons[i].config(state="disabled")

    def enableAll(self):
        '''
        enable all buttons (self.buttons is assumed)
        '''
        for i in range(len(self.buttons)):
            self.buttons[i].config(state="normal")




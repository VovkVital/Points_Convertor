import tkinter
import customtkinter
from Treeview import Treeview
import asyncio
import time


list = [["Test 1", "Data -1"],["Test 2", "Data -2 "],["Test 3", "Data -3"]]

class step_2_test():
    def first_step(self):
         self.function_1()
         self.Tree()
         self.function_2()

    def function_1(self):
        print("Function_1")

    def Tree(self):
        print("Tree started")
        Treeview(data=list)
        time.sleep(5)
        print("Tree finished")

    def function_2(self):
        print("Function 2")





from input_module import take_input
from process_module import process
from output_module import output
from welcome import greet
import os
os.system("cls")

greet()

while True:
    i = take_input()
    o = process(i)
    output(o)

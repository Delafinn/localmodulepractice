# learning to import local modules
from namelist import *
import time
while True:
    gq = input("do you want to display the list of names?")
    if gq == "yes" or gq ==" yes" or gq == "y" or gq == "Y":
        print(namelist)
    time.sleep(3)
    if gq == "no" or gq ==" no" or gq == "n" or gq == "N":
    quit()

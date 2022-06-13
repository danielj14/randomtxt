import json
from random import randrange
from tkinter.font import names

def readFile(fileName):
    file = open(fileName, "rt")
    return json.loads(file.read())

def getText():
    txts = readFile("JsonUtils/Texts.json")["texts"]
    return txts[randrange(0, len(txts))]

def getName():
    names = readFile("JsonUtils/Names.json")["names"]
    return names[randrange(0, len(names))]
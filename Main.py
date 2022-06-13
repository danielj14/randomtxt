# Imports
import Commands.CmdBase as Cmds
import requests

# Code

print("RandomTXT\nCreated by Daniel Júnior")
print("Para gerar um texto aleatorio digite o comando \"randomtxt\" \n")

cmdinput = input("> ")
print(Cmds.commands.get(cmdinput))
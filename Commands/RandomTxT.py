from JsonUtils import JsonFuncs
from .  import CmdBase

def func():
    text = JsonFuncs.getText()
    name = JsonFuncs.getName()
    return text.replace("[]", name)

CmdBase.commands["randomtxt"] = func()
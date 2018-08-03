import platform
if (platform.system()=="window"):
    os.system("PowerShell Mount-DiskImage D:\learning\GTA Grand Theft Auto V.iso")
    #as mount operates only in powershell
elif (platform.system()=="Linux"):
    os.system("mount /dev/dvdrom /mount-point")

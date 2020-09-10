import argparse
import speedtest

cybertest = speedtest.Speedtest()

def download_speed():
    downloadrate = round(cybertest.download() / 1_000_000,2)
    return str(downloadrate) + " Mbps"
    
def upload_speed():
    uploadrate = round(cybertest.upload() / 1_000_000,2)
    return str(uploadrate) + " Mbps"

if _name_ == "__main__":
    bp = argparse.ArgumentParser()
    gathered = bp.add_mutually_exclusive_group()
    gathered.add_argument()
    gathered.add_argument()
    arguments = bp.parse_args()
    
    if arguments.download:
        print()
    
    

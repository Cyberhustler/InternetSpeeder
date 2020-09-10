import argparse
import speedtest

cybertest = speedtest.Speedtest()

def  getspeed():
    downloadrate = round(cybertest.download() / 1_000_000,2)
    return str(downloadrate) + " Mbps"
    
def  givespeed():
    uploadrate = round(cybertest.upload() / 1_000_000,2)
    return str(uploadrate) + " Mbps"

if _name_ == "__main__":
    bp = argparse.ArgumentParser()
    gathered = bp.add_mutually_exclusive_group()
    gathered.add_argument()
    gathered.add_argument()
    arguments = bp.parse_args()
    
    if arguments.download:
        print(f"\nDownload Rate : {getspeed()}\n")
    elif arguments.upload:
        print(f"\nUpload Rate : {givespeed()}\n")
    else:
        print("""\n Choose which one to check :
  -d:  Download Rate
  -u:  Upload Rate 
  """)

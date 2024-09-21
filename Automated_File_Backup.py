import os
import shutil
import datetime
import schedule
import time

source_dir = "D:/New Back/Back from"
destination_dir = "D:/New Back/Back To"

def copy_folder_to_destination(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder exists in: {dest}")
        
def l():
    copy_folder_to_destination(source_dir, destination_dir)
        
schedule.every().day.at("18:40:00").do(l)
        
copy_folder_to_destination(source_dir, destination_dir)

while True:
    schedule.run_pending()
    time.sleep(60)

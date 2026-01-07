import os, tqdm, requests
import pandas as pd
from PIL import Image
from io import BytesIO

API_KEY = 'YOUR_API_KEY_HERE'
IMAGE_SIZE = '400x400'
ZOOM = 19

df_train = pd.read_excel("train.xlsx")
df_test = pd.read_excel("test.xlsx")

os.makedirs("images_train", exist_ok=True)
os.makedirs("images_test", exist_ok=True)

def fetch_satellite_image(lat, long, save_path):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom={ZOOM}&size={IMAGE_SIZE}&maptype=satellite&key={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(save_path)
            return True
        else:
            print(f"Failed for {lat}, {long}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {lat}, {long}: {e}")
    return False

success_count = 0
fail_count = 0
for idx, row in tqdm.tqdm(df_train.iterrows(), desc="Downloading train images"):
    img_path = f"images_train/{row['id']}.png"
    if not os.path.exists(img_path):
        if fetch_satellite_image(row['lat'], row['long'], img_path):
            success_count += 1
        else:
            fail_count += 1
print(f"Train images: {success_count} downloaded, {fail_count} failed")

success_count = 0
fail_count = 0
for idx, row in tqdm.tqdm(df_test.iterrows(), desc="Downloading test images"):
    img_path = f"images_test/{row['id']}.png"
    if not os.path.exists(img_path):
        if fetch_satellite_image(row['lat'], row['long'], img_path):
            success_count += 1
        else:
            fail_count += 1
print(f"Test images: {success_count} downloaded, {fail_count} failed")
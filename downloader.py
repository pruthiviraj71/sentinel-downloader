import os
from pathlib import Path
import xml.etree.ElementTree as ET
import subprocess
from math import isclose
import shutil
import argparse

from tqdm import tqdm
import win32com.client as com

fso = com.Dispatch("Scripting.FileSystemObject")

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, default='products.meta4', help="Filename of the xml containing all the product IDs. Can be downloaded from 'https://scihub.copernicus.eu/dhus/#/home'")
parser.add_argument('-v', '--verbose', type=bool, default=False, help='Verbose level.')
args = parser.parse_args()
filename = args.filename
if filename.endswith('.meta4'):
    newfilename = filename.split('.')[0] + '.xml'
    filename = shutil.copyfile(filename, newfilename)
verbose = args.verbose

# Path to gsutil present in the google cloud sdk and download path.
path_to_gcp_sdk = "C:/............/google-cloud-sdk/bin/gsutil"
download_path = "."

list_of_products = []

tree = ET.parse(filename)
root = tree.getroot()
for child in root:
    url = child[2].text
    uuid = url.split('(')[1].split(')')[0][1:-1]
    product_name = child.attrib['name'] + '.SAFE'
    list_of_products.append(product_name)

print(f"Number of Products to process: {len(list_of_products)}\n")

for file_name in tqdm(list_of_products):

    # Download link for the product.
    download_link = f"gs://gcp-public-data-sentinel-2/tiles/{file_name[39:41]}/{file_name[41:42]}/{file_name[42:44]}/{file_name}"

    if os.path.exists(file_name):

        # Fetch folder size of existing product.
        local_path = os.path.join(os.getcwd(), file_name)
        folder = fso.GetFolder(local_path)
        local_size = folder.Size

        # Fetch product size from gcp.
        cmd = [path_to_gcp_sdk, 'du', '-s', download_link]
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        origin_size = int(output.stdout.decode(encoding='utf-8').split()[0])

        if isclose(origin_size, local_size, abs_tol = 1):
            if verbose:
                print(f'{file_name} already downloaded')
            continue
        else:
            shutil.rmtree(local_path)

    try:
        command = f'{path_to_gcp_sdk} -m cp -r {download_link} {download_path}'
        print(f"Downloading {file_name}")
        if verbose:
            result = subprocess.call(command, shell=True)
        else:
            result = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        continue

    # Add empty AUX_DATA, HTML, QI_DATA folders to make it compatible with sen2cor.
    temp_path = os.getcwd()
    os.chdir(file_name)
    Path("AUX_DATA").mkdir(parents=True, exist_ok=True)
    Path("HTML").mkdir(parents=True, exist_ok=True)
    os.chdir('DATASTRIP')
    os.chdir(os.listdir()[0])
    Path("QI_DATA").mkdir(parents=True, exist_ok=True)
    os.chdir(temp_path)
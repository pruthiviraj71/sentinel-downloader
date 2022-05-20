# Sentinel Data Downloader
Download Sentinel 2A Data from GCP.

## Getting Started

1. Install Google Cloud CLI from Google Cloud SDK which includes gcloud, gsutil and other tools [from here](https://cloud.google.com/sdk/docs/install). (If using proxy, download from [Versioned Archives](https://cloud.google.com/sdk/docs/downloads-versioned-archives))
2. Run `gsutil version` to check if properly installed.
3. Run `gcloud init` and login to continue.
4. Select or create a new project.

Once these are done. gcloud CLI is configured.

## Input File

The input file should be an meta4/xml file generated from 'https://scihub.copernicus.eu/dhus/#/home'.

## Usage
```
In download.py, replace the 'path_to_sdk' with the gsutil path present in the bin directory of google-cloud-sdk.

Usage: python downloader.py [-h] [-f FILENAME] [-v VERBOSE]

Available commands:

  -h, --help                  show this help message and exit
  -f FILENAME, --filename     FILENAME
                              Filename of the xml containing all the product IDs. Can be downloaded from
                              'https://scihub.copernicus.eu/dhus/#/home'
  -v VERBOSE, --verbose       VERBOSE
                              Verbose level.
```

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

Usage: python download.py [-f] [-filename] [-v] [--verbose]

Available commands:

  filename      Filename of the xml containing all the product IDs. Can be downloaded from 'https://scihub.copernicus.eu/dhus/#/home'
  verbose       Verbose level. (True/False)
```

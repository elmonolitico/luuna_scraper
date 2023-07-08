# MercadoLibre Scraper

This is a Python script that scrapes product data from the MercadoLibre marketplace and uploads it to an API for further processing. The script utilizes the requests library to make HTTP requests, fetch product data, and upload it to the specified API.

## Prerequisites

- Python 3.x
- requests library

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the required dependencies by running the following command:


## Configuration

Before running the script, make sure to set up the following configurations:

1. Modify the `merchant` variable in the `scrape_mercadolibre` function to match the desired MercadoLibre merchant.
2. Set up environment variables for the API access:
- `API_TOKEN`: API access token.
- `API_URL`: URL of the API to upload the data to.

## Usage

To run the script, execute the following command:


The script will scrape product data from MercadoLibre, add a timestamp to each product, and upload the data to the specified API. The output will include the scraped data along with a success or failure message for the data upload.

## Error Handling

In case of any exceptions during scraping or data upload, the script will print error messages with details about the encountered issue.

Please note that this script is provided as an example and may require further customization based on your specific use case.

Feel free to reach out if you have any questions or need further assistance.

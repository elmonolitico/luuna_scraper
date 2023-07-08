import requests
from time import sleep
from datetime import datetime
import json
import os

API = "https://api.mercadolibre.com"

def scrape_mercadolibre():
    merchant = "KSMVCAPITALSAPIDECV"
    products = []
    offset = 0

    try:
        while True:
            # Make a request for the next page of results
            response = requests.get(f"{API}/sites/MLM/search?nickname={merchant}&offset={offset}&limit=50").json()
            # Extract the results from the response
            page_results = response['results']
            # Add the extracted results to the list of all results
            products += page_results
            # Update the offset for the next page of results
            offset += len(page_results)
            # Check if we have extracted all the available results
            if offset >= response['paging']['total']:
                break
            # Sleep for a short time before making the next request
            sleep(0.5)
    except Exception as e:
        # Handle any exceptions that occur during scraping
        print(f"Scraping failed: {str(e)}")
        return []

    return products

def upload_data_to_api(products):
    api_token = os.environ['API_TOKEN']
    url = os.environ['API_URL']

    payload = json.dumps({
        "collection": "luuna",
        "database": "zebrands",
        "dataSource": "luuna",
        "documents": products
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': api_token
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        if response.ok:
            print("Data uploaded successfully")
        else:
            print(f"Data upload failed: {response_data['message']}")
    except Exception as e:
        # Handle any exceptions that occur during data upload
        print(f"Data upload failed: {str(e)}")

def lambda_handler(event, context):
    # Scrape data from MercadoLibre
    scraped_data = scrape_mercadolibre()

    # Add timestamp to the scraped data
    timestamp = datetime.now().isoformat()
    for product in scraped_data:
        product['timestamp'] = timestamp

    # Upload the scraped data to the API
    upload_data_to_api(scraped_data)

    return {
        'statusCode': 200,
        'body': json.dumps(scraped_data)
    }
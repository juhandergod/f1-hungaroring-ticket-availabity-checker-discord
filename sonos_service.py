import json

import requests
from bs4 import BeautifulSoup

import discord

base_url = "https://www.sonos.com/en/shop/"

products = [
    "sub-mini-b-stock",
    # "sub-g3-b-stock"
]


def check_availability(product_name: str):
    html_data = fetch_data(product_name)

    json_data = get_html_element(html_data, 'script#__NEXT_DATA__').text
    sonos_data = json.loads(json_data)
    stock_level = sonos_data['props']['pageProps']['product']['inventory']['stockLevel']
    if stock_level > 0:
        discord.send_message("Sonos product available: " + product_name + " - " + base_url + product_name)

    return

def fetch_data(product_name: str):
    response = requests.get(base_url + product_name)
    if response.status_code == 200:
        return response.text
    else:
        discord.send_message(f"Failed to fetch data for {product_name}. Status code: {response.status_code}")
        return None


def get_html_element(html: str, selector: str):
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.select_one(selector)
    return element


if __name__ == '__main__':
    for product in products:
        check_availability(product)
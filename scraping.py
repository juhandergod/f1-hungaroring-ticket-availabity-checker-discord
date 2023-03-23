import requests
from bs4 import BeautifulSoup

url = 'https://www.gpticketshop.hu/Formula_1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def get_weekend_tickets(page):
    products = page.find_all('td', class_="product-name")
    new_tickets = []
    for element in products:
        if element.text.find("Weekend") != -1:
            new_tickets.append(element)

    return new_tickets


def get_available_weekend_tickets():
    tickets = get_weekend_tickets(soup)
    available_tickets = []
    for ticket in tickets:
        if ticket.find_parent().find("td", class_="product-add").text.find("Sold out") == -1:
            available_tickets.append(ticket)

    return available_tickets


def get_tickets_name(tickets):
    tickets_name = []
    for ticket in tickets:
        tickets_name.append(ticket.text)

    return tickets_name

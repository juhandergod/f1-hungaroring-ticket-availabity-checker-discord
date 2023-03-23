import discord
import scraping
from time import sleep

if __name__ == '__main__':
    tickets = scraping.get_available_weekend_tickets()

    if len(tickets) != 0:
        ticket_names = scraping.get_tickets_name(tickets)
        for ticket_name in ticket_names:
            discord.send_message("Ticket available: " + ticket_name + " - " + scraping.url)
            sleep(1)
    else:
        print("No tickets available")
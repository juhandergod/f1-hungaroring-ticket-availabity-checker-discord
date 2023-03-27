import crython
import discord
import scraping
from flask import Flask
from time import sleep

app = Flask(__name__)


@app.route("/")
def hello():
    return "F1 ticket bot"


@crython.job(second=0)
def ticket_checker_job():
    tickets = scraping.get_available_weekend_tickets()
    if len(tickets) != 0:
        ticket_names = scraping.get_tickets_name(tickets)
        for ticket_name in ticket_names:
            discord.send_message("Ticket available: " + ticket_name + " - " + scraping.url)
            sleep(1)
    else:
        print("No ticket available.")


if __name__ == "__main__":
    discord.send_message("Script started successfully.")
    crython.start()
    app.run()

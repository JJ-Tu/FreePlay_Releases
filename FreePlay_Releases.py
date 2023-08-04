#!/usr/bin/env python
# coding: utf-8

# # Email notifications

import smtplib

# Set up Gmail credentials
gmail_username = "obv.thrw.awy.343@gmail.com"
gmail_password = "bdxlzkgxxjckaxbi"


def send_email(subject, body, recipient):
    try:
        # Connect to Gmail SMTP server
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        
        # Log in to your Gmail account
        smtp_server.login(gmail_username, gmail_password)

        # Compose the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        smtp_server.sendmail(gmail_username, recipient, message)

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

    finally:
        # Close the SMTP connection
        smtp_server.quit()

def send_notification():
    subject = "New Tickets Released!"
    body = "New tickets are now available on the website."
    recipient = "jonathantu2000@gmail.com"  # Replace with the recipient's email address
    send_email(subject, body, recipient)


# # Web scraping

import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://www.centertheatregroup.org/tickets/freeplay/"


# Function to fetch the webpage's HTML content and extract the relevant section
def get_relevant_section(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        h3_tag = soup.find("h3", string="Ahmanson Theatre")
        div_tag = soup.find("div", {"class": "unit-aside unit-aside-panel", "id": "health-and-safety-policy"})
        
        # Extract the content between the h3 and div tags
        relevant_section = ""
        while h3_tag and h3_tag.next_sibling != div_tag:
            relevant_section += str(h3_tag.next_sibling)
            h3_tag = h3_tag.next_sibling
        
        return relevant_section
    else:
        return None

# Main function to check for changes and trigger notifications
def check_for_changes():
    # Fetch the current section
    current_section = get_relevant_section(url)
    
    # Read the previous section from a file or create an empty string if the file doesn't exist
    try:
        with open("previous_section.txt", "r") as file:
            previous_section = file.read()
    except FileNotFoundError:
        previous_section = ""
    
    # Compare the current and previous sections
    if current_section != previous_section:
        # Update the previous section with the current one
        print(previous_section)
        print(current_section)
        with open("previous_section.txt", "w") as file:
            file.write(current_section)
        
        # Trigger the notification
        send_notification()
    else:
        # For testing purposes. Delete after confirming functionality
        send_email("This is a test", "This is a test. No changes were detected at this time.", "jonathantu2000@gmail.com")


# Call the main function to check for changes
check_for_changes()





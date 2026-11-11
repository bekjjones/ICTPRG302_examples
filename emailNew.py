#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the gmail smtp server.

Update: 11/11/2026 RAnderson - change server and port

"""

import smtplib


def send_email(message):
    """Send an email notification with the specified message."""

    # Store the email server and account details.
    smtp = {"sender":    "bek.j.jones@gmail.com",
    "recipient": "bek.j.jones@gmail.com",
    "server":    "smtp.gmail.com",
    "port":      587,
    "user":      "bek.j.jones@gmail.com",
    "password":  "phqc kkks qxst dzix"}

    # Create the email message with the recipient, sender, subject, and body.
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: \n\n' + message + '\n'
    
    try:
        # Connect to the email server and send the notification.
        with smtplib.SMTP(smtp["server"], smtp["port"], timeout=10) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()
            smtp_server.login(smtp["user"], smtp["password"])
            smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
            print("Email notification sent successfully.")

    # Handle errors that occur while sending the email notification.
    except Exception as e:
        print(f"ERROR: Email notification failed: {e}")


def main():
            send_email("Testing email function");

# Run the main function when the program is executed directly.
if __name__ == "__main__":
    main()
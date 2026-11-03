#!/usr/bin/env python3
# File name          : protintel.py
# Author             : GitHub: @C3n7ral051nt4g3ncy

# Py libs
import requests
import re
import datetime


def printprotintelligencebanner():
    GREEN_BOLD = "\033[32m\033[1m"
    RED = "\033[31m"
    RESET = "\033[0m"

    banner = r"""
* * * * * * * * * * * * * * * * * * * *
*  ___         _   _ _  _ _____    _  *
* | _ \_ _ ___| |_/ | \| |_   _|__| | *
* |  _/ '_/ _ \  _| | .` | | |/ -_) | *
* |_| |_| \___/\__|_|_|\_| |_|\___|_| *
*                                     *
* * * * * * * * * * * * * * * * * * * *
"""

    print(
        GREEN_BOLD
        + banner
        + "\nGitHub:  https://github.com/C3n7ral051nt4g3ncy"
        + "\nTwitter: @OSINT_Tactical"
        + f"\nTool Contributions (₿TC): {RED}bc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde{GREEN_BOLD}"
        + "\n___________________________________________________________________"
        + RESET
    )


def extract_timestamp(source_code):
    timestamp = re.findall(r':(\d{10}):', source_code)
    return int(timestamp[0]) if timestamp else None


def extract_key_and_length(source_code):
    lines = source_code.split('\n')
    if len(lines) < 2:
        return None, None
    key_parts = lines[1].split(':')
    try:
        return key_parts[2], key_parts[3]
    except IndexError:
        return None, None


def check_email(email):
    url = f"https://api.protonmail.ch/pks/lookup?op=index&search={email}"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"Request to Proton failed: {e}")
        return

    if response.text.startswith('info:1:1'):
        email_domain = email.split("@")[1]
        if email_domain in ["protonmail.com", "protonmail.ch", "proton.me"]:
            print("This is a Protonmail address.")
        else:
            print("This is a Protonmail custom domain.")

        data = response.text.split('\n')
        if len(data) > 2:
            uid_line = data[2]
            email_in_brackets = re.findall(r'<(.*?)>', uid_line)
            if email_in_brackets:
                actual_email = email_in_brackets[0]
                if actual_email != email:
                    print("Catch-All detected, this is the main email -->", actual_email)

        timestamp = extract_timestamp(response.text)
        if timestamp is not None:
            creation_date = datetime.datetime.fromtimestamp(
                timestamp, datetime.timezone.utc
            ).strftime('%Y-%m-%d %H:%M:%S UTC')
            print("PGP Key Date and Creation Time:", creation_date)
        else:
            print("Problem parsing Key Creation Date.")

        key_type, key_length = extract_key_and_length(response.text)
        if key_type is not None:
            if key_type != "22":
                print(f"Encryption Standard : RSA {key_length}-bit")
            else:
                print("Encryption Standard : ECC Curve25519")
        else:
            print("Problem parsing Encryption Standard.")
    else:
        print("Not a Protonmail address or no public PGP key found.")


if __name__ == "__main__":
    printprotintelligencebanner()
    email = input("Enter the email to check: ")
    check_email(email)

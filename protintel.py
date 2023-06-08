#!/usr/bin/env python3
# File name          : protintel.py
# Author             : GitHub: @C3n7ral051nt4g3ncy

# Py libs
import requests
import re
import datetime

def printprotintelligencebanner():
    print("""\u001b[32m\033[1m

* * * * * * * * * * * * * * * * * * * *
*  ___         _   _ _  _ _____    _  *
* | _ \_ _ ___| |_/ | \| |_   _|__| | *
* |  _/ '_/ _ \  _| | .` | | |/ -_) | *
* |_| |_| \___/\__|_|_|\_| |_|\___|_| *
*                                     *
* * * * * * * * * * * * * * * * * * * *                                                                     

GitHub:  https://github.com/C3n7ral051nt4g3ncy                                                          
Twitter: @OSINT_Tactical                                                                             
Tool Contributions (₿TC): \u001b[31mbc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde\u001b[32m                                                               
___________________________________________________________________ \033[0m\n""")

def extract_timestamp(source_code):
    timestamp = re.findall(r':(\d{10}):', source_code)
    return int(timestamp[0]) if timestamp else None

def extract_key(source_code):
    key_line = source_code.split('\n')[1]
    key_parts = key_line.split(':')
    try:
        key = key_parts[2]
    except IndexError:
        key = None
    return key

def check_email(email):
    url = f"https://api.protonmail.ch/pks/lookup?op=index&search={email}"
    response = requests.get(url)
    if response.text.startswith('info:1:1'):
        print("This is a Protonmail custom domain.")
        data = response.text.split('\n')
        uid_line = data[2]
        actual_email = re.findall(r'<(.*?)>', uid_line)[0]
        if actual_email != email:
            print("Catch-All detected, this is the main email -->", actual_email)

        timestamp = extract_timestamp(response.text)
        if timestamp is not None:
            creation_date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print("PGP Key Date and Creation Time:", creation_date)
        else:
            print("Problem parsing Key Creation Date.")

        key = extract_key(response.text)
        if key is not None:
            if key != "22":
                print("Encryption Standard : RSA " + key + "-bit")
            else:
                print("Encryption Standard : ECC Curve25519")
        else:
            print("Problem parsing Encryption Standard.")
    else:
        print("Not a Protonmail custom domain")

if __name__ == "__main__":
    printprotintelligencebanner()
    email = input("Enter the email to check: ")
    check_email(email)

#!/usr/bin/env python3
# File name          : protintel.py
# Author             : GitHub: @C3n7ral051nt4g3ncy


# Py libs
import requests
import re


# Protintelligence banner
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



def is_protonmail_custom(email):
    url = f"https://api.protonmail.ch/pks/lookup?op=index&search={email}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error occurred: {response.status_code}")
        return None
    else:
        result = response.text
        if 'info:1:1' in result:
            catch_all_email = re.search(r'uid:(.*)<', result)
            if catch_all_email and catch_all_email.group(1) != email:
                print(f"Catch-All detected, this is the main email: {catch_all_email.group(1)}")
            return True
        else:
            return False

def main():
    printprotintelligencebanner()

    email = input("Enter an email address: ")
    if is_protonmail_custom(email):
        print(f"{email} uses a ProtonMail custom domain.")
    else:
        print(f"{email} does not use a ProtonMail custom domain.")

if __name__ == "__main__":
    main()


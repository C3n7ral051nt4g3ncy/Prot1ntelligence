#!/usr/bin/env python3
# File name          : protintel.py
# Author             : GitHub: @C3n7ral051nt4g3ncy
# Forks              : 3 modules out of 7 are based off ProtOSINT from @PixelBubble
# v2.0               : Kr0wZ Fixed first function with selenium



# Py libs

from bs4 import BeautifulSoup
import re
import requests
import ipaddress
import datetime
from datetime import datetime
from googlesearch import search
import webbrowser
import readline



# Script Information

print("\u001b[32m\033[1m\n\nProtINTelligence\033[0m\u001b[32m can be used to get:")
print("- ProtonMail account existence & Creation date")
print("- User PGP Key, creation date, Key Type: RSA 4096 or ECC Curve25519")
print("- Download PGP Key & add to your KeyChain to send encrypted mail to user")
print("- Check if the IP address is a ProtonVPN user")
print("- ProtonMail User Digital Footprints (clear & Dark Web)\n\n")



# Protintelligence banner

def printprotintelligencebanner():
    """
    protintelligence banner
    """
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



# Proton API Check/Verification

def checkprotonapistatus():
    """
    Proton API Online or Offline Check
    """
    requestprotonmailstatus = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=admin@protonmail.com')
    if requestprotonmailstatus.status_code == 200:
        print(
            "\u001b[32m\033[1m\n\nGood to go! ProtonMail API is ONLINE!!!\u001b[32m \U0001F7E2 \033[0m\n\n")
    else:
        print(
            "\u001b[31m Protonmail API is OFFLINE\U0001F534")


# Protintelligence Choices

def printprotintelligenceintro():
    protintelligenceintro = """
\n\n\u001b[31m\U0001F575\033[1m INTELLIGENCE COLLECTION METHOD:\n

\u001b[32m\U0001F50D \033[1mALPHA\033[0m\u001b[32m: Check if ProtonMail account exists\n

\u001b[32m\U0001F4E1 \033[1mBRAVO\033[0m\u001b[32m: Proton Email search to check for digital footprints\n

\u001b[32m\U0001F3F4 \033[1mCHARLY\033[0m\u001b[32m: Dark Web search\n 

\u001b[32m\U0001F511 \033[1mDELTA\033[0m\u001b[32m: Get ProtonMail user PGP Key + Key creation date\n

\u001b[32m\U0001F4BB \033[1mECHO\033[0m\u001b[32m: Verify IP address belongs to ProtonVPN user\n
"""
    print(protintelligenceintro)




# Retrieve the timestamp of created email addreses

def extract_timestamp(mail, source_code):

    try:
        timestamp = re.sub(':', '', re.search(':[0-9]{10}::', source_code.text).group(0))
        creation_date = datetime.fromtimestamp(int(timestamp))

        return creation_date

    except AttributeError:
        return None


# Check if this is a business email address

def check_domain_name(mail):
    if(mail.split("@")[1] == "protonmail.com" or mail.split("@")[1] == "proton.me"):
        return False
    else:
        return True


# Perform the API request

def make_api_request(mail):
    try:
        request = requests.get("https://account.proton.me/api/users/available", 
            headers={
                "x-pm-appversion":"web-account@5.0.11.11",
                "x-pm-locale":"en_US"
            },
            params={
                "Name":mail,
                "ParseDomain":"1"
            })

        is_business_address = check_domain_name(mail)

        #Return code 429 = API limit exceeded
        if(request.status_code == 409):
            source_code = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + mail)
            creation_date = extract_timestamp(mail, source_code)

            print("\033[1m\n\nProtonMail Account is VALID! Creation date: " + str(creation_date) + " \033[0m\U0001F4A5")

            return True

        elif(request.status_code == 429):
            print("\u001b[31m\n\nAPI requests limit exceeded...")

        else:
            if(is_business_address):
                print("\u001b[33m\n\nProtonmail API does not handle business protonmail email addresses. This email may not exist\033[0m")
                return True
            else:
                print("\u001b[31m\n\nProtonMail account is NOT VALID")

        return False

    except:
        print("Error when requesting the API")
        return False


# ProtonMail account validity check

def protonmailaccountcheck():
    """
    ALPHA : Check if ProtonMail account exists
    """
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\u001b[32m\nCheck if ProtonMail account exists \n")
    while invalidEmail:

        mail = input("\033[1mType Email address + Enter : ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False

        else:
            print("\u001b[31m\n\nProtonMail user does not exist\u001b[32m")
            invalidEmail = True

    make_api_request(mail)



# Email search for Digital Footprints

def emailtraces():
    """
    BRAVO : Check Email Traces with a Google Dork
    """

    print("\033[1m\u001b[32m\nChecking server status\n")
    response = requests.get('https://google.com')
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')
    elif response.status_code == 404:
        print('404 Not Found, please try again.')

    searchfor = input(
        """\u001b[32mEnter Target Email in quotation marks!(Example:"admin@protonmail.com"): """)
    print("\nProcessing request...\n")
    for result in search(searchfor, tld="com", num=200, stop=200, pause=2):
        print(result)



# DarkWeb email search

def darkwebtraces():
    """
    CHARLY : Check Dark Web Traces
    """

    print("\033[1m\u001b[32m\nChecking server status\n")
    response = requests.get('https://ahmia.fi')
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')

    elif response.status_code == 404:
        print('404 Not Found, please try again')

    choice = input(
        """\033[1mView results in Browser [B] or Terminal [T]: """)

    if choice == "B":
        darkwebbrowser()

    if choice == "T":
        darkwebterminal()



# Dark Web Search with Browser auto-opening

def darkwebbrowser():
    """
    Dark Web Browser Open

    """
    query = input("""\nInput Target email (example: darkmatterproject@protonmail.com: """)
    webbrowser.open("https://ahmia.fi/search/?q=%s" % query)


# Search results displayed within the terminal

def darkwebterminal():
    """
    Dark Web Terminal

    """

    query = input("Input target email: ")
    URL = ("https://ahmia.fi/search/?q=%s" % query)
    page = requests.get(URL)
    request = requests.get(URL)

    if request.status_code == 200:
        print("\n\nRequest went through\n")

    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"])


# Get ProtonMail User PGP Key

def pgpkeyinformation():
    """
    DELTA: Get ProtonMail user PGP Key & Info

    """

    choice = input(
        """\033[1m\nView PGP Key in Terminal [T] or Download Key [D]: """)

    if choice == "T":
        pgpkeyview()

    if choice == "D":
        pgpkeydirectdownload()


def pgpkeydirectdownload():
    """
    Download PGP Key Directly

    """

    query = input(
        """\nInput Target email to Download PGP Key: """)
    webbrowser.open("https://api.protonmail.ch/pks/lookup?op=get&search=" + query)


def extract_key(source_code):
    """
    Extract the key type and length of the email address
    """

    regex = ':[0-9]{2,4}:(.*)::'

    try:
        key = re.search(regex, source_code.text).group(0).split(":")[1]
        return key
    except AttributeError:
        return None


def pgpkeyview():
    """
    View PGP Key in Terminal

    """

    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\nInput Protonmail user email to get user's PGP Key\n")
    while invalidEmail:

        mail = input("\033[1mType Proton email + Enter: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\u001b[31m\n\nProtonmail user does not exist\u001b[32m")
            invalidEmail = True

    #Business addresses are not handled with the new API, so there is a risk that the email doesn't exists and returns a random timestamp

    if(make_api_request(mail)):
        source_code = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + mail)

        if("info:1:0" in source_code.text):
            print("\u001b[31m\n\nCan't retrieve the PGP information\u001b[32m")
        else:
            timestamp = extract_timestamp(mail, source_code)
            key = extract_key(source_code)

            print("\u001b[32mPGP Key Date and Creation Time:", str(timestamp))

            if(key != "22"):
                print("\u001b[32mEncryption Standard : RSA " + key + "-bit")
            else:
                print("\u001b[32mEncryption Standard : ECC Curve25519")

            # Get the USER PGP Key
            invalidResponse = True

            print("\033[1m\nGet user PGP Key? ")
            while invalidResponse:
                # Input
                responseFromUser = input("""\033[1m [Y] or [N]:\033[0m """)
                # Text if the input is valid
                if responseFromUser == "Y":
                    invalidResponse = False
                    requestProtonPublicKey = requests.get('https://api.protonmail.ch/pks/lookup?op=get&search=' + str(mail))
                    bodyResponsePublicKey = requestProtonPublicKey.text
                    print(bodyResponsePublicKey)
                elif responseFromUser == "N":
                    invalidResponse = False
                else:
                    print("Input Not Valid")
                    invalidResponse = True



# Check user IP belongs to ProtonVPN user

def protonvpnipsearch():
    """
    ECHO : Find out if user IP address is a ProtonVPN user
    """

    while True:
        try:
            ip = ipaddress.ip_address(input(
                '\033[1m\n\nEnter Target IP address: (Example: "185.159.157.1"): '))
            break
        except ValueError:
            continue

    requestProton_vpn = requests.get('https://api.protonmail.ch/vpn/logicals')
    bodyResponse = requestProton_vpn.text
    if str(ip) in bodyResponse:
        print(
            "\033[1m\n\nThis IP belongs to a ProtonVPN user! \n")
    else:
        print(
            "\u001b[31m\033[1m\n\nThis IP does not belong to a ProtonVPN user\n")


def main():
    printprotintelligencebanner()
    choice = input(
        """\033[1m\u001b[32mType [c] or [C] to check Proton API Status: \033[0m\u001b[32m""")
    if choice == "c" or choice == "C":
        checkprotonapistatus()
    choice = input("""\033[1mView All Options? \u001b[32m [Y] or [N]:\033[0m\u001b[32m """)
    if choice == "Y":
        printprotintelligenceintro()

    while True:
        choice = input("""\033[1mInput CAPITAL LETTER from each option to make choice!\n"""
                       """\nA | B | C | D |E"""
                       """\n:  """)
        if choice == "A":
            protonmailaccountcheck()
        if choice == "B":
            emailtraces()
        if choice == "C":
            darkwebtraces()
        if choice == "D":
            pgpkeyinformation()
        if choice == "E":
            protonvpnipsearch()

        inp = input("\n\n\u001b[32m\033[1mContinue [Y] or [N]: ")
        if inp.lower() == 'n':
            break




if __name__ == '__main__':
    main()

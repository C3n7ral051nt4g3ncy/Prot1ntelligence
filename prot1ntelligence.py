#!/usr/bin/env python3
# File name          : prot1ntelligence.py
# Author             : GitHub: @C3n7ral051nt4g3ncy
# Creation Date      : 09 June 2022 (Script started on 01/05/2022)

# Py library
from bs4 import BeautifulSoup
import re
import requests
import ipaddress
import datetime
from datetime import datetime
from googlesearch import search
import webbrowser
import readline


# Script Information in English
print("\u001b[32m[ENG] \033[1mProt1ntelligence\033[0m\u001b[32m is used to find information on:")
print("- ProtonMail account existence & Creation date")
print("- User PGP Key, creation date, Key Type: RSA 4096 or ECC Curve25519")
print("- Download PGP Key & add to your KeyChain to send encrypted mail to user")
print("- Check if the IP address is a ProtonVPN user")
print("- ProtonMail User Digital Footprints (clear & Dark Web)\n\n")

# Script Information in French
print("\u001b[33m[FR] \033[1mProt1ntelligence\033[0m\u001b[33m pour obtenir des infos sur:")
print("- Un compte ProtonMail et sa date de creation")
print("- Cle PGP de l'utilisateur, date de creation de la cle")
print("- Telechargement de la cle pour ajouter a votre KeyChain")
print("- Type de cle PGP: RSA 4096 ou ECC Curve25519")
print("- Adresse IP et savoir si c'est un utilisateur ProtonVPN")
print("- Empreinte Numerique de la cible (Source Ouverte et sur le Dark Net)\n")


# Prot1ntelligence banner
def printprot1ntelligencebanner():
    """
    prot1ntelligence banner
    """
    print("""\u001b[32m\033[1m


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *         
*     ____  ____  ____  __________   ________________    __    _________________   ______________   *
*    / __ \/ __ \/ __ \/_  __<  / | / /_  __/ ____/ /   / /   /  _/ ____/ ____/ | / / ____/ ____/   *
*   / /_/ / /_/ / / / / / /  / /  |/ / / / / __/ / /   / /    / // / __/ __/ /  |/ / /   / __/      *
*  / ____/ _, _/ /_/ / / /  / / /|  / / / / /___/ /___/ /____/ // /_/ / /___/ /|  / /___/ /___      *
* /_/   /_/ |_|\____/ /_/  /_/_/ |_/ /_/ /_____/_____/_____/___/\____/_____/_/ |_/\____/_____/      *
*                                                                                                   *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⢠⣾⡿⣿⣿⣿⣛⡛⢟⣿⣿⣛⣻⣿⣿⣿⢿⣷⡅⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⢠⣿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠹⣿⡀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⣤⣧⣾⣿⣿⣿⣿⣿⣿⣿⣖⣂⣲⣿⣿⣿⣿⣿⣿⣿⣶⣼⣄⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿                                           
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿                                          
⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⡿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿                                            
⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠈⠻⢿⣿⣿⠿⢋⣀⣀⠀⣀⣀⡙⠿⣿⣿⡿⠟⢁⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿                                           
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿                                           
⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣧⣤⣿⣿⣿⣿⠟⠻⠿⠾⠿⠟⠻⣻⣿⣿⣷⣄⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿                                            
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡇⠀⢘⣻⣿⣟⡃⠀⢸⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿                                           
⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿                                           
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿                                           
⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⠛⠿⣻⣿⣿⣿⣿⠏⠋⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿                                           
⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⠀⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿                                           
⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿                                          
                C3n7ral051nt4g3ncy                                                                  

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
            "\u001b[32m\033[1m\n\nGood to go! ProtonMail API is ONLINE!!!\u001b[32m \U0001F7E2 \U0001F680 \n\u001b[33mRAS! API ProtonMail est EN LIGNE!!! \033[0m \U0001F7E2 \U0001F680 \n\n")
    else:
        print(
            "\u001b[31m Protonmail API is OFFLINE\U0001F534   |  \u001b[31m ProtonMail API est HORS LIGNE \U0001F534")


# Script Choices Intro in English and French
def printprot1ntelligenceintro():
    prot1ntelligenceintro = """
\u001b[31m\U0001F575\033[1m INTELLIGENCE COLLECTION METHOD: \n\u001b[31mCHOIX METHODE DE COLLECTE DE RENSEIGNEMENT:\n

\u001b[32m\U0001F50D \033[1mALPHA\033[0m\u001b[32m: Type alpha to check if a ProtonMail account exists\n\u001b[33m\033[1mALPHA\033[0m\u001b[33m: Tapez alpha pour verifier si un compte ProtonMail existe 

\u001b[32m\U0001F4E1 \033[1mBRAVO\033[0m\u001b[32m: Type bravo to run a search on the Proton email to check digital footprints\n\u001b[33m\033[1mBRAVO\033[0m\u001b[33m: Tapez bravo pour lancer une verification sur le mail Proton et voir l'empreinte numérique 

\u001b[32m\U0001F3F4 \033[1mCHARLIE\033[0m\u001b[32m: Type charlie to run a Dark Web search on the Proton Email\n\u001b[33m\033[1mCHARLIE\033[0m\u001b[33m: Tapez charlie pour lancer une verification Dark Net sur le mail

\u001b[32m\U0001F511 \033[1mDELTA\033[0m\u001b[32m: Type delta to get ProtonMail user PGP Key and Key creation date\n\u001b[33m\033[1mDELTA\033[0m\u001b[33m: Tapez delta pour obtenir la cle PGP de l'utilisateur et date de creation de la cle

\u001b[32m\U0001F4BB \033[1mECHO\033[0m\u001b[32m: Type echo to verify if an IP address belongs to a ProtonVPN user\n\u001b[33m\033[1mECHO\033[0m\u001b[33m: Tapez echo pour verifier si une adresse IP appartient a un utilisateur ProtonVPN\u001b[32m
"""
    print(prot1ntelligenceintro)


# ProtonMail account validity check
def protonmailaccountcheck():
    """
    ALPHA : Check if ProtonMail account exists
    """
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\u001b[32m\nCheck if ProtonMail account exists \n\u001b[33mVerifier si compte ProtonMail existe:\033[0m\u001b[32m\n")
    while invalidEmail:

        mail = input("\033[1mEmail + Enter : ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False

        else:
            print("\u001b[31m\n\nProtonMail user does not exist\u001b[32m")
            invalidEmail = True

    requestProton = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + str(mail))
    bodyResponse = requestProton.text

    protonmailaccountdoesnotexist = "info:1:0"
    protonmailaccountexists = "info:1:1"

    if protonmailaccountdoesnotexist in bodyResponse:
        print("\u001b[31m\n\nProtonMail account is NOT VALID")

    if protonmailaccountexists in bodyResponse:
        print("\033[1m\n\nProtonMail Account is VALID!!!\033[0m\U0001F4A5")


# Run a search on the Email address and check for Digital Footprints
def emailtraces():
    """
    BRAVO : Check Email Traces (Open Source) with Google Dork
    """

    print("\033[1m\u001b[32m\nCheck server status/\u001b[33m Verification statut du serveur:\u001b[32m\n")
    response = requests.get('https://google.com')
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')
    elif response.status_code == 404:
        print('Not Found.')

    searchfor = input(
        """\u001b[32mEnter Target Email in quotation marks!(Example:"admin@protonmail.com")\n\u001b[33mEntrez le Mail de la Cible dans des guillemets!:\u001b[32m """)
    print("\nProcessing request... \u001b[33mRecherche en cours...\u001b[32m\n")
    for result in search(searchfor, tld="com", num=200, stop=200, pause=2):
        print(result)


# Run a DarkWeb search on the email address
def darkwebtraces():
    """
    CHARLIE : Check Dark Web Email Traces
    """

    print("\033[1m\u001b[32m\nCheck server status\n\u001b[33mVerification statut du serveur:\u001b[32m\n")
    response = requests.get('https://ahmia.fi')
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')

    elif response.status_code == 404:
        print('Not Found.')

    choice = input(
        """\033[1mView results in Browser ("B") or Terminal ("T")?\n\u001b[33mVoir resultats dans Navigateur ("B") ou Terminal ("T")?\n\n\u001b[32mB/T: """)

    if choice == "B":
        darkwebbrowser()

    if choice == "T":
        darkwebterminal()


# Search with the Dark Web Browser opening automatically
def darkwebbrowser():
    """
    Dark Web Browser Open

    """
    query = input("""\nInput Target email or any query to search the Dark Web (example: darkmatterproject@protonmail.com)\n\u001b[33mMail de la cible\u001b[32m: """)
    webbrowser.open("https://ahmia.fi/search/?q=%s" % query)


# Search from Terminal with search results displayed within the terminal

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
	DELTA: Get the ProtonMail user PGP Key and information

	"""
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\nInput the ProtonMail user email address to get the user PGP Key \n\u001b[33mObtenir la cle PGP de la cible avec le mail ProtonMail\033[0m\u001b[32m\n")
    while invalidEmail:

        mail = input("\033[1mProtonMail User Email + Enter: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\u001b[31m\n\nProtonMail user does not exist\u001b[32m")
            invalidEmail = True

    requestProton = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + str(mail))
    bodyResponse = requestProton.text

    protonmailaccountdoesnotexist = "info:1:0"
    protonmailaccountexists = "info:1:1"

    if protonmailaccountdoesnotexist in bodyResponse:
        print("\u001b[31m\n\nProtonMail account is NOT VALID")

    if protonmailaccountexists in bodyResponse:
        print("\033[1m\nProtonMail Account PGP Key Found!!!\n \033[0m\u001b[32m")

        regexPattern1 = "2048:(.*)::"  # RSA 2048-bit (Older but faster)
        regexPattern2 = "4096:(.*)::"  # RSA 4096-bit (Secure but slow)
        regexPattern3 = "22::(.*)::"  # X25519 (Modern, fastest, secure)
        try:
            timestamp = int(re.search(regexPattern1, bodyResponse).group(1))
            dtObject = datetime.fromtimestamp(timestamp)
            print("\nPGP Key Date and Creation Time:", dtObject)
            print("Encryption Standard : RSA 2048-bit")
        except:
            try:
                timestamp = int(re.search(regexPattern2, bodyResponse).group(1))
                dtObject = datetime.fromtimestamp(timestamp)
                print("PGP Key Date and Creation Time:", dtObject)
                print("Encryption Standard : RSA 4096-bit ")
            except:
                timestamp = int(re.search(regexPattern3, bodyResponse).group(1))
                dtObject = datetime.fromtimestamp(timestamp)
                print("PGP Key Date and Creation Time:", dtObject)
                print("Encryption Standard : ECC Curve25519 ")

        # Get the USER PGP Key
        invalidResponse = True

        print("\033[1m\n\nGet User PGP Key? / \u001b[33mObtenir la cle PGP ?\033[1m\u001b[32m ")
        while invalidResponse:
            # Input
            responseFromUser = input("""\033[1m "\033[1mY"/"N":\033[0m """)
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


# Check if the user IP address belongs to ProtonVPN
def protonvpnipsearch():
    """
	ECHO : Find out if the IP address you have for the user makes him a ProtonVPN user
	"""

    while True:
        try:
            ip = ipaddress.ip_address(input(
                '\033[1m\n\nEnter Target IP address: (Example: "185.159.157.1")\n\u001b[33mAdresse IP de la Cible: \033[0m\u001b[32m '))
            break
        except ValueError:
            continue

    requestProton_vpn = requests.get('https://api.protonmail.ch/vpn/logicals')
    bodyResponse = requestProton_vpn.text
    if str(ip) in bodyResponse:
        print(
            "\033[1m\n\nThis IP belongs to a ProtonVPN user!!! \U0001F4A5 \U0001F4BB \n\u001b[33mCette adresse IP appartient a un utilisateur ProtonVPN!!! \U0001F4A5 \U0001F4BB  \033[0m\u001b[32m ")
    else:
        print(
            "\u001b[31m\033[1m\n\nThis IP address does not belong to ProtonVPN user \nCette adresse IP n'appartient pas a un utilisateur ProtonVPN\033[0m\u001b[32m ")


def main():
    printprot1ntelligencebanner()
    choice = input(
        """\033[1m\u001b[32mType "c" to check Proton API Status \n\033[1m\u001b[33mTapez "c" pour statut API ProtonMail: \033[0m\u001b[32m""")
    if choice == "c":
        checkprotonapistatus()
    choice = input("""\033[1m\u001b[32mView Modules? /\u001b[33m Voir Modules?\u001b[32m "Y" or "N":\033[0m\u001b[32m """)
    if choice == "Y":
        printprot1ntelligenceintro()

    while True:
        choice = input(
            """\033[1mMake Choice/\u001b[33mFaire un Choix\u001b[32m\033[1m - alpha | bravo | charlie | delta | echo :\033[0m\u001b[32m """)
        if choice == "alpha":
            protonmailaccountcheck()
        if choice == "bravo":
            emailtraces()
        if choice == "charlie":
            darkwebtraces()
        if choice == "delta":
            pgpkeyinformation()
        if choice == "echo":
            protonvpnipsearch()

        inp = input("\n\n\u001b[32m\033[1mContinue Y/N: ")
        if inp.lower() == 'n':
            break



if __name__ == '__main__':
    main()

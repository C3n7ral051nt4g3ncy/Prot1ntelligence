
<p align="center"> <img src="http://ForTheBadge.com/images/badges/made-with-python.svg"/>
<img src="http://ForTheBadge.com/images/badges/built-with-swag.svg">
  
<br>
<br>
  
<p align="center">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> 
<a href="https://github.com/C3n7ral051nt4g3ncy"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
<a href="https://ko-fi.com/tacticalintelanalyst"> <img alt="Kofi" src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white">
<a href="https://user-images.githubusercontent.com/104733166/171052611-1f76b07c-832f-4a4a-9a0a-2f94595c28c9.png"/><img alt="BTC" src="https://img.shields.io/badge/Bitcoin-000000?style=for-the-badge&logo=bitcoin&logoColor=white">

<p align="center">
<a href="https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence/blob/master/LICENSE"/> <img alt="Licence" src="https://img.shields.io/badge/LICENCE-MIT-brightgreen"> <br>
<br>  
<img src="https://img.shields.io/github/v/release/C3n7ral051nt4g3ncy/Prot1ntelligence?style=for-the-badge">

  
</p>
<br>
    
# PROTINTELLIGENCE 🕵🏻‍♂️
**ProtINTelligence** is a Python 🐍 script for the **OSINT &amp; Cyber Community**.<br>
I am currently working on finishing this tool soon so that it can check if a protonmail address exists and is valid, and then extract key type and creation date which may indicate the date the user created his protonmail account. (This depends whether the user created a new key or not)

# What can this tool do so far? 🔥
Protintelligence is currently working perfectly for checking any domain name to see if this domain uses protonmail to send and receive emails:
Input example: test@fornever.com
<br>
With the input above, this tool can:
   - Tell you if the custom domain uses Protonmail to send and receive emails
   - It will detect if the custom domain is using a **catch-all** and provide you with the main email address.
   - It will provide you with PGP key creation date and time (This is often the same date and time as account creation,as not many people change their keys)
   - It will tell you the Key Encryption Type: RSA (4096)	or ECC (Curve25519)

  
# Requirements 🐍
[Python 3](https://www.python.org/downloads/)<br>


# Installation ⚙️

```
git clone https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence
```

```
cd Prot1ntelligence
```

```
pip install -r requirements.txt
```

or (depending on pip version) 

```
pip3 install -r requirements.txt depending on your set-up.
```

```
python3 protintel.py
```

# Disclaimer ⚠️

`This tool is for the OSINT and Cyber community, don't use it for wrong, immoral, or illegal reasons. I am not responsible for any damage that you cause.`

# Tool Improvements 🔧
If you would like to change some code within the tool or if you have any suggestions, please submit your thoughts here on github or contact me via Twitter or Keybase:<br>
  
<a href="https://twitter.com/OSINT_Tactical"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/> <br>
  
<a href="https://keybase.io/osint_intel"><img src="https://img.shields.io/keybase/pgp/osint_intel?label=Keybase&logo=Keybase&logoColor=orange&style=for-the-badge"/>


# License ⚖️
[MIT](https://choosealicense.com/licenses/mit/)

  
# Thanks 🙏

Thanks to [Joe Gray](https://twitter.com/C_3PJoe) for his great courses and the knowledge he passed on to me.
  
Thanks to [White Hat Inspector](https://twitter.com/WHInspector) and [Justin Seitz](https://twitter.com/jms_dot_py) for their OSINT Automation with Python knowledge sharing.

  
 # Support 💗
This tool took me a good few weeks to make, if you like it and if it's useful for you, please feel free to make a donation for my work by clicking on the **KO-FI** Badge or the **BITCOIN** Badge at the top of this .README file, or simply scan the BTC QR Code to get my BTC Address. 
  
  
# Mention 📢
When I first made this script, I used 3 functions from [Protosint](https://github.com/pixelbubble/ProtOSINT)
- From version 2.1 (08/06/2023), I wiped everything and started making the script to be **100% my own code**.
- There may be some help from [Kr0wZ](https://github.com/Kr0wZ) in the coming weeks for the email validation function.

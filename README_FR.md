<p align="center"> <img src="http://ForTheBadge.com/images/badges/made-with-python.svg"/>
<img src="http://ForTheBadge.com/images/badges/built-with-swag.svg"> 
<br>
<br>
  
<p align="center">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> 
<a href="https://github.com/C3n7ral051nt4g3ncy)"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
<a href="https://ko-fi.com/tacticalintelanalyst"> <img alt="Kofi" src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white">
<a href="https://user-images.githubusercontent.com/104733166/171052611-1f76b07c-832f-4a4a-9a0a-2f94595c28c9.png"/> <img alt="BTC" src="https://img.shields.io/badge/Bitcoin-000000?style=for-the-badge&logo=bitcoin&logoColor=white">

<p align="center">
<a href="https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence/blob/master/LICENSE"/> <img alt="Licence" src="https://img.shields.io/badge/LICENCE-MIT-brightgreen">
</p>
<br>
    
# PROT1NTELLIGENCE 🕵🏻‍♂️
**Prot1ntelligence** est un script en Python 🐍 pour la **Communauté OSINT & CYBER**.<br>
En l'utilisant vous pourrez obtenir du RENS sur:
- Les Utilisateurs/Comptes ProtonMail
- Les Adresses IP ProtonVPN
- Les clés PGP des utilisateurs ProtonMail
- Les empreintes numériques laissés par les utilisateurs ProtonMail sur le Web et sur le Dark Net.
<br>

# Conditions pour Utilisation 🐍
[Python 3](https://www.python.org/downloads/)<br>

Assurez-vous d'avoir:
- Beautiful Soup (pip3 install beautifulsoup4)
- Requests (pip3 install requests)
- Google (pip3 install google)
<br>

# Prot1ntelligence video 🎬

Si vous souhaitez regarder la vidéo YouTube, assurez vous d'être sur un **PC** sinon ce sera dégueulasse de votre téléphone, mettre aussi les **paramètres de la vidéo sur 4K**.
  
<a href="https://youtu.be/Ufw1PEwfTLo" target="_blank">
 <img src="https://user-images.githubusercontent.com/104733166/173109191-89dcd8c1-0f87-4655-990e-582c9f59ca9e.png" alt="Watch the video" width="660" height="360" border="10" />
</a>

<br>
<br>

  
  
<br>
  
# Installation ⚙️

```
git clone https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence
cd Prot1ntelligence
pip install -r requirements.txt ou pip3 install -r requirements.txt selon votre set-up.

python3 prot1ntelligence.py
```

<br>
  
# Les Modules de Prot1ntelligence

<img width="133" src="https://user-images.githubusercontent.com/104733166/172962265-f2596b54-8405-42b9-b573-449d22dfcb5f.png"/>

  
### ALPHA 🔍
``` 
Le Module ALPHA confirme si un mail ProtonMail est VALIDE.
Cela fonctionne aussi pour les "custom domains" et les "catch-all"
Custom Domain= Compte Pro ProtonMail Entreprise (migration avec son propre nom de domaine)
Catch-all= Exemple: Je possède le nom de domaine "prot1ntelligence.fr", si j'active le catch-all, si une personne m'envoi un mail 
en mettant n'importe quels characteres avant le "@prot1ntelligence.fr", le mail arrivera quand même.
Exemple: La personne m'envoi un mail en mettant cette adresse: "ajzhehdo337@prot1ntelligence.fr", mail qui n'existe pas!
Mais avec le cactch-all, il arrivera dans ma boite: "contact@prot1ntelligence.fr"
```
### BRAVO 📡
``` 
Le Module BRAVO est une suite logique du Module ALPHA.
On a obtenu une confirmation que le mail de la cible est VALIDE.
Donc on peut maintenant utiliser BRAVO pour vérifier l'empreinte numérique laissée par la cible en source ouverte.
Mettez des guillemets pour faire un Dork et obtenir ainsi, un résultat exacte.
```
### CHARLIE 🏴
``` 
Le Module CHARLIE recherche des infos sur le mail de la cible sur le Dark Net
Rien ne vous oblige à renseigner que le mail de la cible...
N"importe quel terme sera accepté, de même que pour le module BRAVO.
``` 
### DELTA 🔑
``` 
Le Module DELTA vous donnera du renseignement sur la clé PGP de l'utilisateur ProtonMail
Date de création de la clé et le type de chiffrement utilisé 
Si la cible n'a pas générée de nouvelle clé PGP depuis la création du compte,la date correspond aussi à la création du compte. 
Vous pourrez aussi téléchargé la clé PGP de l'utilisateur et l'ajouter à votre KeyChain pour envoyer un mail chiffré à la cible.
```  
### ECHO 💻
``` 
Le Module ECHO confirme si l'adresse IP de la cible appartient à ProtonVPN.
Donc qui confirmerait que la cible est un utilisateur de ProtonVPN
```   
<br>
  
# Avertissement ⚠️

`Cet outil a été crée pour la communauté OSINT et Cyber, utilisez le pour la bonne cause et pas pour des choses illégales.`

<br>

# Améliorations du Tool 🔧
Si vous souhaitez apporter des suggestions ou modifs du code, n'hésitez pas, je suis joignable sur Twitter et KeyBase: <br>

<a href="https://twitter.com/OSINT_Tactical"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/> <br>
  
<a href="https://keybase.io/osint_intel"><img src="https://img.shields.io/keybase/pgp/osint_intel?label=Keybase&logo=Keybase&logoColor=orange&style=for-the-badge"/>
  
  

<br>

# Licence/Droits ⚖️
[MIT](https://choosealicense.com/licenses/mit/)
 
<br>
  
# Remerciements 🙏
  
Merci à [Joe Gray](https://twitter.com/C_3PJoe) pour son aide et ses formations de qualité.
  
Merci à [White Hat Inspector](https://twitter.com/WHInspector) et [Justin Seitz](https://twitter.com/jms_dot_py) pour leur savoir et leur partage sur l'Automatisation de l'OSINT avec Python.

Merci à mes coéquipiers des divers CTF de me soutenir dans mes projets et de supporter mes messages en pleine nuit 😴:[Cyberologue](https://twitter.com/Cyberologue_fr), [D0c_Kali](https://twitter.com/D0c_Kali), [fs0c131y](https://twitter.com/fs0c131y), [Gimli](https://twitter.com/BanPangar), [Mauraura](https://twitter.com/Mauraura4)
<br>
<br>
  
 # Soutien 💗
Ce tool m'a pris pas mal de temps et j'y ai passé quelques semaines...
Utilisateur de scripts Python depuis un moment déjà, mais jamais créateur.<br>
Alors si ce tool vous plait et que vous l'utilisez souvent, si vous souhaitez soutenir mon travail,
Vous pouvez cliquer sur le badge KO-FI en haut de ce fichier ou cliquer sur le badge BITCOIN pour envoyer un don en cryptomonnaies.

 # Sans oublie de mention 📢
Mea Culpa pour l'oublie de la mention pendant quelques heures après le début de la mise en ligne et merci à la communauté de m'avoir aidé. 
Le code n'est pas 100% à l'identique, mais pour mon premier script/projet Python (n'étant pas encore spécialiste Python), j'ai pris des idées et certains morceaux/fork de **PROTOSINT** de **Pixelbubble**. Protosint ne fonctionne plus pour certains modules et j'y ai ajouté mes propres modules qui me conviennent et je vais continuer à rajouter d'autres modules. Tous les projets sur GitHub en mode public sont en open source, le code aussi est en open source et publiquement accessible. Tout comme Protosint, Prot1ntelligence est sous licence MIT, libre à vous de forker et d'améliorer selon vos souhaits et besoins.
Voici le lien vers Protosint de Pixelbubble: https://github.com/pixelbubble/ProtOSINT

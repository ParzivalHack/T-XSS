# What is XSS?
Cross site scripting (XSS) is an attack in which an attacker injects malicious executable scripts into the code of a trusted application or website. 

# Tool info
T-XSS is a XSS vulnerability scanner written in Python.
This is how it works:
* Given a URL, it grabs all the HTML forms and then prints the number of forms detected.
* It then iterates all over the forms and submits the forms by putting the value of all text and search input fields with a Javascript code.
* If the Javascript code is injected and successfully executed, then this is a clear sign that the web page is XSS vulnerable.

# Installation of T-XSS
* apt update && apt upgrade
* pkg install python
* pkg install python2
* pkg install git
* pkg install toilet
* pkg install requests
* pkg install bs4
* git clone https://github.com/ParzivalHack/T-XSS

# Usage
* cd T-XSS
* chmod +x T-XSS.py
* python T-XSS.py

# Update
* cd T-XSS
* bash update.sh

# License
This tool is under the GPL v.3 License.

© 2022 Tommaso Bona


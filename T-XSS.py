import os
from email import contentmanager
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import colorama
os.system("clear")
os.system("toilet T-XSS")
print("Coded By: ParzivalHack")
print("Github: github.com/ParzivalHack")
print("License: The source code of this tool is under the GPL v.3 License.")
print("© 2022 Tommaso Bona")
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")
def get_form_details(form):
    details = {}
    action = form.attrs.get("action")import os
from email import contentmanager
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import colorama
os.system("clear")
os.system("toilet T-XSS")
print("Coded By: ParzivalHack")
print("Github: github.com/ParzivalHack")
print("License: The source code of this tool is under the GPL v.3 License.")
print("© 2022 Tommaso Bona")
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")
def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs =form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                data[input_name] = input_value
        if form_details["method"] == "post":
            return requests.post(target_url, data = data)
        else:
            return requests.get(target_url, params = data)
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('XSS vulnerable')</scripT>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details: ")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable
if __name__ == "__main__":
    url = str(input("Target URL: "))
    print(scan_xss(url))
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs =form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                data[input_name] = input_value
        if form_details["method"] == "post":
            return requests.post(target_url, data = data)
        else:
            return requests.get(target_url, params = data)
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('XSS vulnerable')</scripT>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details: ")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable
if __name__ == "__main__":
    url = str(input("Target URL: "))
    print(scan_xss(url))

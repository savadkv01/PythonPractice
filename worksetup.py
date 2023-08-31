#https://github.com/Arbazkhan4712
import webbrowser as wb

import os

def workauto():
    vscodepath = '"C:\\Program Files\\Microsoft VS Code\\Code.exe"'
    os.startfile(vscodepath)
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "stackoverflow.com", 
	    "github.com/savadkv01", 
	    "gmail.com",
	    "google.com",
	    "youtube.com"
    )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)
workauto()
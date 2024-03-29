#!/usr/bin/python3

import requests; from os import path; import argparse; import sys; import signal

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

def sig_handler(sig, frame):
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-w","--wordlist")
args = parser.parse_args()

target = args.target
wordlist = args.wordlist

def start():
    global wordlist
    if target and wordlist:
        if path.exists(wordlist):
            wordlist = open(wordlist, "r")
            wordlist = wordlist.read().split("\n")
        else:
            print(f"{redColour}The dictionary does not exist{resetColour}")
            sys.exit(1)

        with open("subdomainsFound.txt", "a") as output:     
            for subdomain in wordlist:
                url = "http://"+ subdomain+"."+target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass    
                else:
                    print(f"{greenColour}[+]{resetColour} Subdomain found: "+ url)
                    output.write(url + "\n")

        with open("subdomainsFound.txt", "a") as output:
            for subdomain in wordlist:
                url = "https://"+ subdomain+"."+target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass    
                else:
                    print(f"{greenColour}[+]{resetColour} Subdomain found: "+ url)
                    output.write(url + "\n")
    else:
        sys.exit(1)

start()


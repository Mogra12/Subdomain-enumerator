from colorama import Fore
from os.path import exists
from random import randint

reset = Fore.RESET
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX

def report(response_200, response_301, response_403, savefile):
    if not savefile:
        if len(response_200) > 0:
            print(f"<========={green}Status 200{reset}=========>")
            for url200 in response_200:
                print(f" - {green}{url200}{reset}")
            print("<============================>")
        elif len(response_301) > 0:
            print(f"<========={yellow}Status 301{reset}=========>")
            for url301 in response_301:
                print(f" - {yellow}{url301}{reset}")
            print("<============================>")
        elif len(response_403) > 0:
            print(f"<========={yellow}Status 403{reset}=========>")
            for url403 in response_403:
                print(f" - {yellow}{url403}{reset}")
            print("<============================>")
    else:
        report_path = "report_urls.txt"
        if exists("report_urls.txt"):
            report_path = f"report_urls{randint(1,101)}.txt"
        try:
            with open(report_path, "w") as file:
                if len(response_200) > 0:
                    file.write("<=========Status 200=========>\n")
                    for url200 in response_200:
                        file.write(f" - {url200}\n")
                    file.write("<============================>\n")
                if len(response_301) > 0:
                    file.write("<========={Status 301}=========>\n")
                    for url301 in response_301:
                        file.write(f" - {url301}\n")
                    file.write("<============================>\n")
                if len(response_403) > 0:
                    file.write("<========={Status 403}=========>\n")
                    for url403 in response_403:
                        file.write(f" - {url403}\n")
                    file.write("<============================>\n")
                print(f"{green}\nReport File Created!{reset}")
        except Exception as e:
            print(f"Error {e}")
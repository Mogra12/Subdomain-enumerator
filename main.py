import requests as req
import argparse
from colorama import Fore
from modules.report import report

class Enum:
    def __init__(self):
        # Init Parser   
        self.parser = argparse.ArgumentParser(description="CLI Subdomain Enumerator")
        
        # CLI Colors
        self.reset = Fore.RESET
        self.green = Fore.LIGHTGREEN_EX
        self.red = Fore.LIGHTRED_EX
        self.yellow = Fore.LIGHTYELLOW_EX
        
    def args(self):
        # CLI Commands
        self.parser.add_argument("-d", "--domain", type=str, help="Defines Domain", required=True)
        self.parser.add_argument("-w", "--wordlist", type=str, help="Defines Wordlist path", required=True)
        self.parser.add_argument("-sf", "--savefile", type=bool, help="Creates an file with URLs")
        self.args = self.parser.parse_args()
    
    def run(self):
        response_200, response_301, response_403 = [], [], []
        try:
            if self.args.wordlist:
                with open(self.args.wordlist, 'r') as file:
                    content = file.read().splitlines()
                    print("Scanning...\n")  
                    for subdomain in content:
                        if subdomain != "":
                            subdomain = subdomain.strip()
                            protocol = "https://" if self.args.domain.startswith("https://") else "http://"
                            url = f"{protocol}{subdomain}.{self.args.domain}"
                            
                            self.args.domain = self.args.domain.replace("https://", "").replace("http://", "").strip("/")
                            try: 
                                response = req.get(url, timeout=5)
                                if response.status_code == 200:
                                    response_200.append(url)
                                    print(f"{self.green}[ + ] {url} - 200{self.reset}")
                                elif response.status_code == 301:
                                    response_301.append(url)
                                    print(f"{self.yellow}[ - ] {url} - 301{self.reset}")
                                elif response.status_code == 403:
                                    response_403.append(url)
                                    print(f"{self.yellow}[ - ] {url} - 403{self.reset}")
                            except req.exceptions.RequestException:
                                print(f"{self.red}[ ! ] Failed to connect: {url}{self.reset}")
                                
                    if not self.args.savefile:
                        report(response_200, response_301, response_403, False)
                    else:
                        report(response_200, response_301, response_403, True)

        except KeyboardInterrupt:
            print("\nProgram interrupted")
                
if __name__ == "__main__":
    enum = Enum()
    enum.args()
    enum.run()
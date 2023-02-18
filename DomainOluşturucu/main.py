import requests, itertools
from colorama import Fore, init, Style
import os

init(autoreset=True)

class DomainNameGenerator(object):
    def __init__(self) -> None:
        self.domainsName = []
        try:
            os.mkdir("Domains")
        except FileExistsError:
            ...
        self.path = os.sep
        self.banner()
        self.word = str(input("[-] Kelime Giriniz : "))
        
    def banner(self):
        print(Fore.BLUE+r"""
              
                       ______
                      /\     \
                     /  \     \
                    /    \_____\
                   _\    / ____/_
                  /\ \  / /\     \
                 /  \ \/_/  \     \
                /    \__/    \_____\
               _\    /  \    / ____/_
              /\ \  /    \  / /\     \
             /  \ \/_____/\/_/  \     \
            /    \_____\    /    \_____\
           _\    /     /    \    / ____/_
          /\ \  /     /      \  / /\     \
         /  \ \/_____/        \/_/  \     \
        /    \_____\            /    \_____\
       _\    /     /            \    / ____/_
      /\ \  /     /              \  / /\     \
     /  \ \/_____/                \/_/  \     \ --Domain Generator
    /    \_____\                    /    \_____\
   _\    /     /_  ______  ______  _\____/ ____/_
  /\ \  /     /  \/\     \/\     \/\     \/\     \
 /  \ \/_____/    \ \     \ \     \ \     \ \     \
/    \_____\ \_____\ \_____\ \_____\ \_____\ \_____\
\    /     / /     / /     / /     / /     / /     /
 \  /     / /     / /     / /     / /     / /     /
  \/_____/\/_____/\/_____/\/_____/\/_____/\/_____/             
              



""")
        
        
    def Generator(self,prefix:str, suffixes:str):
        for prefix, suffix in itertools.product(prefix, suffixes):
            domain = f"{prefix.strip()}{self.word}{suffix.strip()}"
            self.domainsName.append(domain)
            
        return self.domainsName
    
    def readPrefix(self):
        return open(
            "prefix.txt",
            mode="r",
            encoding="utf-8"
        ).readlines()
        
    def readSuffixes(self):
        return open(
            "suffixes.txt",
            mode="r",
            encoding="utf-8"
        ).readlines()
        
        
    def domainNames(self):
        domains = (self.Generator(prefix=self.readPrefix(), suffixes=self.readSuffixes()))
        return domains

    
    def https(self):
        with open(f"Domains{self.path}domainsHttps.txt", mode="w+", encoding="utf-8") as file:
            for domain in self.domainNames():
                url = f"https://www.{domain}"
                try:
                    __requests = (requests.get(url))
                    if __requests.status_code == 200:
                        print(Fore.GREEN+"Found : ", Fore.WHITE+url, Fore.BLUE+ str(__requests.status_code))
                        file.write(__requests.url+"\n")
                except Exception:
                    print(Fore.RED+"Not Found : ", Fore.WHITE+url)
                    
                
                    
                
    def http(self):
        with open(f"Domains{self.path}domainsHttp.txt", mode="w+", encoding="utf-8") as file:
            for domain in self.domainNames():
                url = f"http://www.{domain}"
                try:
                    __requests = (requests.get(url))
                    if __requests.status_code == 200:
                        print(Fore.GREEN+"Found : ", Fore.WHITE+url, Fore.BLUE+ str(__requests.status_code))
                        
                        file.write(__requests.url+"\n")
                except Exception:
                    
                    print(Fore.RED+"Not Found : ", Fore.WHITE+url)
                    
        
    def https_(self):
        with open(f"Domains{self.path}domains.txt", mode="w+", encoding="utf-8") as file:
            for domain in self.domainNames():
                url = f"https://{domain}"
                try:
                    __requests = (requests.get(url))
                    if __requests.status_code == 200:
                        print(Fore.GREEN+"Found : ", Fore.WHITE+url, Fore.BLUE+ str(__requests.status_code))
                        file.write(__requests.url+"\n")
                except Exception:
                    
                    print(Fore.RED+"Not Found : ", Fore.WHITE+url)
                    
                    
  
       
        
        
        
    
if __name__ == "__main__":
    app = DomainNameGenerator()
    (app.https())
    app.https_()
    app.http()
  
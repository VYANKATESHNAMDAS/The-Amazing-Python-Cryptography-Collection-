import os
from setup import colors
logo = f"""

██████  ██       █████  ██    ██ ███████  █████  ██ ██████       ██████ ██ ██████  ██   ██ ███████ ██████  
██   ██ ██      ██   ██  ██  ██  ██      ██   ██ ██ ██   ██     ██      ██ ██   ██ ██   ██ ██      ██   ██ 
██████  ██      ███████   ████   █████   ███████ ██ ██████      ██      ██ ██████  ███████ █████   ██████  
██      ██      ██   ██    ██    ██      ██   ██ ██ ██   ██     ██      ██ ██      ██   ██ ██      ██   ██ 
██      ███████ ██   ██    ██    ██      ██   ██ ██ ██   ██      ██████ ██ ██      ██   ██ ███████ ██   ██ 
                                                                                                           
                                                                                                           

                                            
            

"""
from colorama import Fore,Style
c = colors
def banner():
    os.system("cls")
    print(c.ran + logo)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "» " * 4, " [+] LinkedIn: https://linkedin.com/in/vyankateshnamdas/ ", "» " * 4 + c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "» " * 4, " [+] Github: https://github.com/VYANKATESHNAMDAS/ ", "» " * 3+c.ran + "|")
    print("                        ")
    print(c.ran + '»' * 78)

def banner2():
    clear()
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "» " * 4, " [+] LinkedIn: https://linkedin.com/in/vyankateshnamdas/ ", "» " * 4 + c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "» " * 4, " [+] Github: https://github.com/VYANKATESHNAMDAS/ ", "» " * 3+c.ran + "|")
    print("                        ")
    print(c.ran + '»' * 78)

def clear():
    os.system("clear")

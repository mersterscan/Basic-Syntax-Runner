from os import system as RunCommand

try:
    from colorama import Fore as TextColor
except:
    RunCommand("pip3 install colorama")
    from colorama import Fore as TextColor

#<--------------------------------->#

RunCommand("cls" or "clear")

while True:
        
    Dastur = input(TextColor.LIGHTMAGENTA_EX + f"System@User -> {TextColor.LIGHTGREEN_EX}")
    
    RunCommand(Dastur)
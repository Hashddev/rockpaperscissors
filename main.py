import random

print("""
██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")


# Functions

def hidden():
  print("""
  
█▄█ █▀█ █░█   █▀▀ █▀█ █░█ █▄░█ █▀▄   █▀█ █░█ █▀█   █▀▀ ▄▀█ █▀ ▀█▀ █▀▀ █▀█   █▀▀ █▀▀ █▀▀
░█░ █▄█ █▄█   █▀░ █▄█ █▄█ █░▀█ █▄▀   █▄█ █▄█ █▀▄   ██▄ █▀█ ▄█ ░█░ ██▄ █▀▄   ██▄ █▄█ █▄█
  """)

def htpfunct():
  print("__How to play__\n\nTo play all you need is this software and no friends. Just simply use numbers to navigate through the menus and have fun! Thanks for playing!\n\n-N33dJe5u5 and Justkiddinglol0")
  htp_menu = input("Want to go back?[Y]es: ")
  print("\n")
  if htp_menu == 'y' or 'Y':
    welcomefunct()

def creditfunct():
  print("__Credits__\n\nCode by N33dJe5u5\n\nCoordinated by Justkiddinglol0")
  credit_menu = input("\nWant to go back?[Y]es: ")
  if credit_menu == 'y' or 'Y':
    welcomefunct()

# Game Variables
t = "Tie!"
l = "You Lost!"
w = "You Won!"
end_sentence = "Press 'e' or 'E' to start again, and 'x' or 'X' to quit:"
r = "Rock"
p = "paper"
s = "Scissors"

def gamefunct():
  rpsList = ["Rock","Paper","Scissors"]
  cmp_choice = random.choice(rpsList)
  print("\n__Rock Paper Scissors__\n\n1) Rock\n2) Paper\n3) Scissors\n4) exit")
  game = int(input("What is your choice?(int): "))
  if game == 1:
    if cmp_choice == "Rock":
      print("\n" + t)
    elif cmp_choice == "Paper":
      print("\n" + l)
    elif cmp_choice == "Scissors":
      print("\n" + w)
  elif game == 2:
    if cmp_choice == "Rock":
      print("\n" + w)
    elif cmp_choice == "Paper": 
      print("\n" + t)
    elif cmp_choice == "Scissors":
      print("\n" + l)
  elif game == 3:
    if cmp_choice == "Rock":
      print("\n" + l)
    elif cmp_choice == "Paper": 
      print("\n" + w)  
    elif cmp_choice == "Scissors":
      print("\n" + t)
  game_choice = input(end_sentence + "")
  if game_choice == "e" or "E":
    gamefunct()
  elif game_choice == "x" or "X":
    welcomefunct()


def welcomefunct():
  print("\n__Main Menu__\n\n1) Start game\n2) How to play\n3) Credits")
  welcome = int(input("What is your choice?(int): "))
  if welcome == 1:
    gamefunct()
  elif welcome == 2:
    htpfunct()
  elif welcome == 3:
    creditfunct()
  elif welcome == 4:
    hidden()
  
welcomefunct()
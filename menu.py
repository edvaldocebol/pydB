from function import functions as fun
from varConst import varConst as V
import colorama as color
import time


fun.loading()


def menuIni():
    fun.limpaC()

    fun.logo(color.Fore.RED+'██▓█   ████   ▄████▄   ▒█████   ██▀███   ▄▄▄     ▄▄▄█████▓')
    fun.logo('▓██▒██  ▓██▒  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒█████▄  ▓  ██▒ ▓▒')
    fun.logo('▒██▒▐██▌▒██▒  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒██▒ ▄██ ▒ ▓██░ ▒░')
    fun.logo('░██░▒██▓░██░  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██░█▀   ▒ ▓██▓ ░')
    fun.logo('░██░▒██▓░██░  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▓█  ▀█▓  ░▒██▒ ░')
    fun.logo('░▓  ▒▒▓▒░▓    ░ ░▒ ▒  ░░ ▒░▒░▒░░ ▒▓ ░▒▓░░▒▓███▀▒  ░▒▓▒ ░')
    fun.logo('▒ ░░▒ ░▒▒    ░ ░  ▒     ░ ▒ ▒░  ░▒ ░ ▒░▒░▒   ░  ░░▒  ░')
    fun.logo('▒ ░░░  ░░ ▒   ░        ░ ░ ░ ▒   ░░   ░ ░    ░   ░  ░')
    fun.logo('░  ░  ░   ░   ░ ░          ░ ░    ░     ░          ░')

    print(color.Fore.BLUE+'===================')
    print(color.Fore.RED+'| [1] teste       |')
    print(color.Fore.RED+'| [2] VOLTAR      |')
    print(color.Fore.BLUE+'===================')
    fun.maquina_de_escrever(V.texto2)
    op = input(color.Fore.WHITE+'')
    if op =='2':
        fun.limpaC()
        MenuP()

def MenuP():

   fun.logo(color.Fore.GREEN+'███████╗██╗   ██╗███████╗███████╗██╗    ██╗')
   fun.logo('██╔════╝██║   ██║██╔════╝██╔════╝██║    ██║')
   fun.logo('██║     ██║   ██║███████╗██████╗ ██║ █╗ ██║')
   fun.logo('██║     ██║   ██║╚════██║██╔══██╗██║███╗██║')
   fun.logo('╚██████╗╚██████╔╝███████║██████╔╝╚███╔███╔╝')
   fun.logo(' ╚═════╝ ╚═════╝ ╚══════╝╚═════╝  ╚══╝╚══╝')

   print(color.Fore.BLUE+'|======================|')
   print(color.Fore.RED+'| [1] INICIAR          |')
   print(color.Fore.RED+'| [2] OPÇÃO            |')
   print(color.Fore.RED+'| [3] SOBRE            |')
   print(color.Fore.RED+'| [4] SAIR             |')
   print(color.Fore.BLUE+'|======================|')


   fun.maquina_de_escrever(V.texto)

   opcao = input()
   if opcao == '1':
      menuIni()
   elif opcao == '2':
      print('OLA')
   elif opcao == '3':
      fun.maquina_de_escrever(color.Fore.WHITE+V.cop)
      fun.maquina_de_escrever(V.insta)
   elif opcao == '4':
      fun.maquina_de_escrever(V.adeus)

MenuP()



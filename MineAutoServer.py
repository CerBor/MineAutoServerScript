#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
CerBor's script minecraft start script
"""

import os
import sys
import platform
from time import sleep as stop
try:
    from fuzzywuzzy import fuzz
except ModuleNotFoundError:
    print ("Error: you haven\'t got \'fuzzywuzzy\' library. Please install it!")
    os.system("PAUSE")
haveColorama: bool
try:
    from colorama import init, Fore, Style
    haveColorama = True
except ModuleNotFoundError:
    haveColorama = False
    print ("Note: you don\'t have got \'colorama\' library. If you want to see colored text, install it.")

try:
    def sleep(time: float):
        """
        This method works like time.sleep(), but it works only if variable 'canSleeped' == true
        """
        global canSleeped

        if (canSleeped):
            stop(time)
        else:
            pass

    # If we on windows, delete print commands
    if (platform.system() == "Windows"):
        os.system("@echo off")

    # Testing, are we in pyinstaller or not
    if (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
        pass
    else:
        print ("[BETA] MineAutoServer by CerBor")

    # Set information about me
    __author__ = "CerBor"
    __license__ = "MIT"

    __version__ = "1.0.1"
    __maintainer__ = "CerBor"
    __status__ = "Development"

    # And set variables (canSleeped)
    canSleeped: bool = True

    # * Read server.properties
    try:
        properties = open("server.properties", 'r')
    except FileNotFoundError:
        if (haveColorama):
            print (Fore.YELLOW + "Warring: file \"server.properties is not found\"" + Fore.RESET)
        else:
            print ("Warring: file \"server.properties is not found\"")
        sleep (0.5)
        print ("Generating new...")
        sleep (0.1)

        with open("server.properties", 'w') as prop:
            prop.writelines("allow-flight=false\nallow-nether=true\nbroadcast-console-to-ops=true\nbroadcast-rcon-to-ops=true\ndifficulty=easy\nenable-command-block=false\nenable-jmx-monitoring=false\nenable-query=false\nenable-rcon=false\nenable-status=true\nenforce-whitelist=false\nentity-broadcast-range-percentage=100\nforce-gamemode=false\nfunction-permission-level=2\ngamemode=survival\ngenerate-structures=true\ngenerator-settings=\nhardcore=false\nmax-players=30\nmax-tick-time=60000\nmax-world-size=29999984\nmotd=A Forge Minecraft Server\nnetwork-compression-threshold=256\nonline-mode=true\nop-permission-level=4\nplayer-idle-timeout=0\nprevent-proxy-connections=false\npvp=true\nquery.port=25565\nrate-limit=0\nrcon.password=\nrcon.port=25575\nresource-pack=\nresource-pack-sha1=\nserver-ip=\nserver-port=25565\nsnooper-enabled=true\nspawn-animals=true\nspawn-monsters=true\nspawn-npcs=true\nspawn-protection=16\nsync-chunk-writes=true\ntext-filtering-config=\nuse-native-transport=true\nview-distance=10\nwhite-list=false")
        
        print ("Generating completed!")
        properties = open("server.properties", 'r')
    properties_value = properties.readlines()

    def printStartMessage():
        """
        Print start message
        """
        if (haveColorama):
            init ()
            print (Fore.LIGHTCYAN_EX + "######################################################" + Fore.RESET)
            print (Fore.LIGHTCYAN_EX + "##          " + Fore.YELLOW + Style.BRIGHT + "CerBor\'s " + Style.RESET_ALL + Fore.CYAN + "MineAutoServer script" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "          ##" + Fore.RESET)
            print (Fore.LIGHTCYAN_EX + "######################################################" + Fore.RESET)
        else:
            print ("######################################################")
            print ("##       CerBor\'s python MineAutoServer script      ##")
            print ("######################################################")

    def checkMaxPlayers():
        """
        Check max players, is it very big or very small or it isn't int
        """
        global maxPlayers, maxPlayersValue

        try:
            maxPlayersValue = int(maxPlayers)

            if (maxPlayersValue <= 0):
                if (haveColorama):
                    sys.stdout.write (Fore.RED + "Very small size!" + Fore.RESET)
                else:
                    sys.stdout.write ("Very small size!")

                maxPlayers = input ("\n- ")
                checkMaxPlayers()
            elif (maxPlayersValue >= 1000000):
                if (haveColorama):
                    sys.stdout.write (Fore.RED + "Very big size!" + Fore.RESET)
                else:
                    sys.stdout.write ("Very big size!")

                maxPlayers = input("\n- ")
                checkMaxPlayers()
            else:
                if (haveColorama):
                    sys.stdout.write ("Max players set to " + Fore.LIGHTYELLOW_EX + str(maxPlayersValue) + Fore.RESET)
                else:
                    sys.stdout.write ("Max players set to " + str(maxPlayersValue))

                # Change max-players value
                for index, item in enumerate(properties_value, start=0):
                    if (item.startswith('max-players')):
                        properties_value[index] = "max-players={}\n".format(maxPlayersValue)

                # And apply changes to file
                with open('server.properties', 'w') as write:
                    write.writelines(properties_value)
        except ValueError:
            if (maxPlayers == ""):
                maxPlayersValue = 20
                if (haveColorama):
                    sys.stdout.write ("Max players set to " + Fore.LIGHTYELLOW_EX + "20" + Fore.RESET)
                else:
                    sys.stdout.write ("Max players set to 20")

                # Change max-players value
                for index, item in enumerate(properties_value, start=0):
                    if (item.startswith('max-players')):
                        properties_value[index] = "max-players={}\n".format(maxPlayersValue)

                # And apply changes to file
                with open('server.properties', 'w') as write:
                    write.writelines(properties_value)
            else:
                if (haveColorama):
                    sys.stdout.write (Fore.RED + "Please, write max players value in integer" + Fore.RESET)
                else:
                    sys.stdout.write ("Please, write max players value in integer")

                maxPlayers = input("\n- ")
                checkMaxPlayers()

    def checkRamSize(ram_value):
        """
        Check, is RAM very big or very small or it isn't int
        """
        global haveColorama, ram_size, ram

        try:
            ram_value = int(ram_value)

            if (ram_value <= 0):
                if (haveColorama):
                    sys.stdout.write (Fore.RED)
                print ("Very small size!")
                if (haveColorama):
                    sys.stdout.write (Fore.RESET)

                ram = input("- ")
                checkRamSize(ram)
            elif (ram_value >= 100000):
                if (haveColorama):
                    sys.stdout.write (Fore.RED)
                print ("Very big size!!!")
                if (haveColorama):
                    sys.stdout.write (Fore.RESET)

                ram = input("- ")
                checkRamSize(ram)
            else:
                ram_size = int(ram)

                if (haveColorama):
                    sys.stdout.write ("RAM set to " + Fore.LIGHTYELLOW_EX + str(ram_size) + Fore.RESET + " mb")
                else:
                    sys.stdout.write ("RAM set to " + str(ram_size) + " mb")
        except ValueError:
            if (ram == ""):
                ram_size = 2000
                if (haveColorama):
                    sys.stdout.write ("RAM set to " + Fore.LIGHTYELLOW_EX + "2000" + Fore.RESET + " mb")
                else:
                    sys.stdout.write ("RAM set to 2000 mb")
            else:
                if (haveColorama):
                    print (Fore.RED + "Please, write ram in integer" + Fore.RESET)
                else:
                    print ("Please, write ram in integer")
                
                ram = input("- ")
                checkRamSize(ram)

    def checkLicense():
        """
        Check license, is it True or False or null string
        """
        global isLicense, isLicenseValue, properties_value, haveColorama
        
        try:
            if int(isLicense):
                if (haveColorama):
                    sys.stdout.write (Fore.RED)
                print ("Please, write yes or no")
                if (haveColorama):
                    sys.stdout.write (Fore.RESET)
                isLicense = input("- ")
                checkLicense()
        except ValueError:
            if (isLicense.lower() == "yes" or fuzz.ratio('yes', isLicense) > 80):
                isLicenseValue = True
                if (haveColorama):
                    sys.stdout.write (Fore.LIGHTGREEN_EX + "Now players must have license to join your server" + Fore.RESET)
                else:
                    sys.stdout.write ("Noew players must have license to join your server")

                # Change online-mode value
                for index, item in enumerate(properties_value, start=0):
                    if (item.startswith('online-mode')):
                        properties_value[index] = "online-mode=true\n"

                # And apply changes to file
                with open('server.properties', 'w') as write:
                    write.writelines(properties_value)

            elif (isLicense.lower() == "no" or fuzz.ratio('no', isLicense) > 80):
                isLicenseValue = False
                if (haveColorama):
                    sys.stdout.write (Fore.LIGHTRED_EX + "Now players don't need to have license to join your server" + Fore.RESET)
                else:
                    sys.stdout.write ("Now players don't need to have license to join your server")

                # Change online-mode value
                for index, item in enumerate(properties_value, start=0):
                    if (item.startswith('online-mode')):
                        properties_value[index] = "online-mode=false\n"

                # And apply changes to file
                with open('server.properties', 'w') as write:
                    write.writelines(properties_value)

            elif (isLicense == ""):
                isLicenseValue = False
                if (haveColorama):
                    sys.stdout.write (Fore.LIGHTGREEN_EX + "Now players must have license to join your server" + Fore.RESET)
                else:
                    sys.stdout.write ("Now players must have license to join your server")

                # Change online-mode
                for index, item in enumerate(properties_value, start=0):
                    if (item.startswith('online-mode=')):
                        properties_value[index] = "online-mode=false\n"

                # And apply changes to file
                with open('server.properties', 'w') as write:
                    write.writelines(properties_value)
            else:
                if (haveColorama):
                    sys.stdout.write (Fore.RED + "Please, write yes or no" + Fore.RESET)
                else:
                    sys.stdout.write ("Please, write yes or no")
            
                isLicense = input("\n- ")
                checkLicense()

    def checkDescription():
        """
        Check description, and if it's null or idk set it to default motd
        """
        global motd, motd_value, haveColorama

        # (idk is easter egg)
        if (motd_value == "" or fuzz.ratio("idk", motd_value.lower()) > 80):
            motd_value = "A Minecraft Server"

        # Change motd
        for index, item in enumerate(properties_value, start=0):
            if (item.startswith('motd=')):
                properties_value[index] = "motd={0}\n".format(motd_value)

        # And apply changes to file
        with open('server.properties', 'w') as write:
            write.writelines(properties_value)

        if (haveColorama):
            sys.stdout.write ("Description set to \"" + Fore.LIGHTYELLOW_EX + motd_value + Fore.RESET + "\"")
        else:
            sys.stdout.write ("Description set to \"" + motd_value + "\"")

    def checkGamemode():
        """
        Check gamemode value, is it survival, adventure, creative or spectator
        """
        global gamemode, gamemode_value, haveColorama

        if (gamemode == "" or gamemode.lower() == "survival" or fuzz.ratio("survival", gamemode.lower()) > 80):
            gamemode_value = "survival"
            if (haveColorama):
                sys.stdout.write ("Gamemode set to " + Fore.RED + "survival" + Fore.RESET)
            else:
                sys.stdout.write ("Gamemode set to survival")

            # Change gamemode value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('gamemode=')):
                    properties_value[index] = "gamemode=survival\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (gamemode.lower() == "creative" or fuzz.ratio("creative", gamemode.lower()) > 80):
            gamemode_value = "creative"
            if (haveColorama):
                sys.stdout.write ("Gamemode set to " + Fore.LIGHTYELLOW_EX + "creative" + Fore.RESET)
            else:
                sys.stdout.write ("Gamemode set to creative")

            # Change gamemode value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('gamemode=')):
                    properties_value[index] = "gamemode=creative\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (gamemode.lower() == "adventure" or fuzz.ratio("adventute", gamemode.lower()) > 80):
            gamemode_value = "adventure"
            if (haveColorama):
                sys.stdout.write ("Gamemode set to " + Fore.RED + "adventure" + Fore.RESET)
            else:
                sys.stdout.write ("Gamemode set to adventure")

            # Change gamemode value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('gamemode=')):
                    properties_value[index] = "gamemode=adventure\n"

        # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (gamemode.lower() == "spectator" or fuzz.ratio("spectator", gamemode.lower()) > 80):
            gamemode_value = "spectator"
            if (haveColorama):
                sys.stdout.write ("Gamemode set to " + Fore.RED + "spectator" + Fore.RESET)
            else:
                sys.stdout.write ("Gamemode set to spectator")

            # Change gamemode value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('gamemode=')):
                    properties_value[index] = "gamemode=spectator\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)

        else:
            if (haveColorama):
                sys.stdout.write (Fore.RED + "Please, write gamemode (survival, creative, adventure, spectator)" + Fore.RESET)
            else:
                sys.stdout.write ("Please, write gamemode (survival, creative, adventure, spectator)")

            gamemode = input ("\n- ")
            checkGamemode()

    def checkDifficulty():
        """
        Check difficulty, is it peaceful, easy, normal, hard or hardcore
        """
        global difficulty, difficulty_value, haveColorama

        if (difficulty.lower() == "peaceful" or fuzz.ratio("peaceful", difficulty.lower()) > 80):
            difficulty_value = "peaceful"
            if (haveColorama):
                print ("Difficulty set to " + Fore.LIGHTGREEN_EX + "peaceful" + Fore.RESET)
            else:
                print ("Difficulty set to peaceful")

            # Change difficulty value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('difficulty=')):
                    properties_value[index] = "difficulty=peaceful\n"
                if (item.startswith('hardcore')):
                    properties_value[index] = "hardcore=false\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (difficulty == "" or difficulty.lower() == "easy" or fuzz.ratio("easy", difficulty.lower()) > 80):
            difficulty_value = "easy"
            if (haveColorama):
                print ("Difficulty set to " + Fore.GREEN + "easy" + Fore.RESET)
            else:
                print ("Difficulty set to easy")

            # Change difficulty value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('difficulty=')):
                    properties_value[index] = "difficulty=easy\n"
                if (item.startswith('hardcore')):
                    properties_value[index] = "hardcore=false\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (difficulty.lower() == "normal" or fuzz.ratio("normal", difficulty.lower()) > 80):
            difficulty_value = "normal"
            if (haveColorama):
                print ("Difficulty set to " + Fore.YELLOW + "normal" + Fore.RESET)
            else:
                print ("Difficulty set to normal")

            # Change difficulty value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('difficulty=')):
                    properties_value[index] = "difficulty=normal\n"
                if (item.startswith('hardcore')):
                    properties_value[index] = "hardcore=false\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (difficulty.lower() == "hard" or fuzz.ratio("hard", difficulty.lower()) > 80):
            difficulty_value = "hard"
            if (haveColorama):
                print ("Difficulty set to " + Style.DIM + Fore.YELLOW + "hard" + Style.RESET_ALL)
            else:
                print ("Difficulty set to hard")

            # Change difficulty value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('difficulty=')):
                    properties_value[index] = "difficulty=hard\n"
                if (item.startswith('hardcore')):
                    properties_value[index] = "hardcore=false\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        elif (difficulty.lower() == "hardcore" or fuzz.ratio("hardcore", difficulty.lower()) > 80):
            difficulty_value = "hardcore"
            if (haveColorama):
                print ("Difficulty set to " + Fore.RED + "hardcore" + Fore.RESET)
            else:
                print ("Difficulty set to hardcore")

            # Change difficulty value
            for index, item in enumerate(properties_value, start=0):
                if (item.startswith('hardcore=')):
                    properties_value[index] = "hardcore=true\n"

            # And apply changes to file
            with open('server.properties', 'w') as write:
                write.writelines(properties_value)
        else:
            if (haveColorama):
                sys.stdout.write ("Please, write difficulty of your server ({peaceful}peaceful{reset}, {easy}easy{reset}, {normal}normal{reset}, {hard}hard{reset} or {hardcore}hardcore{reset})".format(peaceful=Fore.LIGHTGREEN_EX, easy=Fore.GREEN, normal=Fore.YELLOW, hard=Style.DIM + Fore.YELLOW, hardcore=Fore.RED, reset=Style.RESET_ALL))
            else:
                sys.stdout.write ("Please, write difficulty of your server (peaceful, easy, normal, hard or hardcore)")
            
            difficulty = input ("\n- ")
            checkDifficulty()

    def createServerStartFile():
        """
        Create start.bat file with user ram
        """
        global ram_size

        print ("Creating bat start server file...")
        with open('start.bat', 'w') as startFile:
            startFile.write("@rem --------------------------------\n")
            startFile.write("@rem Auto-created server start file\n")
            startFile.write("@rem          (RAM: {ram}m)\n".format(ram=ram_size))
            startFile.write("@rem --------------------------------\n")
            startFile.write("@echo off\n")
            startFile.write("java -Xmx{ram}M -Xms{ram}M -jar server.jar nogui\n".format(ram=ram_size))
            startFile.write("echo Server stopped\n")
            startFile.write("PAUSE")
        print ("Completed!")

    def printBr():
        """
        Print \\n symbol
        """
        print ("\n")

    printStartMessage()
    ram = input("What ram are you need (in mb)?\n- ")
    ram_size: int
    checkRamSize(ram)

    sleep (0.5)
    printBr()

    maxPlayers = input("How many maximum players can be on your server?\n- ")
    maxPlayersValue: int
    checkMaxPlayers()

    sleep (0.5)
    printBr()

    isLicense = input("OK, do you want make a license server (players may join server if they have license)?\nyes, no - ")
    isLicenseValue: bool
    checkLicense()

    sleep (0.5)
    printBr()

    motd = input ("What motd (description) do you want to set on server?\n- ")
    motd_value: str = motd
    checkDescription()

    sleep(0.5)
    printBr()

    gamemode = input ("What gamemode are you want to be on your server?\n- ")
    gamemode_value: str = gamemode
    checkGamemode()

    sleep(0.5)
    printBr()

    if (haveColorama):
        difficulty = input ("And what difficulty are you want to be on your server ({peaceful}peaceful{reset}, {easy}easy{reset}, {normal}normal{reset}, {hard}hard{reset} or {hardcore}hardcore{reset})?\n- ".format(peaceful=Fore.LIGHTGREEN_EX, easy=Fore.GREEN, normal=Fore.YELLOW, hard=Style.DIM + Fore.YELLOW, hardcore=Fore.RED, reset=Style.RESET_ALL))
    else:
        difficulty = input ("And what difficulty are you want to be on your server (peaceful, easy, normal, hard or hardcore)?\n- ")
    difficulty_value: str = difficulty
    checkDifficulty()

    sleep (0.5)
    printBr()

    # here is start mine script
    properties.close()
    createServerStartFile()

    sys.stdout.write ("\n")

    os.system("PAUSE")
except KeyboardInterrupt:
    sys.exit()
from os import system
from utils.globals import term

def print_help():
    system("clear")
    system("echo '" + term.normal \
        + term.green("Launch Arguments: \n") + term.red \
        + "--------------------------------------------- \n" \
        + get_line("--copy-skeleton ", " --- ", "copies template settings") \
        + term.cyan("This file can be found at ~/.config/Discline/config \n") \
        + "\n"
        + get_line("--store-token", " --- ", "stores your token") \
        + term.cyan("This file can be found at ~/.config/Discline/token \n") \
        + "\n"
        + term.green("Available Commands: \n") + term.red \
        + "--------------------------------------------- \n" \
        + get_line("/channel", "   - ", "switch to channel - (alias: 'c')") \
        + get_line("/server", "    - ", "switch server     - (alias: 's')") \
        + term.cyan + "Note: these commands can now fuzzy-find! \n" \
        + "\n" \
        + get_line("/servers", "   - ", "list available servers") \
        + get_line("/channels", "  - ", "list available channels") \
        + get_line("/users", "     - ", "list servers users") \
        + get_line("/emojis", "     - ", "list servers custom emojis") \
        + "\n" \
        + get_line("/nick", "      - ", "change server nick name") \
        + get_line("/game", "      - ", "change your game status") \
        + get_line("/file", "      - ", "upload a file via path") \
        + get_line("/status", "    - ", "change online presence") \
        + term.cyan + "This can be either 'online', 'offline', 'away', or 'dnd' \n" \
        + term.cyan + "(dnd = do not disturb) \n" \
        + "\n" \
        + get_line("/cX", "        - ", "shorthand to change channel (Ex: /c1)") \
        + term.cyan("This can be configured to start at 0 in your config") \
        + "\n" \
        + "\n" \
        + get_line("/quit", "      - ", "exit cleanly") \
        + "\n \n" \
        + term.magenta + "Note: You can send emojis by using :emojiname: \n" \
        + term.cyan("Nitro emojis do work! Make sure you have \n") \
        + term.cyan("nitro enabled in your config. \n") \
        + "\n"
        + term.yellow + "You can scroll up/down in channel logs \n" \
        + term.yellow + "by using PageUp/PageDown. \n" \
        + term.green + "~ \n" \
        + term.green + "~ \n" \
        + term.green + "~ \n" \
        + term.green + "(press q to quit this dialog)" \
        + "' | less -R")



def get_line(command, div, desc):
    return term.yellow(command) + term.cyan(div) + term.normal + desc + "\n"

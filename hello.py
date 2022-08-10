#!/usr/bin/env python3
"""Hello World Multi languages.

Depending on the language configured in the environment, the program show a 
corresponding message.

How to use:

You need have the LANG variable, example: 

        export LANG=pt_BR

Execution:

        python3 hello.py
        or
        ./hello.py
"""
__version__ = "0.0.1"
__autor__   = "Michel Ferreira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
elif current_language == "de_DE":
    msg = "Hallo Welt!"

print(msg) 
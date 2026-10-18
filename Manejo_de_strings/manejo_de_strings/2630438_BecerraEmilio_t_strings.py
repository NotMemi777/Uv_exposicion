# ==========================================
# COVER PAGE
# ==========================================
# Name: Emilio Alejandro Becerra Mireles
# Student ID: 2630438
# Email: 2630438@upv.edu.mx
# Group: IM-1
# Assignment: Strings in Python (t_strings)

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================
# Un string en Python es una secuencia de caracteres de tipo str y es
# inmutable: cualquier cambio crea una cadena nueva.
# Se puede concatenar, medir con len(), cortar con slicing, buscar con
# in o find() y reemplazar con replace().
# Como los usuarios escriben con espacios de más, mayúsculas mezcladas
# o nada, hay que limpiar con strip() y lower() y validar antes de
# procesar.
# Aquí hay seis programas: nombre, correo, palíndromo, estadísticas de
# una oración, contraseña y etiqueta de producto. Cada uno trae
# descripción, entradas, salidas, validaciones y tres casos de prueba.

# ==========================================
# GOOD PRACTICES
# ==========================================
# - Los strings son inmutables: cada cambio genera una cadena nueva.
# - Conviene usar strip() y lower() antes de comparar texto.
# - Evito números mágicos en los índices y explico qué saca cada slice.
# - Uso los métodos de string que ya existen en vez de rehacerlos.
# - Primero reviso que la entrada no esté vacía, después su formato.
# - Uso nombres de variables claros y mensajes de error entendibles.


# ==========================================
# Problem 1: Full name formatter (name + initials)
# ==========================================
# Description: Takes a full name in one string, cleans it up and shows
# it in Title Case together with the initials (for example J.C.T.).
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name is not empty after strip()
# - It has at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> Juan Carlos Tovar / J.C.T.
# 2) Border: "  ana   lopez  " -> Ana Lopez / A.L.
# 3) Error: "   " (only spaces) -> error message

# Prompt the user for their name and remove leading/trailing spaces
full_name = input("Name: ").strip()

# Split the input string into a list of words based on whitespace
words = full_name.split()

# Validate that the input is not empty and contains at least two words (first name + last name)
if not full_name or len(words) < 2:
    print("type at least a first name and a last name")
else: 
    # Reconstruct the name with a single space between words
    clean_name = " ".join(words)
    
    # Capitalize the first letter of each word
    formatted_name = clean_name.title()
    
    # Extract the first letter of each word, convert to uppercase, join with dots, and append a trailing dot
    initials = ".".join([word[0].upper() for word in words]) + "."
    
    # Output the formatted full name and its initials
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ==========================================
# Problem 2: Simple email validator (structure + domain)
# ==========================================
# Description: Checks that an email has exactly one '@', at least one
# '.' after the '@' and no spaces. If it is valid, it also shows the
# domain (the part after '@').
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text is not empty after strip()
# - Exactly one '@'
# - No spaces inside the text
#
# Test cases:
# 1) Normal: "emilio@upv.edu.mx" -> true, Domain: upv.edu.mx
# 2) Border: "a@b.c" -> true, Domain: b.c
# 3) Error: "emilio@upv" -> false (no '.' after the '@')

# Prompt for email input and remove outer whitespace
email_text = input("email: ").strip()

# Find the index of the '@' symbol
at_position = email_text.find("@")

# Extract the substring after the '@' symbol (the domain part)
domain_part = email_text[at_position + 1:]

# Evaluate all validation rules:
# 1. Ensure input is not empty
# 2. Check for no inner spaces
# 3. Ensure exactly one '@' character exists
# 4. Verify that the domain part contains at least one dot '.'
is_valid = (
    len(email_text) > 0 and 
    " " not in email_text and 
    email_text.count("@") == 1 and 
    "." in domain_part
)

# Output validation results according to specifications
if is_valid: 
    print("Valid email: true")
    print(f"Domain: {domain_part}")
else: 
    print("Valid email: false")



# ==========================================
# Problem 3: Palindrome Checker (Ignoring Spaces and Case)
# ==========================================
# Description: Checks if a phrase reads the same forwards and
# backwards, ignoring spaces and uppercase/lowercase.
#
# Inputs:
# - palindrome (string)
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - The normalized phrase when it is a palindrome
#
# Validations:
# - The phrase needs at least 3 characters after removing spaces
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true (anitalavalatina)
# 2) Border: "aba" -> true (exactly 3 characters)
# 3) Error: "ab" -> false (shorter than 3 characters)

# Prompt for a phrase and convert all characters to lowercase
palindrome = input("Checking if it is a palindrome: ").lower()

# Remove all spaces between words to normalize the string
clean_pal = palindrome.replace(" ", "")

# Validate that the normalized string has a minimum length of 3 characters
is_valid = len(clean_pal) >= 3

# Reverse the normalized string using slicing
checking_pal = clean_pal[::-1]

# Check if the normalized string equals its reverse AND meets the length requirement
if clean_pal == checking_pal and is_valid: 
    print("Is palindrome: true")
    print(clean_pal)
else:
    print("Is palindrome: false")


# ==========================================
# Problem 4: Sentence word stats (lengths and first/last word)
# ==========================================
# Description: Splits a sentence into words and shows how many there
# are, the first and last word, and the shortest and longest word.
#
# Inputs:
# - message (string)
#
# Outputs:
# - "Word count: <n>", "First word: <...>", "Last word: <...>"
# - "Shortest word: <...>", "Longest word: <...>"
#
# Validations:
# - The sentence has at least one word after strip() and split()
#
# Test cases:
# 1) Normal: "I love python programming" -> 4 words, first I,
#    last programming, shortest I, longest programming
# 2) Border: "Hello" -> 1 word, and it is first, last, shortest and longest
# 3) Error: "   " (only spaces) -> "Error: The sentence cannot be empty."

message = input("Type a sentence: ")
without_spaces = message.strip()
separating_message = without_spaces.split()

# Check that the list has at least one word
if len(separating_message) > 0:
    word_count = len(separating_message)
    shortest_word = separating_message[0]
    largest_word = separating_message[0]

    # The loop goes inside the if, so it only runs with valid input
    for word in separating_message:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(largest_word):
            largest_word = word

    # Print the results with the required format
    print(f"Word count: {word_count}")
    print(f"First word: {separating_message[0]}")
    print(f"Last word: {separating_message[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {largest_word}")

else:
    print("Error: The sentence cannot be empty.")


# ==========================================
# Problem 5: Password strength classifier
# ==========================================
# Description: Classifies a password as weak, medium or strong.
# Rules I used:
# - Strong: 8+ characters with uppercase, lowercase, digit and symbol.
# - Medium: 8+ characters with uppercase and lowercase, or a digit.
# - Weak: anything else.
#
# Inputs:
# - password (string)
#
# Outputs:
# - "Password strength: weak", "Password strength: medium" or
#   "Password strength: strong"
#
# Validations:
# - The password is not empty after strip()
#
# Test cases:
# 1) Normal: "Hello123!" -> strong
# 2) Border: "Abcdefg1" -> medium (8 characters, no symbol)
# 3) Error: "" (empty) -> "Error: invalid input"

password = input ("Type your password: ")
clean_password = password.strip()
result = ""
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in clean_password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():  # if it is not alphanumeric, it is a symbol
        has_symbol = True

if len(clean_password) >= 8 and has_symbol and has_digit and has_lower and has_upper:
    result = "strong"
elif len(clean_password) >= 8 and ((has_upper and has_lower) or has_digit):
    result = "medium"
else:
    result = "weak"

if len(clean_password) == 0:
    print("Error: invalid input")
else:
    print(f"Password strength: {result}")


# ==========================================
# Problem 6: Product label formatter (fixed-width text)
# ==========================================
# Description: Builds a one-line label "Product: <NAME> | Price: $<PRICE>"
# that is exactly 30 characters long: padded with spaces if it is
# shorter and cut if it is longer.
#
# Inputs:
# - product_name (string)
# - price_value (number)
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
#
# Validations:
# - product_name is not empty after strip()
# - price_value is greater than 0
#
# Test cases:
# 1) Normal: "Pen", 12.5 -> "Product: Pen | Price: $12.5   "
# 2) Border: "Notebook", 99.99 -> "Product: Noteb | Price: $99.99"
#    (name cut to 5 characters, label is exactly 30)
# 3) Error: "Pen", 0 -> "Error: A price cannot be 0 or less."

# ==========================================
# Problem 6: Product label formatter (fixed-width text)
# ==========================================

product_name = input("Type the name of a product: ")

try:
    price_value = float(input("Type the price of the product: "))
    
    clean_name = product_name.strip()

    # Initial validations
    if len(clean_name) == 0:
        print("Error: Product name cannot be empty.")
    elif price_value <= 0:
        print("Error: A price cannot be 0 or less.")
    else:
        # 1. Limit the product name first so it never crushes the price
        clean_name = clean_name[:5]
        
        # 2. Build the label with the safe name
        label = f"Product: {clean_name} | Price: ${price_value}"
        
        # 3. Pad with spaces at the end up to 30 characters
        label = label.ljust(30)

        # 4. Cut it in case it is longer than 30 characters
        label = label[:30]
            
        # 5. Print the final result between quotes
        print(f'Label: "{label}"')

except ValueError:
    print("Error: invalid input")

# ==========================================
# CONCLUSIONS
# ==========================================
# Casi todo programa con texto empieza limpiando la entrada: strip() y
# lower() hacen que un mismo dato escrito de tres formas se compare
# igual, como "Anita lava la tina" en el palíndromo.
# split() sirve para contar palabras y join() para armarlas otra vez
# con un solo espacio. Las validaciones evitan datos basura: una
# contraseña vacía o un precio de 0 no deben llegar al resto.
# Con la etiqueta vi que ljust() rellena pero no recorta, hace falta
# [:30], y que cada método devuelve una cadena nueva (inmutables).

# ==========================================
# REFERENCES
# ==========================================
# 1) Python documentation - Built-in Types: Text Sequence Type - str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Tutorial - An Informal Introduction to Python (Strings)
#    https://docs.python.org/3/tutorial/introduction.html#strings
# 4) W3Schools - Python Strings
#    https://www.w3schools.com/python/python_strings.asp
# 5) Real Python - Strings and Character Data in Python
#    https://realpython.com/python-strings/
# 6) PEP 8 - Style Guide for Python Code (naming conventions)
#    https://peps.python.org/pep-0008/
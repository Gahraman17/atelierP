def full_name(str_arg:str) -> str:
    parts = str_arg.split()
    
    if len(parts)== 2:
        nom = parts[0].upper()
        prenom = parts[1].capitalize()
        
        return f"{nom} {prenom}"
    
user_input = input("Enter a name in the format 'nom prenom': ")
print(full_name(user_input))
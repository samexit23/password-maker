import random
import string

def generate_random_characters(length):
    # Combines letters, numbers and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_specific_combination_to_file(filename, combination):
    # Saves a specific combination to the specified file
    with open(filename, 'w') as file:
        file.write(combination + '\n')
    print(f"\nLa combinaison a été enregistrée dans '{filename}'.")

def main():
    while True:
        
        try:
            length_per_combination = int(input("Quelle longueur pour chaque combinaison de caractères ? :"))
            if length_per_combination <= 0:
                print("La longueur doit être un nombre positif.")
                continue
        except ValueError:
            print("Veuillez entrer un numéro valide.")
            continue

        num_combinations = int(input("Combien de combinaisons souhaitez-vous générer ? :"))
        if num_combinations <= 0:
            print("Le nombre de combinaisons doit être un nombre positif.")
            continue
    
        print("\nCombinaisons générées :")
        combinations = []
        for i in range(num_combinations):
            combination = generate_random_characters(length_per_combination)
            formatted_combination = f"Combinaison {i + 1}   : {combination}"
            print(formatted_combination)
            combinations.append(formatted_combination)
        
        # Ask if user wants to save a combination in particular
        save_option = input("\nVoulez-vous enregistrer une combinaison spécifique dans un fichier ? (o/n) ").strip().lower()
        if save_option == 'y':
            try:
                index = int(input(f"Entrez le numéro de combinaison à enregistrer (1 à {num_combinations}) : ")) - 1
                if 0 <= index < num_combinations:
                    filename = input("Veuillez entrer le nom du fichier (avec l'extension .txt) : ")
                    save_specific_combination_to_file(filename, combinations[index])
                else:
                    print("Numéro de combinaison invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        
        cont = input("\nVoulez-vous générer d’autres combinaisons ? (o/n) ").strip().lower()
        if cont != 'o':
            print("Fin du programme.")
            break

if __name__ == "__main__":
    main()

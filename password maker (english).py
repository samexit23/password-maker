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
    print(f"\nThe combination was saved in '{filename}'.")

def main():
    while True:
        
        try:
            length_per_combination = int(input("What length for each character combination ? :"))
            if length_per_combination <= 0:
                print("The length must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        num_combinations = int(input("How many combinations do you want to generate ? :"))
        if num_combinations <= 0:
            print("The number of combinations must be a positive number.")
            continue
        
        print("\nCombinations generated:")
        combinations = []
        for i in range(num_combinations):
            combination = generate_random_characters(length_per_combination)
            formatted_combination = f"Combination {i + 1}   : {combination}"
            print(formatted_combination)
            combinations.append(formatted_combination)
        
        # Ask if user wants to save a combination in particular
        save_option = input("\nDo you want to save a specific combination to a file? (y/n) ").strip().lower()
        if save_option == 'y':
            try:
                index = int(input(f"Enter the combination number to save (1 to {num_combinations}) : ")) - 1
                if 0 <= index < num_combinations:
                    filename = input("Please enter the file name (with extension .txt) : ")
                    save_specific_combination_to_file(filename, combinations[index])
                else:
                    print("Invalid combination number.")
            except ValueError:
                print("Please enter a valid number.")
        
        cont = input("\nDo you want to generate other combinations? (y/n) ").strip().lower()
        if cont != 'o':
            print("End of program.")
            break

if __name__ == "__main__":
    main()

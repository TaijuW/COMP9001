def choose_stone(color, options):
    print(f"\n{color.upper()} player, choose your stone:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            choice = int(input("Enter number (1-3): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")
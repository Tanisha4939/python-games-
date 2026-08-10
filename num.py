import random

def play_dice_battle():
    print("\n=== Welcome to the Dice Face Battle! ===")
    
    while True:
        # 1. Player chooses a target dice face
        user_input = input("\nChoose a dice face (1-6) or type 'exit': ").strip().lower()
        
        if user_input == 'exit':
            print("Thanks for playing! Goodbye.")
            break
            
        # Validation: Check if input is a digit and between 1 and 6
        if not user_input.isdigit() or not (1 <= int(user_input) <= 6):
            print("❌ Invalid choice! Please select a number from 1 to 6.")
            continue
            
        chosen_face = int(user_input)
        print(f"🎯 Your Target Face: {chosen_face}")
        
        # 2. Roll the dice (one for computer, one for player)
        player_roll = chosen_face
        computer_roll = random.randint(1, 6)
        
       
        print(f"🤖 Computer Rolled: {computer_roll}")
        
        # 3. Step A: Determine the Highest Number Winner
        print("\n--- Battle Results ---")
        if player_roll > computer_roll:
            print("🎉 You win! Your roll is higher.")
        # elif computer_roll > player_roll:
        #     print("😢 Computer wins! Its roll is higher.")
        else:
            print("🤝 It's a tie! Both rolled the same number.")
            
        # 4. Step B: Bonus Target Check using if-else
        if  and computer_roll == chosen_face:
            print("🔥 WOW! Both you and the computer hit your target face!")
        elif player_roll == chosen_face:
            print("⭐ Bonus: You hit your target face exactly!")
        elif computer_roll == chosen_face:
            print("🤖 Bonus: The computer hit your target face!")

# Run the game loop
play_dice_battle()

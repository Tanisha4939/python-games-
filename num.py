import random

def play_dice_vs_computer():
    print("\n=== Welcome to Dice Choice vs Computer! ===")
    print("Rules: Choose your die face. The computer rolls randomly. Highest number wins!")
    
    while True:
        
        user_input = input("\nChoose your die number (1-6) or type 'exit': ").strip().lower()
        
        if user_input == 'exit':
            print("Thanks for playing! Goodbye.")
            break
             
        if not user_input.isdigit() or not (1 <= int(user_input) <= 6):
            print("❌ Invalid input! Please enter a number from 1 to 6.")
            continue
            
        player_choice = int(user_input)
           
        computer_roll = random.randint(1, 6)
        
        print(f"\n🎲 You chose: {player_choice}")
        print(f"🤖 Computer rolled: {computer_roll}")
        print("-----------------------")
        
        if player_choice > computer_roll:
            print(f"🎉 You win! Your number ({player_choice}) is higher than the Computer's ({computer_roll}).")
        elif computer_roll > player_choice:
            print(f"😢 Computer wins! Its number ({computer_roll}) is higher than yours ({player_choice}).")
        else:
            print(f"🤝 It's a tie! Both of you have the number {player_choice}.")
            

play_dice_vs_computer()

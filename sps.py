import random

def play_stone_paper_scissors():
    choices = ["stone", "paper", "scissors"]
    print("\n--- Welcome to Stone, Paper, Scissors! ---")
    
    while True:
        # 1. Input & Validation
        player = input("\nEnter choice (stone, paper, scissors) or type 'exit': ").lower().strip()
        
        if player == "exit":
            print("Thanks for playing! Goodbye.")
            break # Breaks the loop to end the game
            
        if player not in choices:
            print("❌ Invalid input! Please check your spelling.")
            continue # Restarts the loop to ask the player again
            
        # 2. Computer Choice
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        # 3. Game Logic using if-elif-else
        if player == computer:
            print("🤝 It's a tie!")
        elif (player == "stone" and computer == "scissors") or \
             (player == "paper" and computer == "stone") or \
             (player == "scissors" and computer == "paper"):
            print("🎉 You win this round!")
        else:
            print("🤖 Computer wins this round!")

# Run the game
play_stone_paper_scissors()

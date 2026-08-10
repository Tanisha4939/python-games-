import random

def play_stone_paper_scissors():
    choices = ["stone", "paper", "scissors"]
    print("\n--- Welcome to Stone, Paper, Scissors! ---")
    
    while True:
        player = input("\nEnter choice (stone, paper, scissors) or type 'exit': ").lower().strip()
        
        if player == "exit":
            print("Thanks for playing! Goodbye.")
            break 
            
        if player not in choices:
            print("❌ Invalid input! Please check your spelling.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("🤝 It's a tie!")
            
        elif (player == "stone" and computer == "scissors"):
            print("🎉 You win this round!")

        elif (player == "paper" and computer == "stone"):
            print("🎉 You win this round!")

        elif (player == "scissors" and computer == "paper"):
            print("🎉 You win this round!")

        else:
            print("🤖 Computer wins this round!")

play_stone_paper_scissors()

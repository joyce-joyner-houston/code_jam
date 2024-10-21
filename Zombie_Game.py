class SurvivalZombieGame:
    
 
    def init (self, player_name: str, zombie_count: int):
        
 
        if zombie_count <= 0:
            print("Error: Zombie count should be greater than zero.")
 
        self.player_name = player_name
        self.zombie_count = zombie_count
 
    def start(self):
 
        
        player_health = 100
 
        
        while self.zombie_count > 0 and player_health > 0:
            print(f"Player: {self.player_name}")
            print(f"Health: {player_health}")
            print(f"Zombies remaining: {self.zombie_count}")
            print("What do you want to do?")
            print("1. Attack")
            print("2. Run away")
 
            choice = input("Enter your choice: ")
 
            if choice == "1":
                
                self.zombie_count -= 1
                player_health -= 10
                print("You attacked a zombie!")
                print("You took some damage in the process.")
 
            elif choice == "2":
                
                print("You ran away from the zombies!")
                print("Game over.")
                return "You lose!"
 
            else:
                print("Invalid choice. Please try again.")
 
        if self.zombie_count == 0:
            print("Congratulations! You defeated all the zombies!")
            return "You win!"
 
        if player_health <= 0:
            print("You were defeated by the zombies.")
            return "You lose!"
 

game = SurvivalZombieGame("Steve", 8)

result = game.start()

print(result)

# Imports
from LeagueGeneration import LeagueGeneration


# Functions
def startGame():
    start = "start"
    userInput = input("Type 'start' to begin: ")
        
    while start!=userInput:
        userInput = input("Type 'start' to begin: ")


# Main

print("Welcome to Simple Hoops Sim where you can create your own basketball league and become the owner you've always wanted to be")

startGame()

# ask user how many teams they'd like to generate for their new league
amountOfTeams = int(input("how many teams would you like to generate? "))
playersPerTeam = int(input("how many players do you want generated per roster? "))

LeagueGeneration.LeagueGeneration(amountOfTeams, playersPerTeam)

print(LeagueGeneration.PlayersDetails)
print(LeagueGeneration.PlayersAdvancedDetails)
#Step 1 
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





word_list = ["Matrix", "Avatar", "StarWars", "Titanic", "Inception", "Joker", "PulpFiction", 
            "Interstellar", "ForrestGump", "TheGodfather", "Gladiator", "TheShawshankRedemption", 
            "TheDarkKnight", "JurassicPark", "TheAvengers", "HarryPotter", "TheLordoftheRings", 
            "LaLaLand", "ToyStory", "Frozen", "E.T.theExtraTerrestrial", "BacktotheFuture", 
            "TheLionKing", "TheTerminator", "FindingNemo", "Casablanca", "TheSixthSense", 
            "FightClub", "DieHard", "MadMax", "ThePrincessBride", "Jaws", "TheShining", 
            "Goodfellas", "TheSoundofMusic", "Grease", "TheExorcist", "TheWizardofOz", 
            "RaidersoftheLostArk", "Rocky", "BladeRunner", "TheSilenceoftheLambs", 
            "Braveheart", "Alien", "TheTrumanShow", "BlackPanther", "AClockworkOrange", 
            "TheGrandBudapestHotel", "GonewiththeWind", "MaryPoppins", "2001:ASpaceOdyssey", 
            "Amadeus", "The Green Mile", "TheBigLebowski", "Memento", "NoCountryforOldMen", 
            "TheDeparted", "ReservoirDogs", "Scarface", "TaxiDriver", "TheSocialNetwork", 
            "TheGreatGatsby", "The Revenant", "12YearsaSlave", "ThePianist", "Dunkirk", 
            "Arrival", "The Shape of Water", "Moonlight", "Birdman", "TheArtist", "DallasBuyersClub", 
            "The Hurt Locker", "Argo", "Spotlight", "BirdBox", "A Quiet Place", "Us", "GetOut", 
            "Black Swan", "The KingsSpeech", "SlumdogMillionaire", "TheHelp", "SilverLiningsPlaybook", 
            "AmericanHustle", "TheWolfofWall Street", "Gravity", "Her", "Boyhood", "Whiplash", 
            "ManchesterbytheSea", "MoonriseKingdom", "Brooklyn", "LaLaLand"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)

lower_case_word = chosen_word.lower()

#Displaying the blanks
display = []

word_length = len(chosen_word)

for _ in range(word_length):
  display += "_"
print(display)
####################

#Game loop
end_of_game = False

lives = 0

while not end_of_game:
  
  guess = input("Guess a letter: ").lower()
  
  #Checking the guessed letter and replacing the blanks with the guessed letter
  
  for position in range(word_length):
    letter = lower_case_word[position]
    if letter == guess:
      display[position]= letter
    
  print(display)

  if guess not in lower_case_word:
    lives +=1
    if lives == 0:
      end_of_game = True
      print("You lose")
  
  if "_" not in display:
    end_of_game = True
    print("You win")
  

#############################
  print(stages[lives])



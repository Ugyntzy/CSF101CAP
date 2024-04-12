################################
# Ugyen Wangchuk
#BE ELECTRICAL ENGG. 1YEAR
# 02230092
################################
# REFERENCES
# @Python Crash course
# @Learn python 3 the hard way
################################
# My Solution Score:49801
################################

# Read the input.txt file
def read_input(Input_your_file_name):#The function read_input takes a single argument called Input_your_file_name.
                                     #It reads data from a file specified by the filename provided.
    # Initializes an empty list to store the data
    x = []

    # Opens the specified file in read mode
    with open(Input_your_file_name, 'r') as files:
        # Iterates through each line in the file
        for y in files:
            # Splits the line into two parts based on whitespace
            opponent_choice, outcome = y.split()
            # Append a tuple (opponent_choice, outcome) to the list
            x.append((opponent_choice, outcome))

    # Returns the list containing the data from the file
    return x


# To Calculate the score for each round
def calculate_score(Total_Number_of_rounds):
    Score = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # X means the opponent need to win
            if opponent_choice == 'A':#Theinput is A meaning they showed Rock
                Score += 3  #  The opponent won since we showed scissor(Rock breaks scissor),score=0(lose)+3(scissor)
            elif opponent_choice == 'B':#The input is B meaning they are showing Papper
                Score += 1  #The opponent won since we showed Rock(Paper blocks rock), score=0(lose)+1(Rock)
            elif opponent_choice == 'C':# The the input is C meaning they showed scissor
                Score += 2  # The opponent won since we showed Paper(scissor cuts paper),score=0(lose)+2(scissor)
        elif outcome == 'Y':  # Y means we need to end up in a draw
            if opponent_choice == 'A':#The input is A meaning they showed Rock
                Score += 4  #The result is a draw since we also showed rock,score=3(Draw)+1(Rock)
            elif opponent_choice == 'B':#The input is B meaning they showed paper
                Score += 5   #The result is a draw since we also showed paper,score=3(Draw)+2(Paper)
            elif opponent_choice == 'C':#The input is C meaning they picked Scissor
                Score += 6  #The result is a draw since we also showed rock,score=3(Draw)+3(Scissor)
        elif outcome == 'Z':  # Z means we need to win
            if opponent_choice == 'A':#The input is A meaning they picked Rock
                Score += 8 #Since Paper blocks Rock we show Paper to win,score=6(Win)+2(Paper)
            elif opponent_choice == 'B':#The input is B meaning they chose Paper
                Score += 9  # Since scissor cuts paper we show scissor to win,score=6(Win)+3(scissor)
            elif opponent_choice == 'C':#The input is C meaning the opponent showed scissor
                Score += 7  # Since Rock breaks Scissor we show Rock to win,score=6(Win)+1(Rock)
    print(f"The total score is:{Score}") #The outcome for this code will be yo based on the input from the file

# To Run the programe
Input_your_file_name = "CSF101_CAP/input_2_cap1.txt" 
calculate_score(read_input(Input_your_file_name))
#The variable Input_your_file_name contains the filename (e.g., "CSF101_CAP/input_2_cap1.txt").
#The function read_input reads data from the specified file.
#It will  processe each line in the file, splitting it into opponent_choice and result.
#The data will be stored in a list called Total_Number_of_rounds.
#The function calculate_score processes each round in Total_Number_of_rounds.
#Based on the outcome (which can be 'X', 'Y', or 'Z'), it updates the Score.

# Trivia Game

# Store questions

# Store answers

# Randomly pick and ask questions

# Check answers

# Store score

# Give score

# Import the random module
import random

# Dictionary storing the trivia questions
trivia_questions = {
    "Is Evan Gay?": "Yes",
    "How many continents are there on Earth?": "7",
    "What is 5 + 7?": "12",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "What is the chemical symbol for water?": "H2O",
    "How many legs does a spider have?": "8",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the tallest animal in the world?": "Giraffe",
    "What is the square root of 64?": "8"
}
def main():
    # Start the main game by calling the function  
    start_game()
    
    
# Main game function.
def start_game():
    
    # Store the questions in a list functionm, set the number of questions to be asked and the user score to zero
    questions = list(trivia_questions.keys())
    total_questions = 5
    score = 0
    
    # Pick set number of random questions from dictionary
    selected_questions = random.sample(questions, total_questions)
    
    # user enumerate for loop to print each question with an index position
    for index, question in enumerate(selected_questions):
        print(f"{index + 1}: {question}")
        
    # Get the users answer for each question, covert to lower and remove white spaces
        user_input = input("Please enter your answer: ").lower().split()
        
        check_answer = trivia_questions[question]
    
        if user_input == check_answer.lower().split():
            print("Correct! \n")
            score += 1
        else:
            print(f"Incorrect, the correct answer is {check_answer} \n")
        
    print(f"Game Complete! Your final score is: {score}/{total_questions}")

 
main()

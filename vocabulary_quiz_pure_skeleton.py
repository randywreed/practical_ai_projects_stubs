
# Vocabulary Quiz
# A simple quiz program using dictionaries and lists

# TODO: Create an empty dictionary to store words and their definitions


# TODO: Create two empty lists:
# - One to store correctly answered words
# - One to store incorrectly answered words
correct_vocab=[]
incorrect_vocab=[]

# TODO: Create the add_word function that:
# - Takes parameters: word (str) and definition (str)
# - Adds the word and definition to the vocabulary dictionary
# - Prints a message confirming the word was added
def add_words(word,definition):
  vocab[word]=definition
  print("word added")
  return
  
# TODO: Create the take_quiz function that:
# - Takes optional parameter: num_questions (int, default 5)
# - Imports the random module to select random words
# - Clears both the correct_answers and incorrect_answers lists
# - Checks if there are any words in the vocabulary
# - If no words, prints a message and returns 0
# - Otherwise, limits the number of questions to the available words
# - Uses random.sample to select random words for the quiz
# - Initializes a score variable to keep track of correct answers
# - Loops through each word in the quiz_words list
# - For each word, asks the user for the definition
# - Checks if the answer is correct (matches the definition)
# - If correct, increments score and adds to correct_answers list
# - If incorrect, adds to incorrect_answers list
# - Prints the final score
# - Returns the score
def take_quiz(num_questions=5):
    import random
    correct_vocab.clear=[]
    incorrect_vocab.clear=[]
    if not vocab:
      print('no vocab words, please add words first')
      return 0
    num_questions=min(num_questions,len(vocab))
    quiz_words=random.sample(list(vocab.keys()),numquestions)
    score=0
    for word in quiz_words:
        user_definition=input(f"what is the definition of {word}: ")
        if user_definition==vocab[word]:
            score+=1
            print("correct!")
            correct_vocab.append(word)
        else:
            incorrect_vocab.append(word)
            print("sorry! thats wrong")
    print(f'your final score is {score}/{num_questions}')
    return score

# TODO: Create the show_results function that:
# - Takes no parameters
# - Prints a header for the quiz results
# - Checks if any quiz has been taken (both results lists are empty)
# - If no quiz taken, prints a message and returns
# - Otherwise, prints all correct answers with their definitions
# - Prints all incorrect answers with their definitions
# - Calculates and prints the final score as a fraction
def show_results():
    print("quiz results")
    if not correct_vocab and not incorrect_vocab:
        print("no quiz has been taken")
      return  
    print("correct vocab")
    for word in correct_vocab:
        print(f'{word}: {vocab[word]]}')
    print("incorrect answers")
    for word in incorrect_vocab:
        print(f'{word}: {vocab{word}}')
    score=len(correct_vocab)+len(incorrect_vocab)
    total_words=len(correct_vocab)+len(incorrect_vocab)
    print(f"your score is {len(correct_vocab)}/{total_words}")
    

# TODO: Create the main program that:
# - Prints a welcome message
# - Creates a menu loop with these options:
#   1. Add new word
#   2. Take quiz
#   3. Show results
#   4. Exit
# - For option 1: Gets word and definition from user, calls add_word
# - For option 2: Gets number of questions from user, calls take_quiz
# - For option 3: Calls show_results
# - For option 4: Prints goodbye message and exits
# - For invalid options: Shows error message
def main
    print("welcome to the vocabulary quiz")
    while true:
        print("/n menu"
        print("1. add new word")
        print("2. take quiz")
        print("3. show results")
        print('4. exit')
        choice=input("enter your choice: ")
        if choice==1:
            add_word=input("enter the word: ")
            definition=input("enter the definition: ")
            add_word(word,definition)
        if choice==2:
            num_questions=int(input("how many question would you like? "))
            take_quiz(num_questions)
          elif choice==3:
            show_results()
          elif choice==4:
            show results()
            
          print('Bye')
          break
      else:
          print('invalid choice')

if __name__ == "__main__"
          
        
        

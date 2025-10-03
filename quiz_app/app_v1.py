import csv

def load_questions(filename):
    questions =[]
    # Open CVS file
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Parses each question, its options, and the correct answer.
        for row in reader:
            Q = row['question']
            Op1 = row['option1']
            Op2 = row['option2']
            Op3 = row['option3']
            Op4 = row['option4']
            A = row['answer']
            questions.append({
                'question': Q,
                'options': [Op1, Op2, Op3, Op4],
                'answer': A,
            })
    # Returns a list of question dictionaries.
    return questions

def run_quiz(questions):
    score = 0
    count = 1
    # Parses each question one at a time
    for q in questions:
        print(f"Question {count}: {q['question']}?")
        for idx, option in enumerate(q['options']):
            print(f"Option {idx+1}: {option}")
        count = count + 1
        # Collects answers and checks correctness.
        choice = int(input("Your Answer (1-4): "))
        answer = int(q['answer'])
        if choice == answer:
            score += 1
            print(f"Correct! \nScore: {score}/{count - 1}")
        else:
            print(f"Incorrect. \nScore: {score}/{count - 1}")
    return score

def save_score(score, filename):
    # Saves the user's score to a file after the quiz.
    # Get user to input name
    name = input(f"Input your name to save your score \nEnter 'no' to exit without saving. \nName:")
    if name.strip().lower() == "no":
        return
    else:
        # Save username, score in csv
        with open(filename, 'a', newline='',) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, score])
        print(f"{name.title()}'s score of {score} has been saved!")


def read_scores(filename):
    # Reads and displays scores.
    print("Score's So Far")
    # Open file
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        reader = sorted(reader, key = lambda row: row[1], reverse = True) ## sorting into score order
        # Printing each username + score
        for row in reader:
            name = row[0]
            score = row[1]
            print(name + ":", score)


def main():
    run = True
    # Keeps program running
    while run:
        print("Welcome to the Computer Science Quiz \nDo you want to: \nA: Take The Quiz \nB: See The Scores \nC: Exit")
        # Takes a choice from the user
        choice = input("")
        choice =  choice.strip()
        # Choose action depending on choice
        if choice == "C":
            run = False
            exit
        elif choice == "B": ## view scores
            read_scores('Education\\quiz_app\\score.csv')
            # Allows you to leave after viewing the scores
            leave = input("Do you want to exit? [Y]Yes [N]No ")
            if leave == "Y":
                run = False
                exit
            else:
                continue
        elif choice == "A": ## play quiz
            questions = load_questions('Education\\quiz_app\\questions.csv')
            score = run_quiz(questions)
            save_score(score, 'Education\\quiz_app\\score.csv')
            # Allows you to leave if you save your score
            leave = input("Do you want to exit? [Y]Yes [N]No ")
            if leave == "Y":
                run = False
                exit
            else:
                continue


main()
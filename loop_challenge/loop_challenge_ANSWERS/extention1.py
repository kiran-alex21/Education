## Score Processor with Names

# global variables
scorelist = {}
score_info = {}
top5 = []

def score_input():
    ## Take an input of scores and names
    num_scores = int(input("How many score do you have to input? "))
    for i in range(num_scores):
        name = input(f"Student {i+1}: ")
        score = input(f"Score {i+1}: ")
        ## Keep names and scores linked
        scorelist.update({name: score})
    return scorelist

def compute_scores(scorelist):
    ## Total Scores Entered
    total = 0
    amount = 0
    for k in scorelist:
        total += 1
        amount = amount + int(scorelist[k])
    ## Average Score
    avg = round(float(amount / total), ndigits=1)
    ## Top 5 Scores
    high = 0
    for ke in scorelist:
        # No. of people with Highest Score
        if int(scorelist[ke]) <= high:
            try:
                i = 0
                while int(scorelist[ke]) <= int(top5[i][1]):
                    i += 1
                top5.insert(i, [ke, int(scorelist[ke])])
            except IndexError:
                top5.append([ke, int(scorelist[ke])])
        elif int(scorelist[ke]) > high:
            high = int(scorelist[ke])
            top5.insert(0, [ke, high])
    del top5[5:]
    # Dictionary of info
    score_info = {
        'Total': total,
        'Average': avg,
        'Top5' : top5
    }
    return score_info

def print_scores(score_info):
    ## Display the:
    # Total Scores Entered
    print(f"There were {score_info['Total']} scores inputted")
    # Average Score
    print(f"The Average Score was {score_info['Average']}")
    # Top 5 scores and names attached to them
    print("The top 5 scores are:")
    top = score_info['Top5']
    for person, score in top:
        print(f"Name: {person} | Score {score}")
    return

def main():
    print_scores(compute_scores(score_input()))

main()

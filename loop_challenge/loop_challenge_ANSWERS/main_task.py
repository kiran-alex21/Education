## Score Processor

# global variables
scorelist = []
score_info = {}

def score_input():
    ## Take an input of scores.
    raw_scores = input("Enter a list of scores, sperated by comma's (,): ")
    # split into list of speperate scores
    scorelist = raw_scores.split(',')
    # convert from strings to floats
    scorelist = [float(score) for score in scorelist]
    # output scorelist
    return scorelist

def compute_scores(scorelist):
    # Total Scores Entered
    total = 0
    amount = 0
    for i in scorelist:
        total += 1
        amount = amount + i
    # Average Score
    avg = round(float(amount / total), ndigits=1)
    # Highest Score
    high = 0
    count = 0
    for i in scorelist:
        # No. of people with Highest Score
        if i == high:
            count += 1
        elif i > high:
            high = i
            count = 1
    # Dictionary of info
    score_info = {
        'Total Scores given': total,
        'Average Score': avg,
        'Highest Score': int(high),
        'No. with Highest Score': count,
    }
    return score_info

def print_scores(score_info):
    # Display:
    for item in score_info:
        print(item, 'is', score_info[item])

def main():
    print_scores(compute_scores(score_input()))

main()

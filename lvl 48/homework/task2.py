def better_than_average(scores, your_score):
    # Calculate the average of the peers' scores
    average_score = sum(scores) / len(scores)
    
    # Compare your score with the average score
    return your_score > average_score

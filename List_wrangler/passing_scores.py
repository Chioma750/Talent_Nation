# Implement passing_scores(scores, minimum).
# Return a new list containing only the scores that
# are greater than or equal to minimum. Preserve the 
# original order. Do not modify the original list.

def passing_scores(scores, minimum):
    result = []

    for score in scores:
        if score >= minimum:
            result.append(score)

    return result
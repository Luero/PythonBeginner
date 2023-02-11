# ask_number (upgraded)
# Created by Luero, 30/05/2022

def ask_number (question = "Choose the number", low = 0, high = 10, gap = 1):
    response = None
    count = []
    while response not in range(low, high):
        response = int(input(question))
        count.append(response)
        for point in range (response, high):
            point += gap
            count.append(point)
    return count

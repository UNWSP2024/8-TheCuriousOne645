import random

def capital_quiz():
    # U.S. states and their capitals
    states_capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
        'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
        'Florida': 'Tallahassee', 'Georgia': 'Atlanta'
    }

    correct = 0
    incorrect = 0
    states = list(states_capitals.keys())
    random.shuffle(states)

    for state in states:
        capital_guess = input(f"What is the capital of {state}? ")
        if capital_guess.lower() == states_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The capital of {state} is {states_capitals[state]}.")
            incorrect += 1

    print(f"\nQuiz Results: {correct} correct, {incorrect} incorrect.")

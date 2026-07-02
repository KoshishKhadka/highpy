scores = [85,92,78,95,88]

for score in scores:
    print (f"score: {score} ")

print(f"first score: {scores[0]}")
print(f"last score:{scores[4]}")
print (f"Total scores:{len(scores)}")

print(f"Last score using -1:{scores[-1]}")

def average(numbers):
    result = sum(numbers) / len(numbers)
    return result

avg = average(scores)
print(f"Average score: {avg}")
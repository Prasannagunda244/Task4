print("=" * 50)
print("        BASIC TEXT RECOGNITION AI")
print("=" * 50)

positive_words = [
    "good",
    "great",
    "excellent",
    "happy",
    "love",
    "awesome",
    "nice",
    "amazing",
    "best"
]

negative_words = [
    "bad",
    "sad",
    "hate",
    "worst",
    "angry",
    "poor",
    "terrible",
    "awful"
]

print("\nEnter any sentence:")
text = input(">> ").lower()

positive_count = 0
negative_count = 0

words = text.split()

for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

print("\nRecognized Words:")

for word in words:
    if word in positive_words:
        print(word, "-> Positive")
    elif word in negative_words:
        print(word, "-> Negative")
    else:
        print(word, "-> Neutral")

print("\nResult")

if positive_count > negative_count:
    print("Overall Sentiment : POSITIVE 😊")
elif negative_count > positive_count:
    print("Overall Sentiment : NEGATIVE ☹️")
else:
    print("Overall Sentiment : NEUTRAL 😐")

print("\nStatistics")
print("Positive Words :", positive_count)
print("Negative Words :", negative_count)
print("Total Words :", len(words))
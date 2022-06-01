from collections import Counter
sentence = "I can do i can me don't know what you know you".upper()
sentence_counts = Counter(sentence.split())
print(f"{'word':<12}count")
for word,y in sorted(sentence_counts.items()):
    print(f"{word:<12}{y}")

print("\n the number of unique word is",len(sentence_counts))
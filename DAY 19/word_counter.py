content = "The quick brown fox jumps over the lazy dog. The dog woke up and barked at the fox. They both ran away."
with open("story.txt", "w") as file:
    file.write(content)
    
with open("story.txt", "r") as file:
    text = file.read()

words_list = text.split() 
total_words = len(words_list)

print(f"Total words in file: {total_words}")

the_count = 0
for word in words_list:
    
    if word.lower() == "the":
        the_count += 1

print(f"The word 'the' appears {the_count} times.")
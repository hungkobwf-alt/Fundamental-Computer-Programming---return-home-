# Task 1: Find the 5 greatest numbers
numbers = []

print("Enter numbers one by one. Press Enter without typing anything to stop.")

while True:
    user_input = input("Enter a number: ")
    
    if user_input == "":
        break 
        
    number = int(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

top_five = numbers[:5]

print("\n--- Results ---")
print("The greatest numbers are:", top_five)
# Task 2: Determine the season based on the month
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("The season is:", seasons[0])

elif month == 3 or month == 4 or month == 5:
    print("The season is:", seasons[1])

elif month == 6 or month == 7 or month == 8:
    print("The season is:", seasons[2])

elif month == 9 or month == 10 or month == 11:
    print("The season is:", seasons[3])

else:
    print("Invalid month! Please enter a number between 1 and 12.")
 
# Task 3: Track new and existing names
entered_names = set()

print("Enter names one by one. Press Enter without typing anything to stop.")

while True:
    name = input("Enter a name: ")
    
    if name == "":
        break
        
    if name in entered_names:
        print("Existing name")
    else:
        print("New name")
        entered_names.add(name)

print("\n--- List of all unique names entered ---")
for unique_name in entered_names:
    print(unique_name)
# Task 4: Calculate the proportion of the top 5 most common words

def calculate_word_proportion(text):

    text = text.lower()

    text = text.replace(".", "").replace(",", "")
    
    words_list = text.split()
    total_words = len(words_list)
    
    word_counts = {}
    
    for word in words_list:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1 
            
    all_counts = list(word_counts.values())
    
    all_counts.sort(reverse=True)
    
    top_5_counts = all_counts[:5]
    
    top_5_sum = sum(top_5_counts)

    proportion = (top_5_sum / total_words) * 100

    print(f"Total number of words: {total_words}")
    print(f"Proportion of 5 most common words: {top_5_sum} / {total_words} = {proportion:.2f}%")

sample_text = "The world is mine out there The world is big and the world is beautiful but the world is also crazy so the world is mine"
calculate_word_proportion(sample_text)
# Task 5: Remove odd numbers from a list

def remove_odds(numbers_list):
    even_numbers = []
    
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
            
    return even_numbers

if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
    
    cut_down_list = remove_odds(original_list)
    
    print("Original list:", original_list)
    print("Cut-down list (evens only):", cut_down_list)
# Use filter() with a lambda to keep only words longer than 5 letters from a list.

words = ["Apple", "Banana", "Strawberry", "Pear", "Mango", "Pineapple", "Watermelon"]

filter_words = list(filter(lambda x : len(x) > 5, words))

print(filter_words)
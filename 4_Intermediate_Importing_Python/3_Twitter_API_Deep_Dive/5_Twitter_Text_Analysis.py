# Twitter text analysis

# Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many
# tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'. In the pre-exercise code, we have defined
# the following function word_in_text(), which will tell you whether the first argument (a word) occurs within
# the 2nd argument (a tweet).

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# You're going to iterate over the rows of the DataFrame and calculate how many tweets contain each of
# our keywords! The list of objects for each candidate has been initialized to 0.

# Start
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

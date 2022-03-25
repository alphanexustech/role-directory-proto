test_data_lookup = {
    "programmer": {
        "key_words": ["python", "javascript", "software"]
    }
}

sample_statement = """
As a software developer, my programs infterface with a variety of systems and complex
"""

# print(test_data_lookup)
# print(sample_statement)


# Write a function with one input string (api interface)
def sample_statement_handler(vrb):
    print(vrb)

def basic_function():
    print("hello mister anderson")

# sample_statement_handler(sample_statement)

# Find key words in the text with string matching (search)
# how do i write a for loop
key_words = ["python", "javascript", "software"]
for x in key_words:
    print(x)
    if x == "javascript":
        basic_function()

# how do i split a string on a specific character
# for x in "python":
#     print(x)



# Return roles that match the text from a lookup object (query results)

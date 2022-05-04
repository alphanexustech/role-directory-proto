test_data_lookup = {
    "programmer": {
        "key_words": ["python", "javascript", "software"]
    }
}

sample_statement = """
As a software developer, my programs infterface with a variety of systems, like javascript , python and complex
"""

# print(test_data_lookup)
# print(sample_statement)


# Write a function with one input string (api interface)
def query_results(sample_statement):
    # Find key words in the text with string matching (search)
    key_words = ["python", "javascript", "software"]
    string_list = sample_statement.split()
    for x in key_words:
        # print(x)
        for z in string_list:
            # print(z)
            if x == z: # "word" == 'word'
                role_finder(z)

def role_finder(m):
    print("match found", m)

query_results(sample_statement)





# Return roles that match the text from a lookup object (query results)

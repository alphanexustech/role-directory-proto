test_role_01 = [{
    "name": "programmer",
    "key_words": ["python", "javascript", "software"]
}]

test_role_02 = [{
    "name": "cyberserf",
    "key_words": ["cyberpolice", "backtraced", "consequences"]
}]


test_role_03 = [{
    "name": "pest control",
    "key_words": ["bugs", "insects", "ants"]
}]


test_roles = []
test_roles += test_role_01
test_roles += test_role_02
test_roles += test_role_03

sample_statement = """
As a software developer, my programs infterface with a variety of systems, like javascript , python and complex
"""

# print(test_data_lookup)
# print(sample_statement)


# Write a function with one input string (api interface)
def query_results(sample_statement, name, key_words):
    # Find key words in the text with string matching (search)
    string_list = sample_statement.split()
    for x in key_words:
        # print(x)
        for z in string_list:
            # print(z)
            if x == z: # "word" == 'word'
                role_finder(z, name)

def role_finder(m, name):
    print("match found", m, name)


for role in test_roles:
    query_results(sample_statement, role["name"], role["key_words"])





# Return roles that match the text from a lookup object (query results)

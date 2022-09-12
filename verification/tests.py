"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["adjacent_letters"],
            "answer": "adjacent_lrs"
        },
        {
            "input": [""],
            "answer": ""
        },
        {
            "input": ["aaa"],
            "answer": "a"
        },
        {
            "input": ["ABBA"],
            "answer": ""
        }
    ],
    "Extra": [
        {
            "input": ["lllllet's get rrready to the rrrummmmmble!"],
            "answer": "let's get ready to the rumble!"
        },
        {
            "input": ["abcd!dcba"],
            "answer": "abcd!dcba"
        },
        {
            "input": ["abcddcba"],
            "answer": ""
        },
        {
            "input": ["mississippi"],
            "answer": "m"
        },
        {
            "input": ["mammal"],
            "answer": "ml"
        },
        {
            "input": ["kinnikinnik"],
            "answer": "k", 
            "explanation": "That the real word! Check wiki"
        },
        {
            "input": ["tattarrattat"],
            "answer": "",
            "explanation": "That the real word! Check wiki"
        }
    ]
}

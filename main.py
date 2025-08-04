questions = [
    {
        "question": "What is the capital of France?",
        "options": {
            "a": "Paris",
            "b": "London",
            "c": "Berlin",
            "d": "Madrid"
        },
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "a": "Earth",
            "b": "Mars",
            "c": "Jupiter",
            "d": "Saturn"
        },
        "answer": "b"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": {
            "a": "Charles Dickens",
            "b": "William Shakespeare",
            "c": "Mark Twain",
            "d": "Jane Austen"
        },
        "answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": {
            "a": "Atlantic Ocean",
            "b": "Indian Ocean",
            "c": "Arctic Ocean",
            "d": "Pacific Ocean"
        },
        "answer": "d"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": {
            "a": "Oxygen",
            "b": "Gold",
            "c": "Silver",
            "d": "Iron"
        },
        "answer": "a"
    },
    {
        "question": "What is 9 x 9?",
        "options": {
            "a": "81",
            "b": "72",
            "c": "99",
            "d": "90"
        },
        "answer": "a"
    },
    {
        "question": "What year did India gain independence?",
        "options": {
            "a": "1945",
            "b": "1947",
            "c": "1950",
            "d": "1960"
        },
        "answer": "b"
    },
    {
        "question": "Which language is used to style web pages?",
        "options": {
            "a": "HTML",
            "b": "Python",
            "c": "CSS",
            "d": "C++"
        },
        "answer": "c"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {
            "a": "Oxygen",
            "b": "Carbon Dioxide",
            "c": "Nitrogen",
            "d": "Hydrogen"
        },
        "answer": "b"
    },
    {
        "question": "Which device is used to convert AC to DC?",
        "options": {
            "a": "Inverter",
            "b": "Rectifier",
            "c": "Transformer",
            "d": "Amplifier"
        },
        "answer": "b"
    }
]


def game(questions):
    print('Welcome the Game of Knowledge')
    score =  0
    for q in questions:
        print(q['question'])
        print(q['options'])

        user_ans = input('Enter Your Option:').lower()
        if(user_ans == q['answer']):
            print('Yes u are correct!! Won 10cr')
            score += 1
        else:
            print('LOOSER!!, 😢😢😢😢')      
    print(f'You were correctly answer {score} out of {len(questions)}')


game(questions)
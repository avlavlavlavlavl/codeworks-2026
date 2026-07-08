# My new quiz

score = 0

questions = [
    {
        "question": "1. Who is the best troll?",
        "options": ["A. Karkat", "B. Eridan", "C. Jimmy Trollpants", "D. Kurloz"],
        "answer": "A"
    },
    {
        "question": "2. Who is the worst troll?",
        "options": ["A. Karkat", "B. Eridan", "C. Jimmy Trollpants", "D. Trollvan"],
        "answer": "C"
    },
    {
        "question": "3. Who is not a Homestuck character?",
        "options": ["A. Karkat", "B. John", "C. Jimmy Trollpants", "D. FedoraFreak"],
        "answer": "B"
    }
]

print("====Welcome to the Best Quiz ever Ever. I would say I hope you like it, but I know you already will. Heh Heh.====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter Your Tuff Mango Answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("You did it. Congratulations. Good job. Wow. I'm so proud. Good. Yes.\n")
        score += 1
    else:
        print(f"You are a loser. I'm so, so ashamed. You should have said {q['answer']}.\n")

print("=" * 40)
print(f"Your Tuff Mango score is {score}/{len(questions)}")
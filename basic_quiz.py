print("Welcome to quiz game!")
playing = input("Do you want to play?  ")

score = 0

if playing.lower() != "yes":
    quit()
else:    
    print("Lets get started!")

answer = input("Who is the father of computer? ").lower()
if answer == "charles babbage":
    print("Correct")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect answer!")

answer = input("what is the full for form of CPU? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What is the full form of ROM? ").lower()
if answer == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect answer!")

print(f"you have {score} correct answers")

# This is the KeyboardTester class, which tests the keyboard.

class KeyboardTester:
    def __init__(self):
        self.exercises = [
            {
                "prompt": "First, please type in 'Hello, world.': ",
                "answer": "Hello, world.",
                "hint": "The correct answer is: Hello, world.\n"
            },
            {
                "prompt": "Now, give me the alphabet starting from 'a' to 'k': ",
                "answer": "abcdefghijk",
                "hint": "The correct answer is: abcdefghijk\n"
            },
            {
                "prompt": "I am a slow-moving animal with a shell. What am I?: ",
                "answer": "turtle",
                "hint": "The correct answer is: turtle\n"
            }
        ]
        
        self.failed_attempts = 0

    def opening_message(self):
        print ("--- Welcome to our keyboard tester ---\n")
        print ("You will go through a series of keyboard exercises to test your keyboard!\n")

    # Runs an individual exercise
    def run_exercise(self, prompt, answer, hint):
        attempts = 0
        
        while attempts < 3:
            user_input = input(prompt)
            if user_input.lower() == answer.lower():
                print ("Correct!\n")
                return True
            
            else:
                attempts += 1
                print ("Incorrect. Try again.")
                
        print(hint)
        self.failed_attempts += 1
        return False

    # Runs all the stored exercises
    def run(self):
        self.opening_message()
        for exercise in self.exercises:
            self.run_exercise(
                prompt=exercise["prompt"],
                answer=exercise["answer"],
                hint=exercise["hint"]
            )

        # Outcome of user input and final message    
        if self.failed_attempts == len(self.exercises):
            print ("Your keyboard might be broken... or there's personal issues with you.\n")
        else:
            print ("Congratulations! Your keyboard works perfectly!\n")


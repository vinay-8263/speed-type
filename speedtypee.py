import time

def calculate_typing_speed(text, elapsed_time):
    words = text.split()
    num_words = len(words)
    minutes = elapsed_time / 60
    speed = num_words / minutes
    return speed

def run_typing_test():
    print("Welcome to the Speed Typing Test!")
    print("Type the following sentence as fast as you can:")
    print("The quick brown fox jumps over the lazy dog.")
    print("Press Enter when you're ready to start.")
    input()

    start_time = time.time()

    print("Type the sentence now:")
    typed_text = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    speed = calculate_typing_speed(typed_text, elapsed_time)
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {speed:.2f} words per minute")

run_typing_test()
print("this was coded and devloped by I.Vinay Datta")
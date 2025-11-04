import time

leaderboard = []

def main():
    # The word to spell
    word = "pneumonoultramicroscopicsilicovolcanoconiosis"
    running = True
    while running:
        # Wait for user to give input
        com = input("Enter 'y' when ready, 'q' to quit, 'h' for high scores: ")
        
        # Start if 'y' is input
        if com == "y":
            run(word)

        # Quit if 'q' is input
        elif com == "q":
            print("Have a nice day!")
            running = False
        
        # Display top 5 scores
        elif com == "h":
            display_highscores()
        
        # If anything else is input, give error message and repeat loop
        else:
            print("Incorrect input, try again")

def run(word):
    # Countdown to start
    for i in range(3):
        print(3-i)
        time.sleep(1)
    flush_input()
    print("GO!")

    # Get time of start
    start = time.perf_counter_ns()

    # Wait for submitted word
    submitted_word = input()

    # Get stop time & determine difference
    stop = time.perf_counter_ns()
    duration = round((stop-start) / (10**9), ndigits=5)

    # Determine result
    if submitted_word.lower() == word.lower():
        print(f"Congratulations! You spelled {word} in {duration} seconds!")
        leaderboard.append([word, duration])
        leaderboard.sort()
    else:
        print("Oops! Try again next time!")

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def display_highscores():
    i = 1
    if len(leaderboard) != 0:
        print("TOP SPELLING TIMES")
        for score in leaderboard:
            print(f" {str(i).ljust(3)} - Time: {(str(score[1]) + "s").ljust(8)} - Word: {score[0]}")
            i += 1
    else:
        print("No Leaderboard Entries")

if __name__ == "__main__":
    main()

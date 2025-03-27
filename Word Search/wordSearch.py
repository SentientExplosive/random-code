import random
import time

wordGrid = []
width = 78
height = 32
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#OGwords = ["hello","world","are","tea","coal"]
#OGwords+ = ["hello","world","coal","tree","gourd","robe"]
words = []

def main():
    """Main game loop."""
    random.seed()
    fails = 0
    maxFails = 5
    readWordsFile()
    generating = True
    while generating:
        global wordGrid
        wordGrid = []
        generateWordArray()
        generateWordsearch()
        generating = False
        # try:
        #     generateWordsearch()
        #     generating = False
        # except:
        #     print("An error occurred in wordsearch generation")
        #     fails += 1
        #     if fails > maxFails:
        #         break

    displayWordsearch()
    displayWords()

def generateWordArray():
    for i in range(height):
        row = []
        for j in range(width):
            row.append("0")
        wordGrid.append(row)

def readWordsFile():
    file = open("words2.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        words.append(line.strip())
    file.close()
    print(words)

def generateWordsearch():
    for word in words:
        print(word)
        placing_word = True
        while placing_word:
            print("Attempting to place word")
            placing_word = False
            word_direc = random.randint(0,3) # 0-vert; 1-left diagonal; 2-horiz; 3-right diagonal
            backwards = random.randrange(0,2)
            if backwards:
                step = -1
            else:
                step = 1

            print(word_direc)
            print(backwards)

            start_pos = generateStartPos(backwards, word_direc, word)
            
            curr_pos = start_pos[:]
            
            print(start_pos)

            # check to see if the word can be inserted
            for i in range(len(word)):
                print(wordGrid[curr_pos[0]][curr_pos[1]])
                if wordGrid[curr_pos[0]][curr_pos[1]] != "0" and wordGrid[curr_pos[0]][curr_pos[1]] != word[i]:
                    placing_word = True
                    break
                
                # step in the direction the word is going in
                if word_direc == 0:
                    curr_pos[0] += step
                elif word_direc == 1:
                    curr_pos[0] += step
                    curr_pos[1] += step
                elif word_direc == 2:
                    curr_pos[1] += step
                elif word_direc == 3:
                    curr_pos[0] += step
                    curr_pos[1] -= step
                
                print(curr_pos)

        print("Placing word...")

        # reset curr_pos
        curr_pos = start_pos[:]
        print(curr_pos)
        print(start_pos)

        # add the word in
        for i in range(len(word)):
            if wordGrid[curr_pos[0]][curr_pos[1]] == "0":
                wordGrid[curr_pos[0]][curr_pos[1]] = word[i]
            
            # step in the direction the word is going in
            if word_direc == 0:
                curr_pos[0] += step
            elif word_direc == 1:
                curr_pos[0] += step
                curr_pos[1] += step
            elif word_direc == 2:
                curr_pos[1] += step
            elif word_direc == 3:
                curr_pos[0] += step
                curr_pos[1] -= step
            
            print(curr_pos)
    
        print("Done")

        displayWordsearch()
    
    print("Filling remaining spots")
    # Fill remaining spots in the 
    for i in range(height):
        for j in range(width):
            if wordGrid[i][j] == "0":
                index = random.randint(0,25)
                wordGrid[i][j] = alphabet[index]

def displayWordsearch():
    print("┌", end="")
    for i in range(2*width+1):
        print("-", end="")
    print("┐")

    for row in wordGrid:
        print("| ", end="")
        for letter in row:
            print(letter, end=" ")
        print("| ", end="")
        print("")
    
    print("└", end="")
    for i in range(2*width+1):
        print("-", end="")
    print("┘")

def displayWords():
    print("Words:", end="")
    val = 0
    for word in words:
        if val % 10 == 0:
            print("")
        print(f"{word:15}", end="")
        val += 1
    print("")

def generateStartPos(back, direc, word):
    if back:
        if direc == 0:
            start_pos = [height - random.randint(0,height-len(word)) - 1, random.randint(0,width-1)]
        elif direc == 1:
            start_pos = [height - random.randint(0,height-len(word)) - 1, width - random.randint(0,width-len(word)) - 1]
        elif direc == 2:
            start_pos = [random.randint(0,height-1), width - random.randint(0,width-len(word)) - 1]
        elif direc == 3:
            start_pos = [height - random.randint(0,height-len(word)) - 1, random.randint(0,width-len(word))]
    else:
        if direc == 0:
            start_pos = [random.randint(0,height-len(word)), random.randint(0,width-1)]
        elif direc == 1:
            start_pos = [random.randint(0,height-len(word)), random.randint(0,width-len(word))]
        elif direc == 2:
            start_pos = [random.randint(0,height-1), random.randint(0,width-len(word)),]
        elif direc == 3:
            start_pos = [random.randint(0,height-len(word)), width - random.randint(0,width-len(word)) - 1]
    
    return start_pos



if __name__ == "__main__":
    main()
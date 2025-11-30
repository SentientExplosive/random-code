# Searches log files for specific keywords, then grabs those lines and puts them into an output file
import os

# Variables for log file and output file names
outputFileName = "output"
outputFileExtension = ".txt"
startFileName = [2025,11,8,1]   # Year, Month, Day, lognum (1 or 2) of first log file to search
currFileName = startFileName    # Current File Name starts at first file name
endFileName = [2025,11,25,1]    # Year, Month, Day, lognum (1 or 2) of last log file to search
logFileExtension = ".log"
outputFiles = []

keywords = ["FengardTheGreat", "FengardTheGreat buy", "FengardTheGreat sell", "/pay FengardTheGreat", "FengardTheGreat issued server command: /pay", "hello"]
# keywords = ["hello"]

def main():
    running = True
    
    # Open output files
    try:
        for i in range(len(keywords)):
            file = open(f"{outputFileName}{i}{outputFileExtension}", "w+", encoding='utf8')
            print(f"Keyword: '{keywords[i]}'", file=file)
            outputFiles.append(file)
    except:
        print("Couldn't load output files")

    while running:
        # Generate file name
        folderAddress = os.getcwd() + "\\logs\\"
        year = currFileName[0]
        month = currFileName[1]
        day = currFileName[2]
        lognum = currFileName[3]
        if month < 10:
            month = "0" + str(month)
        if day < 10:
            day = "0" + str(day)
        
        logFileName = str(year) + "-" + str(month) + "-" + str(day) + "-" + str(lognum) + logFileExtension
        
        fileName = folderAddress + logFileName
        # print(fileName)

        try:
            # Open the file
            file = open(fileName, encoding='utf8')

            # Print to the file that you are starting to parse the given file
            for i in range(len(keywords)):
                print(f"Start of {logFileName}", file = outputFiles[i])

            # Read file contents line by line, search for keyword(s) in each line and sort the lines into the appropriate files
            for line in file:
                try:
                    processedLine = line.strip()
                    # print(f"line: {line}")
                    # print(f"processed line: {processedLine}")

                    # Check if keywords are in the line
                    for i in range(len(keywords)):
                        if keywords[i].lower() in processedLine.lower():
                            print(processedLine, file= outputFiles[i])
                except Exception as e:
                    print(f"An error occurred while processing line: {e}")

            # Print to the file that you have finished parsing the given file
            for i in range(len(keywords)):
                print(f"End of {logFileName}", file = outputFiles[i])

            # Close File
            print(f"Search through {logFileName} complete.")
            file.close()

        except FileNotFoundError:
            # Error opening the file
            print(f"Error: The file '{fileName}' was not found.")

        except Exception as e:
            # Other random errors that occur
            print(f"An error occurred: {e}")
        
        # Increment the file name to the next log file
        incrementFileName()
        
        # Checks if the last log file has been reached based on the day, month, and year
        for i in range(len(currFileName)):
            if currFileName[i] > endFileName[i] and i != 3:
                print("End reached")
                running = False
        
        # Checks if the last log file has been reached based on the log number
        # (special case in the instance you want it to end on a log file number that isn't the last file, i.e. stopping after lognum 1 instead of parsing through lognums 2+)
        if currFileName[0] == endFileName[0] and currFileName[1] == endFileName[1] and currFileName[2] == endFileName[2] and currFileName[3] > endFileName[3]:
            print("End reached")
            running = False
    
    # Close output files
    for file in outputFiles:
        file.close()

def incrementFileName():
    monthMax = [31,28,31,30,31,30,31,31,30,31,30,31]        # Max num of days in a month
    leapMonthMax = [31,29,31,30,31,30,31,31,30,31,30,31]    # Max num of days in a month during leap years
    
    # Current file name
    year = currFileName[0]
    month = currFileName[1]
    day = currFileName[2]
    lognum = currFileName[3]
    
    # Update all the variables in the log file name
    if lognum < 2:
        lognum += 1

    elif not isLeapYear():
        if day < monthMax[month-1]:
            lognum = 1
            day += 1

        elif day >= monthMax[month-1] and month < 12:
            lognum = 1
            day = 1
            month += 1
        
        elif month >= 12:
            lognum = 1
            day = 1
            month = 1
            year += 1

    elif isLeapYear(): # Special case for leap years, pretty much the same structure though just with leapMonthMax in place of monthMax
        if day < leapMonthMax[month-1]:
            lognum = 1
            day += 1

        elif day >= leapMonthMax[month-1] and month < 12:
            lognum = 1
            day = 1
            month += 1
        
        elif month >= 12:
            lognum = 1
            day = 1
            month = 1
            year += 1
    
    # Update current file name
    currFileName[0] = year
    currFileName[1] = month
    currFileName[2] = day
    currFileName[3] = lognum

def isLeapYear():
    # Determines whether the current year is a leap year or not and returns true or false, respectively
    year = currFileName[0]

    if (year % 4) == 0:
        return True
    elif (year % 100) == 0:
        if (year % 400) == 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
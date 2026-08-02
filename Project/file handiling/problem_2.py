# A program to count line,word,characters

def count(filename):
    try:
        with open(filename,"r") as file:
            lines=file.readlines()

            line_count=len(lines)
            word_count=sum(len(line.split()) for line in lines)
            char_count=sum(len(line) for line in lines)

            print(f"Lines:{line_count}")
            print(f"Words:{word_count}")
            print(f"Characters:{char_count}")
    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print("An error occured",e)        

filename=input("Enter name of file (with .txt extension):")
count(filename)

import csv
import sys

def get_data_from_csv() -> list:
    data = [] 
    with open("nytcrosswords.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def main():
    data = get_data_from_csv()
    for question in data:
        while True:
            print("The question: ", question['Clue'])
            print("Type 'quit' to exit")
            guess = str(input("Answer to the question: "))
            if guess == "quit":
                sys.exit()
            elif guess == question['Word']:
                print("correct")
                break
            else:
                print("Guess again\n")



if __name__ == "__main__":
    main()
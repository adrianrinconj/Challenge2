import csv

city_dict = {}

# Open the CSV file
with open('MontanaCounties.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row
    for row in reader:
        del row['License Plate Prefix']
        key = row['County Seat']
        del row['County Seat']
        city_dict[key] = row


def to_text_file(dict, filename):
    with open(filename, 'w', newline='') as file:
        for key, value in dict.items():
            file.write(f"{key},{value['County']}\n")


def load_from_text_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                city, county = line.strip().split(',')
                city_dict[city.lower()] = {'County': county}
        return city_dict
    except FileNotFoundError:
        return {}


def update_file(city, county, filename):
    with open(filename, 'a') as file:
        file.write(f"{city},{county}\n")


def main():
    city_dict = load_from_text_file('output.txt')
    q = False
    while True:
        stay_or_go = input("Please type 'city' to look up a city, or type 'exit' to exit\n").lower()
        if stay_or_go == 'city':
            user_input = input("Enter a city name\n").lower()
            if user_input in city_dict:
                print("County:", city_dict[user_input]['County'])
            else:
                new_county = input("That city does not exist in the database."
                                   " Please enter which county it is in.\n").lower()
                for value in city_dict.values():
                    if new_county in value['County'].lower():
                        q = True
                        print("That is a valid county")
                        print("City is being added to county")
                        update_file(user_input.capitalize(), new_county.capitalize(), 'output.txt')
                        break
                if q == False:
                    print("That is not a valid county")
        elif stay_or_go == 'exit':
            exit()
        else:
            print("That is not a valid input. Try again.\n")


if __name__ == '__main__':
    main()

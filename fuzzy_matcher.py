import csv
from fuzzywuzzy import fuzz

# Function to read names from a CSV file
def read_names_from_csv(file_path):
    names = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            names.append(row[0])  # Assuming names are in the first column
    return names

# Function to perform fuzzy matching
def fuzzy_match(names, threshold=80):
    matches = []
    
    for name in names:
        # Find matches for each name in the list
        for other_name in names:
            if name != other_name:  # Skip matching the name with itself
                similarity = fuzz.ratio(name, other_name)
                if similarity >= threshold:
                    matches.append([name, other_name, similarity])
    
    return matches

# Main function
def main():
    # Read names from a CSV file
    names = read_names_from_csv('names.csv')
    
    # Perform fuzzy matching
    matched_names = fuzzy_match(names)

    # Write the results to a CSV file
    with open('fuzzy_matches.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Matched Name', 'Similarity (%)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for match in matched_names:
            writer.writerow({'Name': match[0], 'Matched Name': match[1], 'Similarity (%)': match[2]})

    print("Results have been written to 'fuzzy_matches.csv'.")

# Run the main function
if __name__ == '__main__':
    main()

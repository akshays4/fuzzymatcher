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
    n = len(names)
    for i in range(n):
        for j in range(i+1, n):  # Compare each pair only once
            similarity = fuzz.ratio(names[i], names[j])
            if similarity >= threshold:
                matches.append([names[i], names[j], similarity])
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

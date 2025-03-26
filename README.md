# Fuzzy Matcher - Name Similarity Tool

This project allows you to perform fuzzy matching on a list of names and find names that are similar based on a similarity threshold (default is 80%).

You can input the list of names from a CSV file and the script will generate a CSV file with the matching names and their similarity percentages.

### Features:
- Read names from a CSV file (`names.csv`).
- Perform fuzzy matching of names based on similarity threshold (default 80%).
- Output the results into a new CSV file (`fuzzy_matches.csv`).

---

## Requirements

- **Python** (version 3.6 or higher)
- **fuzzywuzzy** library for fuzzy matching
- **PyInstaller** to create an executable file

---

## Installation

### 1. Clone or Download this Repository

You can clone or download this project to your local machine.

### 2. Install Python Dependencies

If you want to use the Python script directly, you need to install the required dependencies:

1. Install **Python** (if not installed):
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to your system's PATH during installation.

2. Install required Python libraries:
   Open a terminal or PowerShell and run:

   ```bash
   pip install fuzzywuzzy pyinstaller

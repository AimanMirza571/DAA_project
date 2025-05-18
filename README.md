# String Matching Algorithm Comparison

This project implements and compares two string matching algorithms: Boyer-Moore and Rabin-Karp. It provides a user-friendly web interface built with Streamlit to search for patterns in text and compare the performance of both algorithms.

## Features

- Case-insensitive pattern matching using Boyer-Moore and Rabin-Karp algorithms
- Real-time performance comparison between both algorithms
- Highlighting of matched patterns in the text
- Pattern replacement functionality
- Interactive web interface

## Requirements

- Python 3.7+
- Streamlit
- Pandas

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command in your terminal:
```bash
streamlit run app.py
```

## How to Use

1. Enter or paste the text you want to search in the text area
2. Enter the pattern you want to search for
3. (Optional) Enter replacement text if you want to replace the matches
4. Click "Search and Compare" to see the results
5. If matches are found and you entered replacement text, click "Replace Matches" to replace all occurrences

## Algorithm Comparison

- **Boyer-Moore Algorithm**: Generally more efficient for larger patterns and texts, as it can skip portions of the text
- **Rabin-Karp Algorithm**: Efficient for multiple pattern searching, uses rolling hash function

The application will show you which algorithm performed better for your specific case. 
# BookBot - Text Analysis Tool

BookBot is my first [Boot.dev](https://www.boot.dev) project! This command-line application analyzes text files and provides statistical insights about their content.

## 🎯 Project Overview

BookBot is a Python-based text analysis tool that reads book files and generates comprehensive statistics including word count and character frequency analysis. This project demonstrates fundamental Python programming concepts without using Object-Oriented Programming (OOP).

## 🚀 Features

- **Word Count Analysis**: Calculates the total number of words in a text file
- **Character Frequency Analysis**: Counts occurrences of each character (case-insensitive)
- **Sorted Character Report**: Displays alphabetical characters sorted by frequency
- **Command-Line Interface**: Simple CLI for easy interaction
- **Modular Design**: Separates concerns between main logic and statistical functions

## 💻 Technical Skills Demonstrated

### Core Python Concepts

1. **File I/O Operations**
   - Reading files using `with` statement for proper resource management
   - File path handling

2. **Functions and Modularity**
   - Creating reusable functions with clear responsibilities
   - Separating logic into modules (`main.py` and `stats.py`)
   - Function parameters and return values

3. **Data Structures**
   - **Dictionaries**: Used for character frequency counting
   - **Lists**: Used for storing and sorting character data
   - **List of Dictionaries**: Converting dictionary data for sorting

4. **Control Flow**
   - Conditional statements (`if/else`)
   - Loops (`for` loops for iteration)
   - Error handling with command-line arguments

5. **String Manipulation**
   - String splitting for word counting
   - Case conversion (`.lower()`)
   - Character validation (`.isalpha()`)

6. **Command-Line Arguments**
   - Using `sys.argv` for parsing command-line inputs
   - Input validation and user feedback

7. **Sorting and Lambda Functions**
   - Custom sorting with `key` parameter
   - Sorting complex data structures

8. **Module Imports**
   - Importing standard library modules (`sys`)
   - Importing custom modules and specific functions

## 📁 Project Structure

```
bookbot/
├── README.md          # Project documentation
├── main.py           # Main application entry point
├── stats.py          # Statistical analysis functions
└── books/            # Sample text files
    ├── frankenstein.txt
    ├── mobydick.txt
    └── prideandprejudice.txt
```

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/arduriki/bookbot.git
   cd bookbot
   ```

2. Run the analysis on a book:
   ```bash
   python3 main.py books/frankenstein.txt
   ```

### Example Output:
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
...
============= END ===============
```

## 🔍 Code Architecture

### `main.py`
- Entry point of the application
- Handles command-line arguments
- Orchestrates the analysis workflow
- Formats and displays results

### `stats.py`
- Contains all statistical analysis functions:
  - `get_num_words()`: Counts total words
  - `get_num_letters()`: Creates character frequency dictionary
  - `dict_into_list()`: Converts dictionary to list of dictionaries
  - `sort_on()`: Helper function for custom sorting

## 🎓 Learning Outcomes

Through this project, I've demonstrated proficiency in:

- **Problem Decomposition**: Breaking down complex problems into manageable functions
- **Code Organization**: Structuring code in a maintainable way
- **Python Fundamentals**: Working with core Python features without relying on advanced concepts
- **Algorithm Implementation**: Creating efficient solutions for text analysis
- **Clean Code Practices**: Writing readable, well-structured code
- **Command-Line Tools**: Building practical CLI applications

## 🚦 Future Enhancements

While this project focuses on procedural programming, potential improvements could include:
- Additional text statistics (sentences, paragraphs, readability scores)
- Support for multiple file formats
- Export functionality for analysis results
- Performance optimization for larger texts

## 📝 Note

This project intentionally avoids Object-Oriented Programming (OOP) concepts to demonstrate mastery of fundamental Python programming concepts including functions, data structures, control flow, and modular programming.

---

Built as part of the [Boot.dev](https://www.boot.dev) curriculum to solidify Python fundamentals.
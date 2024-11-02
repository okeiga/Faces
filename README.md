Functions and Variables
This project contains a series of Python programs that demonstrate basic input and output handling, string manipulation, and simple mathematical calculations. Below are descriptions of each file included in this repository:

Files
playback.py
This program prompts the user for input and outputs that same input, replacing each space with ... (three periods). It showcases string manipulation and user interaction.

faces.py
This file contains two functions:

convert(s: str) -> str: This function takes a string as input and replaces any occurrences of :) with 😊 (a slightly smiling face) and any occurrences of :( with 😞 (a slightly frowning face). All other text is returned unchanged.

main(): This function prompts the user for input, calls convert on that input, and prints the result.

einstein.py
This program prompts the user for mass as an integer (in kilograms) and outputs the equivalent energy in Joules, calculated using Einstein’s mass-energy equivalence formula. It demonstrates basic mathematical calculations and user input handling.

tip.py
This file includes two functions:

dollars_to_float(dollar_str: str) -> float: This function accepts a string formatted as $##.##, removes the leading $, and returns the amount as a float.

percent_to_float(percent_str: str) -> float: This function accepts a string formatted as ##%, removes the trailing %, and returns the percentage as a float.

Installation
To run these programs, ensure you have Python installed on your system. Clone the repository to your local machine:

Run git clone https://github.com/okeiga/Functions-and-Variables.git
Change into the project directory.

Usage
You can run each program by executing the corresponding Python file in your terminal. Follow the prompts provided by each program.
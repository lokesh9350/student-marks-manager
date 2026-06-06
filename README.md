# 🎓 Student Marks Manager

A Python project that helps students calculate their academic performance by taking obtained marks and maximum marks for multiple subjects.

## Features

* Accepts marks for multiple subjects
* Accepts maximum marks for each subject
* Validates user input
* Calculates total obtained marks
* Calculates total maximum marks
* Calculates overall percentage
* Assigns grades automatically
* Calculates percentage for each subject
* Finds highest subject percentage
* Finds lowest subject percentage
* Uses modular programming with functions

## Technologies Used

* Python

## Functions

### inp()

Takes input from the user:

* Number of subjects
* Obtained marks
* Maximum marks

Performs input validation.

### tot()

Calculates:

* Total obtained marks
* Total maximum marks

### per()

Calculates overall percentage.

### sub_per()

Calculates percentage of each subject individually.

### grd()

Assigns grade based on overall percentage.

### mxp()

Finds the highest subject percentage.

### mnp()

Finds the lowest subject percentage.

### out()

Displays the final result.

### main()

Controls the complete execution flow of the program.

## Grade Criteria

| Percentage   | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80 – 89      | A     |
| 70 – 79      | B     |
| 60 – 69      | C     |
| 50 – 59      | D     |
| Below 50     | F     |

## Sample Input

Enter number of subjects: 3

Enter marks of subject 1: 80

Enter maximum marks of subject 1: 100

Enter marks of subject 2: 45

Enter maximum marks of subject 2: 50

Enter marks of subject 3: 70

Enter maximum marks of subject 3: 100

## Sample Output

==============RESULT==============

Total Obtained            :195.0

Total maximum marks       :250.0

Percentage                :78.00%

Grade                     :B

Highest Subject Percentage:90.00%

Lowest Subject Percentage :70.00%

## Project Structure

Student-Marks-Manager

├── marksManager.py

├── README.md

└── .gitignore

## Concepts Used

* Functions
* Lists
* Loops
* Conditional Statements
* Input Validation
* Return Values
* Modular Programming
* Percentage Calculations

## Future Improvements

* Add subject names
* Display best subject name
* Display weakest subject name
* Save results to a file
* Support multiple students
* Menu-driven interface

## Author

Lokesh Sangdoya

B.Tech CSE (AI & ML)

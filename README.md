
This is a team problem, but you will be graded individually for your role.
The goal of this exercise is to implement a Python package for sorting integer lists using the DevOps software development approach.
Start by downloading the python package archive .zip file on your computer.
Warning: If working on Windows, some directories and files in the skeleton archive will not be visible because they start with a '.'. In the file browser, change the View to display "Hidden items".
To complete this assignment, you will need to:

Add a file: .pre-commit-config.yml which:
a. Limits maximal file size.
b. Runs the black and flake8 linters.
c. Detect presence of aws credentials private keys.
Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory, code should be documented using standard Python practices (there are several docstring styles).
a. Bubble sort – Measure CPU usage
b. Quick sort – Measure runtime
c. Insertion sort – Measure memory usage
Use psutil to measure https://psutil.readthedocs.io/en/latest/#
Implement linting, style checking using both flake8 and black.
Modify the GitHub actions workflow so that it tests and builds the package for all three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about Distributing Python packages.
a. This should run each test once for each OS, create a table in your repo README comparing the measurements.
Modify the README.md to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
Optional: Add a job to the workflow which uploads the wheel to TestPyPI. As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use abbreviation of your course number and team name.

Warning: Do not upload to the authoritative Python Package Index (PyPI).
**Possible work division, three sub-teams:
A. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
B. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
C. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).
Tasks

Establish a new GitHub repo (or create one as part of your team repo).
Download the python package exercise from Assignment 5, BrightSpace.
Have your ToolMaster/Version Control Master/Support Manager invite us (terry.yoo@maine.edu & john.sylvain@maine.edu) to share your GitHub repo.
Begin creating the .precommit YAML markup file, the GitHub workflow, tests (pytest), linters, and links.
Find/Write the python code for the sorting algorithms. Write and configure tests for your sorting algorithms.
Submit a write-up via BrightSpace, including a screen capture of your working workflow, and your individual contribution and impressions of CI/CD.

As a TEAM:
Create Repo (don't forget to invite me john.sylvain@maine.edu)
Implement workflow with github actions, lint, and test 3 sorting algorithms.
As an Individual:
Submit a write up including a screen capture of your working workflow, your individual contribution and impressions of CI/CD, as well as a minimum 300 word design for a test case for your project:
What framework do you need? What OS/systems will it be tested on? What cases are being considered? What is the input/output? What is the speed needed to pass? Type of test? Be creative and tailor the test to your project.
Coordinating with your team to have different test cases.
Grading
60% Repo:

Commit history (Did you do what you said you did?) – 15%
Working workflows – 30%
Table of test measurements – 10%
README – 5%

40% Writeup:

Individual contribution and impressions of CI/CD – 10%
Design for a test case – 30%

• Submit your individual report as either a PDF or MSWord document via BrightSpace
• Due 24-November-2025, 11:59:59 PM Eastern Time
(You can copy-paste the entire text above directly into Microsoft Word – it will preserve all formatting, headings, bold text, bullet points, and hyperlinks perfectly.)

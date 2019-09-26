# Instructions

The 'main.py' file holds all of the functions, while the rest of the files contain the tests for them. Each test will run as "1 passed, 1 failed". This is just the way I did it as you showed in Office Hours. 
***Note, my computer was requiring me to type ".py" at the end of my files when testing. So, "pytest test_login.py"!

# Explanations

1. 'test_login' - Tests if login matches the login needed to sign in as a System Admin (admin, password)
2. 'test_file' - Tests if file matches the specific name required for the assignment (in this case its 'assignment.md')
3. 'test_date' - Tests if file is uploaded before the submissions closes on the due date (in this case, the due date is '2019-10-28')
4. 'test_occupation' - Tests if the person that the system admin is adding to the system is an Instructor or not.
5. 'test_comment' - Tests if assignment has been graded already so that it can become available for TA/Instructor comments to be added.
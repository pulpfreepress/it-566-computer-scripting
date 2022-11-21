# IT 566: Computer Scripting Techniques - Fall 2022 - Midterm Exam

## Start Here
- Review this document entirely before proceeding
- You have 2 hours to complete the exam
    - At 2 hours hands-off keyboard, &
    - Demo what you have
- Work quietly during the exam
- **DO NOT COLLABORATE** with fellow students 
- **DO** refer to your notes, source code examples, or Google
- Take a break if you need to but maintain quiet 
- Let me know when you finish and are ready for me to grade 
- For grade, demo your program and show me the code you have written
    - Also show me your GitHub repository commit history
- When you have received your grade, pack your things quietly and leave 
- We will review the exam and any questions you may have next week

## Questions
- I’ll field general questions before the exam starts
- You get one free question during the exam
- You may ask two additional questions, but each question will dock 5 points off your exam grade
- A question must clarify a concept and be specific
- I will not debug your code! 
- I will not explain git commands!
- I will not answer a question I feel you could easily find by Googling!
- There’s no extra credit — so don’t ask


# STOP HERE UNTIL TOLD TO PROCEED


## Preparation
- Clone the git@github.com:pulpfreepress/it-566-computer-scripting.git repository
- Switch to the midterm branch:
    -- `git branch midterm`
- Copy the folder `exams/midterm_fa_2022` to your local projects repository
- Commit the `midterm_fa_2022` folder and its contents to your remote repository
    - In the data folder you will find a file named: `team_roster.json`
    - In the src folder you will find three files named: `main.py`, `roster_app.py`, and `roster.py`
- Create the virtual environment with `pipenv`
- Run the application to display the menu:
```
       Team Roster Application

		1. New Roster
		2. Load Roster
		3. Print Roster
		4. Add Team Members to Roster
		5. Save Roster
		7. Exit
```

- All the methods in the RosterApp class are either implemented or stubbed out. This means you can interact with the menu but no actual features work except menu choice 7: Exit.
- Most of your work, but not all, will be focused on completing the implemention of the `Roster` class

## Tasks
- Implement menu items 2 – 5
- Do this by completing the implementation of the `Roster` class declared in roster.py
- For menu item 3 — just print either the dictionary or the JSON to the console
    - No need to make it look pretty
- Commit your work to your remote repository as you complete each menu item
- For grade:
     - Demo menu items 2 – 5
     - Show me your GitHub repository commit history




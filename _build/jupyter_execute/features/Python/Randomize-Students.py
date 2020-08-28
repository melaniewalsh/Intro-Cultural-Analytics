# Make Random Student Groups

This page demonstrates how to make a Python function called `make_random_groups()` that will take a list of student names and randomly create a desired number of groups from the list.

### Import random module

import random

### Make list of students

Here's a list of student names. Yes, in this scenario, I'm teaching the NBA's all-star basketball players.

students = ['LeBron James',
'Giannis Antetokounmpo',                
'Kevin Durant',
'Steph Curry',
'Kyrie Irving',
'Joel Embiid', 
'Kawhi Leonard', 
'Paul George', 
'James Harden', 
'Kemba Walker', 
'Khris Middleton', 
'Anthony Davis', 
'Nikola Jokić', 
'Klay Thompson', 
'Ben Simmons', 
'Damian Lillard', 
'Blake Griffin', 
'Russell Westbrook', 
'D\'Angelo Russell', 
'LaMarcus Aldridge', 
'Nikola Vučević', 
'Karl-Anthony Towns', 
'Kyle Lowry', 
'Bradley Beal', 
'Dwyane Wade', 
'Dirk Nowitzki']

### Create `make_random_groups()` function

def make_random_groups(students, number_of_groups):
    
    #Shuffle list of students
    random.shuffle(students)
    
    #Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)
    
    #Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index+1}✨: {' / '.join(group)}\n")

### Use `make_random_groups()` function

make_random_groups(students, 10)

## Make Random Student Groups Explained in More Detail

### Shuffle the order of the students

random.shuffle(students)

### Extract a certain number of groups from the list of randomly shuffled students

all_groups = []
    
    for index in range(number_of_groups):
        
        group = students[index::number_of_groups]
        
        all_groups.append(group)

- `all_groups = []`
    - creates an empty list
- `range(number_of_groups)`
    - creates a sequence of numbers from 0 to the desired number of groups
- `index`
    - represents each number in that sequence
- `students[index::number_of_groups]`
    - extracts a group of students from the list by selecting the student at whatever position in the list `index` represents, then jumping forward by `number_of_groups` spots to select a student at that position in the list, etc
- `all_groups.append(group)`
    - adds each group to a master list

Let's say we have 15 students and want 5  random groups. For each `index` aka number in `range(5)` — (0,1,2,3,4) — we make a group by selecting `students[index::5]`.

**Group 1**  
`students[0::5]`  
We select the 0th student in the randomly shuffled list, then jump by 5 to select the 5th person in the list, and then jump by 5 to take the 10th person in the list.

**Group 2**   
`students[1::5]`  
We select the 1st student in the randomly shuffled list, then jump by 5 to select the 6th person in the list, and then jump by 5 to take the 11th person in the list.
 
**Group 3**  
`students[2::5]`  
We select the 2nd student in the randomly shuffled list, then jump by 5 to select the 7th person in the list, and then jump by 5 to take the 12th person in the list.

**Group 4**  
`students[3::5]`  
We select the 3rd student in the randomly shuffled list, then jump by 5 to select the 8th person in the list, and then jump by 5 to take the 13th person in the list.

**Group 5**  
`students[4::5]`
We select the 4th student in the randomly shuffled list, then jump by 5 to select the 9th person in the list, and then jump by 5 to take the 14th person in the list.

### Format and display each group

for index, group in enumerate(all_groups):
    print(f"✨Group {index+1}✨: {' / '.join(group)}\n")
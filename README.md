
## 2.12.4 Policy comparison
 
Task 2.12.5: Use these procedures to figure out which senator is most like Rhode Island
legend Lincoln Chafee. Then use these procedures to see who disagrees most with Pennsylvania’s Rick Santorum. Give their names.
Task 2.12.6: How similar are the voting records of the two senators from your favorite
state?
## 2.12.5 Not your average Democrat
Task 2.12.7: Write a procedure find average similarity(sen, sen set, voting dict)
that, given the name sen of a senator, compares that senator’s voting record to the voting
records of all senators whose names are in sen set, computing a dot-product for each, and
then returns the average dot-product.
Use your procedure to compute which senator has the greatest average similarity with
the set of Democrats (you can extract this set from the input file).
In the last task, you had to compare each senator’s record to the voting record of each
Democrat senator. If you were doing the same computation with, say, the movie preferences
of all Netflix subscribers, it would take far too long to be practical.
Next we see that there is a computational shortcut, based on an algebraic property of
the dot-product: the distributive property:
(v1 + v2) · x = v1 · x + v2 · x
Task 2.12.8: Write a procedure find average record(sen set, voting dict) that,
given a set of names of senators, finds the average voting record. That is, perform vector
addition on the lists representing their voting records, and then divide the sum by the number
of vectors. The result should be a vector.
Use this procedure to compute the average voting record for the set of Democrats, and
assign the result to the variable average Democrat record. Next find which senator’s
voting record is most similar to the average Democrat voting record. Did you get the same
result as in Task 2.12.7? Can you explain?
## 2.12.6 Bitter Rivals
Task 2.12.9: Write a procedure bitter rivals(voting dict) to find which two senators disagree the most.
This task again requires comparing each pair of voting records. Can this be done faster than
the obvious way? There is a slightly more efficient algorithm, using fast matrix multiplication.
We will study matrix multiplication later, although we won’t cover the theoretically fast
algorithms.
## 2.12.7 Open-ended study
You have just coded a set of simple yet powerful tools for sifting the truth from the sordid
flour of contemporary politics. Use your new abilities to answer at least one of the following
questions (or make up one of your own):
• Who/which is the most Republican/Democratic senator/state?
• Is John McCain really a maverick?
• Is Barack Obama really an extremist?
• Which two senators are the most bitter rivals?
• Which senator has the most political opponents? (Assume two senators are opponents
if their dot-product is very negative, i.e. is less than some negative threshold.)

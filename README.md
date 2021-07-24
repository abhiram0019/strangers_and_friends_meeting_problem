# strangers_and_friends_meeting_problem

A group of people go to a networking meetup1 . 

The rules of the meetup are simple:
a. Every individual must be acquainted with at least one other person attending the event
b. Adam can be introduced to Eve if and only if there is at least one person Bob who knows both of them
c. Adam cannot introduce himself to Eve without the aid of somebody like Bob. It is considered rude
d. If Bob knows both Adam and Eve, and they did not previously know each other, Bob must introduce one to the other 

This arrangement ensures that at the end of the meetup, people can be divided into a few sub-groups where people within each subgroup are acquainted with everyone within in it but nobody from other sub-groups.

 A few extreme examples are:
I. Two people who only know each other will not interact with anybody new as there is nobody who can introduce them to others.This sub-group will be one of the tiniest.
II. There’s always that person who knows 50 people in every room they walk into. 

Everybody who knows her will be introduced to all her contacts, contacts of her contacts and so on. This might end up becoming a big sub-group.
meetup.csv contains names of all people who attended the meetup.

The records look like:
Adam Bob
Bob Eve
Cindy Joe

The first line should be read as Adam knows Bob.
Write a function that takes in the CSV file (with path if applicable) as an argument and returns a list of sets – each set consisting people within a sub-group as described above. 
Output for the records in the above example would look like [{Adam, Bob, Eve}, {Cindy, Joe}] .

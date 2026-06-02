# Day 38 Mini Challenge


# Challenge 1 - Scholarship List
school_students = [
{"name": "iqra", "marks": 82},
{"name": "aamna", "marks": 69},
{"name": "fatima", "marks": 95},
{"name": "khadiza", "marks": 80}
]
scholarship_list = []
for student in school_students:
    if student["marks"] >= 80:
        scholarship_list.append(student["name"])
print("Scholarship List:", scholarship_list)



# Challenge 2 - Warehouse Alert
products = {
"pen": 18,
"book": 1,
"pencil": 8,
"toys": 4,
"teddy": 10,
"mini car": 3,
"mack": 2
}
for item in products:
    if products[item] < 5:
        print("Alert!", item, "left:", products[item])



# Challenge 3 - Tournament Winner
players = [
{"name": "rohan", "points": 4240},
{"name": "suman", "points": 729393},
{"name": "choi", "points": 29393}
]
winner_points = players[0]["points"]
winner_name = players[0]["name"]
for player in players:
    if player["points"] > winner_points:
        winner_points = player["points"]
        winner_name = player["name"]
print("Winner:", winner_name)
print("Points:", winner_points)



# Challenge 4 - Attendance Report
data = {
"suman": "present",
"priya": "absent",
"riya": "present",
"rohan": "present",
"laina": "absent"
}
present_report = []
for student in data:
    if data[student] == "present":
        present_report.append(student)
print("Attendance Report:", present_report)



# Challenge 5 - Recommended Movies
movies = [
{"name": "interstellar", "rating": 8.9},
{"name": "dil de chuke sanam", "rating": 7.3},
{"name": "hum aapke hai kaun", "rating": 9},
{"name": "bahubali", "rating": 8}
]
recommended = []
for movie in movies:
    if movie["rating"] >= 8:
        recommended.append(movie["name"])
print("Recommended Movies:", recommended)



# Challenge 6 - User Access
users = [
{"name": "naina", "age": 17},
{"name": "laina", "age": 23},
{"name": "nainu", "age": 17},
{"name": "asuno", "age": 22}
]
for user in users:
    if user["age"] >= 18:
        print(user["name"], "can access")



# Challenge 7 - Smart Analysis
scores = [83, 24, 48, 20, 80, 87, 67, 55, 90, 32]
highest = scores[0]
count = 0
for score in scores:
    if score > highest:
        highest = score
    if score >= 50:
        count += 1
print("Highest Score:", highest)
print("Players Scoring 50+:", count)


# Challenge 8 - Library Report
library = {
"the power": 400,
"human being": 48,
"ai": 60,
"agentic ai": 530,
"love": 313,
"thinking": 70
}
popular_books = []
for book in library:
    if library[book] >= 100:
        popular_books.append(book)
print("Popular Books:", popular_books)
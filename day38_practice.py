# Day 38 Practice
# Topic: Collections in Logic

# Attendance Counter
class3 = ["present", "absent", "present", "present", "absent", "present"]
present_count = 0
for status in class3:
    if status == "present":
        present_count += 1
print("Total Present Students:", present_count)


# Product Price Filter
cart = {
    "pen": 10,
    "books": 200,
    "toys": 20000,
    "mini car": 304899,
    "makeup kit": 3999,
    "teddy bear": 300,
    "bag": 900
}
for product in cart:
    if cart[product] > 500:
        print(product, "->", cart[product])


# Highest Score Finder
scores = [200, 420, 540, 200, 440, 300, 590]
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print("Highest Score:", highest)


# Contact Directory
contacts = {
    "riya": "98393..",
    "rohan": "39382..",
    "priya": "39409..",
    "suman": "93838.."
}
for person in contacts:
    print(person, contacts[person])


# Low Stock Checker
store = {
    "book": 4,
    "toys": 8,
    "pen": 32,
    "mouse": 19,
    "mobile": 4,
    "equipments": 9,
    "glasses": 23
}
for item in store:
    if store[item] < 10:
        print(item, "left:", store[item])


# Reading List
books = [
    "science",
    "computer science",
    "ai",
    "generative ai",
    "agentic ai"
]
for book in books:
    print("Reading", book)


# Player Leaderboard
players = [
    {"name": "choi", "points": 39873},
    {"name": "rkive", "points": 24355909},
    {"name": "nainu", "points": 4999999}
]
highest = players[0]["points"]
name = players[0]["name"]
for player in players:
    if player["points"] > highest:
        highest = player["points"]
        name = player["name"]
print(name, highest)


# Adult User Filter
users = [
    {"name": "riya", "age": 30},
    {"name": "priya", "age": 23},
    {"name": "suman", "age": 17},
    {"name": "rohan", "age": 42}
]
for person in users:
    if person["age"] >= 18:
        print(person["name"])
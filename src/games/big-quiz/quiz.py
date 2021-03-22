import pgzrun
from pgzero.clock import schedule_interval
from pgzero.rect import Rect

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 20

q1 = ["What food is Japan famous for?", "Ramen", "Sushi", "Fish", "Tempura", 2]
q2 = ["What is 1/8 of 200?", "20", "50", "40", "25", 4]
q3 = ["What color do you get when you mix pink, orange, and white?", "magenta", "peach", "light pink", "light purple", 2]
q4 = ["Which American Football Team won the 2021 Superbowl?", "Chiefs", "Patriots", "Jaguars", "Buccaneers", 4]
q5 = ["What is another name for Dihydrogen Monoxide?", "Water", "Oil", "Soap", "Silicon Gel", 1]
q6 = ["How many stuffed animals does Shpitzy have?", "13", "9", "16", "19", 1]
q7 = ["What planet is 6th away from the sun?", "Jupiter", "Uranus", "Saturn", "Mars", 3]
q8 = ["Where is Origami originally from?", "Japan", "USA", "China", "UK", 3]
q9 = ["What is the tallest mountain in Massachusetts?", "Mt. Washington", "Mt. Wachusett", "Great Blue Hill", "Mt. Greylock", 4]
q10 = ["How many boardgames are on the bookshelf in our living room?", "5", "17", "15", "12", 2]
q11 = ["How many cookbooks does ima have?", "36", "24", "11", "41", 1]
q12 = ["How many plants do we have in our house?", "6", "8", "9", "7", 4]
q13 = ["How many letters does shpitzy's full (real) name have?", "13", "14", "12", "15", 3]
q14 = [""]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]
num_of_qs = len(questions)
question = questions.pop(0)


def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color="black")
    screen.draw.textbox(question[0], main_box, color="black")

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color="black")
        index += 1


def game_over():
    global question, time_left
    message = f"Game over. You got %s out of {num_of_qs} questions correct!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left

    score += 1
    if questions:
        question = questions.pop(0)
        time_left = 20
    else:
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == question[5]:
                correct_answer()
            else:
                game_over()
        index += 1


def update_time_left():
    global time_left

    if time_left:
        time_left -= 1
    else:
        game_over()


schedule_interval(update_time_left, 1.0)
pgzrun.go()

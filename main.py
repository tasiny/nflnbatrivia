import tkinter as tk
import pygame
from data import question_bank_1
from nba_data import nba_question_bank
import random
import os
from PIL import ImageTk, Image

blue_team_score = 0
red_team_score = 0
image_folder = "nfl_pngs"
image_folder_nba = "nba_pngs"
current_timer = "0"
trivia_dict = question_bank_1
trivia_dict_nba = nba_question_bank


def turn_nfl_on():
    def stop_timer():
        global current_timer
        if current_timer:
            main_screen.after_cancel(current_timer)
            timer_button.config(text="Timer")
            pygame.mixer.music.stop()

    def show_question():
        global current_question, answer
        current_question = random.choice(list(trivia_dict.keys()))
        answer = trivia_dict[current_question]
        question_label.config(text=current_question)
        result_label.config(text="")

    def check_answer():
        global answer, blue_team_score
        result_label.config(text=f"The correct answer is: {answer}", fg="red")

    def add_score_blue(amount):
        global blue_team_score
        blue_team_score += amount
        blue_score_label.config(text=f"Blue Team: {blue_team_score}")

    def add_score_red(amount):
        global red_team_score
        red_team_score += amount
        red_score_label.config(text=f"Red Team: {red_team_score}")

    def display_png():
        top = tk.Toplevel()
        top.minsize(width=300, height=300)
        top.title("Identify the player!")
        png_list = []
        for filename in os.listdir(image_folder):
            png_list.append(filename)
            f = os.path.join(image_folder, random.choice(png_list))
        canvas = tk.Canvas(top, width=300, height=300)
        canvas.pack()
        img = tk.PhotoImage(file=f)
        canvas.image = img
        canvas.create_image(150, 150, image=img)

    def start_timer():
        global current_timer
        if current_timer:
            main_screen.after_cancel(current_timer)
            current_timer = "0"
        play_music(160)

        # starting music
        pygame.mixer.init()
        pygame.mixer.music.load("NFL Primetime Song 1.mp3")
        pygame.mixer.music.play(loops=1)

    def play_music(count):
        # set the timer
        count_minute = int(count / 60)
        count_second = count % 60
        if count > 0:
            global current_timer
            current_timer = main_screen.after(1000, play_music, count - 1)
        if count_second == 0:
            formatted_timer = f"{count_minute}:{count_second}0"
        elif count_second < 10:
            formatted_timer = f"{count_minute}:0{count_second}"

        else:
            formatted_timer = f"{count_minute}:{count_second}"
        timer_button.config(text=formatted_timer, foreground="red")

    # Removing items from Main Screen grid
    main_title_label.grid_remove()
    main_title_label.destroy()
    main_instruction_label.grid_remove()
    main_instruction_label.destroy()
    nba_logo_button.grid_remove()
    nba_logo_button.destroy()
    nfl_logo_button.grid_remove()
    nfl_logo_button.destroy()
    frame.grid_remove()
    frame.destroy()
    main_screen.title("NFL Trivia Game")
    nfl_frame = tk.Frame(main_screen, width=100, height=100)
    nfl_frame.grid(row=0, column=0, columnspan=4)

    # Creating NFL Trivia Screen Widgets
    nfl_logo_label = tk.Label(nfl_frame, image=nfl_png)
    question_label = tk.Label(main_screen, text="", font=("TkDefaultFont", 16), wraplength=500, justify="center", padx=25, pady=15)
    result_label = tk.Label(main_screen, text="", font=("TkDefaultFont", 16), wraplength=500, justify="center", pady=10)
    check_button = tk.Button(main_screen, text="Check", font=("TkDefaultFont", 16), command=check_answer)
    next_question_button = tk.Button(main_screen, text="Next Question", font=("TkDefaultFont", 16), command=show_question)
    blue_add_score_button = tk.Button(main_screen, text="Add", font=("TkDefaultFont", 16), bg="blue", fg="white",
                                      command=lambda: add_score_blue(1))
    blue_score_label = tk.Label(main_screen, text="Blue Team: 0", font=("TkDefaultFont", 16))
    red_score_label = tk.Label(main_screen, text="Red Team: 0", font=("TkDefaultFont", 16))
    red_add_score_button = tk.Button(main_screen, text="Add", font=("TkDefaultFont", 16), bg="red", fg="white",
                                     command=lambda: add_score_red(1))
    bonus_question_button = tk.Button(main_screen, text="Bonus", font=("TkDefaultFont", 16), command=display_png)
    timer_button = tk.Button(main_screen, text="Timer", font=("TKDefaultFont", 16), command=start_timer)
    stop_timer_button = tk.Button(main_screen, text="STOP", font=("TKDefaultFont", 16), command=stop_timer, foreground="red")

    # Grid for NFL Trivia Screen
    nfl_logo_label.grid(row=0, column=0, columnspan=4)
    question_label.grid(row=1, column=0, columnspan=4)
    check_button.grid(row=2, column=1, columnspan=2)
    next_question_button.grid(row=3, column=1, columnspan=2)
    result_label.grid(row=4, column=0, columnspan=4)
    blue_add_score_button.grid(row=5, column=0)
    blue_score_label.grid(row=5, column=1)
    red_score_label.grid(row=5, column=2)
    red_add_score_button.grid(row=5, column=3)
    bonus_question_button.grid(row=2, column=3)
    timer_button.grid(row=2, column=0)
    stop_timer_button.grid(row=3, column=0)

    show_question()


def turn_nba_on():
    def show_question():
        global current_question, answer
        current_question = random.choice(list(trivia_dict_nba.keys()))
        answer = trivia_dict_nba[current_question]
        question_label.config(text=current_question)
        answer_entry.delete(0, 'end')
        result_label.config(text="")

    def check_answer():
        global answer, blue_team_score
        user_answer = answer_entry.get()
        if user_answer == answer:
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text=f"The correct answer is: {answer}", fg="red")

    def add_score_blue(amount):
        global blue_team_score
        blue_team_score += amount
        blue_score_label.config(text=f"Blue Team: {blue_team_score}")

    def add_score_red(amount):
        global red_team_score
        red_team_score += amount
        red_score_label.config(text=f"Red Team: {red_team_score}")

    def display_png():
        top = tk.Toplevel()
        top.minsize(width=300, height=300)
        top.title("Identify the player!")
        png_list = []
        for filename in os.listdir(image_folder_nba):
            png_list.append(filename)
            f = os.path.join(image_folder_nba, random.choice(png_list))
        canvas = tk.Canvas(top, width=300, height=300)
        canvas.pack()
        img = tk.PhotoImage(file=f)
        canvas.image = img
        canvas.create_image(150, 150, image=img)

    def play_music(count):
        # set the timer
        count_minute = int(count / 60)
        count_second = count % 60
        if count > 0:
            global current_timer
            current_timer = main_screen.after(1000, play_music, count - 1)
        if count_second == 0:
            formatted_timer = f"{count_minute}:{count_second}0"
        elif count_second < 10:
            formatted_timer = f"{count_minute}:0{count_second}"

        else:
            formatted_timer = f"{count_minute}:{count_second}"
        timer_button.config(text=formatted_timer, foreground="red")

    def start_timer():
        global current_timer
        if current_timer:
            main_screen.after_cancel(current_timer)
            current_timer = "0"
        play_music(160)

        # starting music
        pygame.mixer.init()
        pygame.mixer.music.load("nba_theme_song.mp3")
        pygame.mixer.music.play(loops=1)

    def stop_timer():
        global current_timer
        if current_timer:
            main_screen.after_cancel(current_timer)
            timer_button.config(text="Timer")
            pygame.mixer.music.stop()

    # Removing items from Main Screen grid
    main_title_label.grid_remove()
    main_title_label.destroy()
    main_instruction_label.grid_remove()
    main_instruction_label.destroy()
    nba_logo_button.grid_remove()
    nba_logo_button.destroy()
    nfl_logo_button.grid_remove()
    nfl_logo_button.destroy()
    frame.grid_remove()
    frame.destroy()
    main_screen.title("NBA Trivia Game")
    nba_frame = tk.Frame(main_screen, width=100, height=100)
    nba_frame.grid(row=0, column=0, columnspan=4)

    # Creating NBA Widgets
    nba_logo_label = tk.Label(nba_frame, image=nba_jpg, pady=25)
    question_label = tk.Label(main_screen, text="", font=("TkDefaultFont", 16), wraplength=500, justify="center", pady=15, padx=25)
    answer_entry = tk.Entry(main_screen, font=("TkDefaultFont", 16))
    result_label = tk.Label(main_screen, text="", font=("TkDefaultFont", 16), wraplength=500, justify="center", pady=10)
    check_button = tk.Button(main_screen, text="Check", font=("TkDefaultFont", 16), command=check_answer)
    next_question_button = tk.Button(main_screen, text="Next Question", font=("TkDefaultFont", 16), command=show_question)
    blue_score_label = tk.Label(main_screen, text="Blue Team: 0", font=("TkDefaultFont", 16))
    blue_add_score_button = tk.Button(main_screen, text="Add", font=("TkDefaultFont", 16), bg="blue", fg="white",
                                      command=lambda: add_score_blue(1))
    red_score_label = tk.Label(main_screen, text="Red Team: 0", font=("TkDefaultFont", 16))
    red_add_score_button = tk.Button(main_screen, text="Add", font=("TkDefaultFont", 16), bg="red", fg="white",
                                     command=lambda: add_score_red(1))
    bonus_question_button = tk.Button(main_screen, text="Bonus", font=("TkDefaultFont", 16), command=display_png)
    timer_button = tk.Button(main_screen, text="Timer", font=("TKDefaultFont", 16), command=start_timer)
    stop_timer_button = tk.Button(main_screen, text="STOP", font=("TKDefaultFont", 16), command=stop_timer, foreground="red")

    # Grid for NBA Widgets
    nba_logo_label.grid(row=0, column=0, columnspan=4)
    question_label.grid(row=1, column=0, columnspan=4)
    check_button.grid(row=2, column=1, columnspan=2)
    next_question_button.grid(row=3, column=1, columnspan=2)
    result_label.grid(row=4, column=0, columnspan=4)
    blue_add_score_button.grid(row=5, column=0)
    blue_score_label.grid(row=5, column=1)
    red_score_label.grid(row=5, column=2)
    red_add_score_button.grid(row=5, column=3)
    bonus_question_button.grid(row=2, column=3)
    timer_button.grid(row=2, column=0)
    stop_timer_button.grid(row=3, column=0)

    show_question()


# Screen for choosing NFL or NBA
main_screen = tk.Tk()
main_screen.title("Sports Trivia Game")

# NFL Logo
frame = tk.Frame(main_screen, width=100, height=100)
frame.grid(row=2, column=0, columnspan=2, pady=25)
nfl_png = ImageTk.PhotoImage(Image.open("nfl_logo.png"))

# NBA Logo
nba_jpg = ImageTk.PhotoImage(Image.open("nba_logo.jpg"))

# Labels
main_title_label = tk.Label(main_screen, text="Welcome to Sports Trivia", font=("TkDefaultFont", 36), justify="center", pady=10, padx=25)
main_instruction_label = tk.Label(main_screen, text="Please choose the type of trivia you want", font=("TkDefaultFont", 20), justify="center", pady=10, padx=25)
nfl_logo_button = tk.Button(frame, image=nfl_png, justify="left", command=turn_nfl_on)
nba_logo_button = tk.Button(frame, image=nba_jpg, justify="right", command=turn_nba_on)

# Grid
main_title_label.grid(row=0, column=0, columnspan=2)
main_instruction_label.grid(row=1, column=0, columnspan=2)
nfl_logo_button.grid(row=2, column=0, padx=30)
nba_logo_button.grid(row=2, column=1, padx=30)

main_screen.mainloop()

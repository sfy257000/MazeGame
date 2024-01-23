from flask import Flask, render_template, request
import os
import tty
import termios
import sys
import time
from datetime import datetime, timedelta


app = Flask(__name__)

def move_player(move, player_position):
    new_position = list(player_position)
    if move == 'w' and player_position[0] > 0 and maze[player_position[0] - 1][player_position[1]] != '#':
        new_position[0] -= 1
    elif move == 's' and player_position[0] < len(maze) - 1 and maze[player_position[0] + 1][player_position[1]] != '#':
        new_position[0] += 1
    elif move == 'a' and player_position[1] > 0 and maze[player_position[0]][player_position[1] - 1] != '#':
        new_position[1] -= 1
    elif move == 'd' and player_position[1] < len(maze[0]) - 1 and maze[player_position[0]][player_position[1] + 1] != '#':
        new_position[1] += 1

    return tuple(new_position)

def print_maze(player_position, remaining_time, score):
    os.system('clear') 
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) == player_position:
                print('P', end=' ')
            elif maze[i][j] == 'S':
                print('S', end=' ')
            elif maze[i][j] == 'E':
                print('E', end=' ')
            elif maze[i][j] == '#':
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
    print(f"Remaining Time: {remaining_time.seconds} seconds")
    print(f"Score: {score} points")

def get_char():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global maze


    map_choice = request.form.get('map_choice')
    
    if map_choice not in ['a', 'b', 'c']:
        return "請輸入有效的選項。"

    if map_choice == 'a':
        maze = [
            ['S', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'E', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
    elif map_choice == 'b':
        maze = [
            ['S', ' ', '#', '#', '#', '#', '#', '#', 'E', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
    elif map_choice == 'c':
        maze = [
            ['S', ' ', '#', '#', '#', 'E', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', '#', '#'],
            ['#', '#', '#', ' ', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#'],
        ]

    player_position = (0, maze[0].index('S'))
    start_time = datetime.now()
    score = 0

    while True:
        elapsed_time = datetime.now() - start_time
        remaining_time = timedelta(seconds=30) - elapsed_time
        if remaining_time.total_seconds() <= 0:
            print_maze(player_position, remaining_time, score)
            return "時間到！遊戲結束。分數：0。"

        print_maze(player_position, remaining_time,score)
        
        if maze[player_position[0]][player_position[1]] == 'E':
            score = int(100 * (remaining_time.total_seconds() / 30))
            return render_template('game_over.html', score=score)

        move = get_char()
        
        if move == 'q':
            print_maze(player_position, remaining_time, score)
            return f"遊戲結束。分數：{score}"
        player_position = move_player(move, player_position)

if __name__ == '__main__':
    app.run(debug=True)


# 🎮 Breakout Game

A classic **Breakout Game** built using Python's Turtle graphics module. Control the paddle, bounce the ball, and break the bricks to increase your score.

## 📌 About the Project

This project is a Python-based arcade game inspired by the classic Breakout game. The player controls a paddle to keep the ball from falling and uses it to break bricks.

The game includes colored bricks, score tracking, ball bouncing, and a retry option after Game Over.

## ✨ Features

- 🎾 Ball movement and bouncing
- 🧱 Randomly generated colored bricks
- 🏓 Paddle movement using keyboard controls
- 🏆 Score tracking
- ⚡ Changing ball speed during gameplay
- 🔄 Retry option after Game Over
- 🐍 Built using Python Turtle graphics

## 🛠️ Technologies Used

- **Python** — Game logic
- **Turtle** — Graphics and game objects
- **Random** — Random brick generation
- **Time** — Controlling game speed

## 📂 Project Structure

```text
Breakout-Game/
│
├── main.py
├── brick.py
├── ball.py
├── score.py
└── README.md
```

`__pycache__` may also be created automatically by Python when the modules are imported.

## 🚀 How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the main Python file:

```bash
python main.py
```

Make sure `brick.py`, `ball.py`, and `score.py` are in the same folder as `main.py`.

## 🎮 Controls

| Key | Action |
|---|---|
| ⬅️ Left Arrow | Move paddle left |
| ➡️ Right Arrow | Move paddle right |
| R | Retry after Game Over |

## 🎯 Objective

- Keep the ball from falling below the paddle.
- Hit the bricks with the ball.
- Earn points by breaking bricks.
- Try to achieve a higher score!

## 📚 What I Learned

- Creating and managing objects using Python Turtle
- Working with classes and imported modules
- Handling keyboard events
- Using lists to manage multiple game objects
- Implementing collision detection
- Managing game loops and score tracking
- Generating game elements randomly

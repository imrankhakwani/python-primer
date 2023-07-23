import turtle
import random


class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = "right"

    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == "right":
            x += 1
        elif self.direction == "left":
            x -= 1
        elif self.direction == "up":
            y -= 1
        elif self.direction == "down":
            y += 1
        self.body.insert(0, (x, y))
        self.body.pop()

    def check_collision(self):
        head = self.body[0]
        x, y = head
        if x < 0 or x >= 20 or y < 0 or y >= 20:
            return True
        for body in self.body[1:]:
            if body == head:
                return True
        return False


def main():
    snake = Snake()
    screen = turtle.Screen()
    screen.setup(width=200, height=200)
    screen.bgcolor("black")
    turtle.hideturtle()
    while True:
        snake.move()
        if snake.check_collision():
            break
        screen.clear()
        for body in snake.body:
            turtle.goto(body[0], body[1])
            turtle.dot()
        turtle.update()


if __name__ == "__main__":
    main()

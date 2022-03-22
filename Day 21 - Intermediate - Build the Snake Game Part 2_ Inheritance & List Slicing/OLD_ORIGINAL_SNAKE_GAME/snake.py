from turtle import Turtle

INITIAL_BLOCKS = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self) -> None:
        self.blocks = []
        self.create_snake()
        self.FIRST_BLOCK = self.blocks[0]

    def create_snake(self, x=0, y=0, initial_block=INITIAL_BLOCKS):
        for _ in range(initial_block):
            new_block = Turtle('square')
            new_block.color('white')
            new_block.up()
            new_block.goto(x, y)
            x -= 20
            self.blocks.append(new_block)

    def move(self):
        for block_number in range(len(self.blocks) - 1, 0, -1):
            self.blocks[block_number].goto(self.blocks[block_number - 1].pos())
        self.blocks[0].forward(20)

    def grow_bigger(self):
        self.create_snake(self.blocks[-1].xcor(), self.blocks[-1].ycor(), 1)

    def up(self):
        if self.FIRST_BLOCK.heading() != DOWN:
            self.FIRST_BLOCK.setheading(UP)

    def left(self):
        if self.FIRST_BLOCK.heading() != RIGHT:
            self.FIRST_BLOCK.setheading(LEFT)

    def right(self):
        if self.FIRST_BLOCK.heading() != LEFT:
            self.FIRST_BLOCK.setheading(RIGHT)

    def down(self):
        if self.FIRST_BLOCK.heading() != UP:
            self.FIRST_BLOCK.setheading(DOWN)

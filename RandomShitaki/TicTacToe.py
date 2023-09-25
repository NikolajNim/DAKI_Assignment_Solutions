import pygame as pg
class Hitbox:
    def __init__(self, x, y, width, height, id):
        self.rect = pg.Rect(x, y, width, height)
        self.id = id

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
pg.init()
screen = pg.display.set_mode((1000, 1000))
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
width = screen.get_width()
height = screen.get_height()
center = (width / 2, height / 2)

pg.draw.line(screen, black, (width / 3, 0), (width / 3, height), 5)
pg.draw.line(screen, black, (width / 3 * 2, 0), (width / 3 * 2, height), 5)
pg.draw.line(screen, black, (0, height / 3), (width, height / 3), 5)
pg.draw.line(screen, black, (0, height / 3 * 2), (width, height / 3 * 2), 5)

hitboxes = []
box_width = width // 3
box_height = height // 3



for i in range(3):
    for j in range(3):
        x = i * box_width
        y = j * box_height
        hitbox = Hitbox(x, y, box_width, box_height, (i, j))
        hitboxes.append(hitbox)







run_flag = True
while run_flag is True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_flag = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                for hitbox in hitboxes:
                    if hitbox.is_clicked(mouse_pos):
                        print(f"{hitbox.id} was clicked")

    pg.display.flip()


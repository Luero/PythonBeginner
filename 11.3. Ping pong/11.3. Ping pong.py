# Пинг-понг на 1 игрока
# Пользователь манипулирует ракеткой, шарик отскакивает от трех сторон поля
# Created by Luero, 24/07/2022

from livewires import games, color
import random

games.init(screen_width = 480, screen_height = 650, fps = 50)

class Rocket(games.Sprite):
    image = games.load_image("rocket.jpg")
    def __init__(self):
        super(Rocket, self).__init__(image = Rocket.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
        self.score = games.Text(value = 0,
                                size = 25,
                                color = color.black,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.right > games.screen.width:
            self.right = games.screen.width
        if self.left < 0:
            self.left = 0
        self.collision_with_ball()

    def collision_with_ball(self):
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            
class Ball(games.Sprite):
    image = games.load_image("ball.jpg")
    def __init__(self):
        super(Ball, self).__init__(image = Ball.image,
                                   x = random.randrange(games.screen.width),
                                   top = 0, dx = 3, dy = 3)

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.destroy()
            self.game_over()
        for rocket in self.overlapping_sprites:
            self.dx = -self.dx
            self.dy = -self.dy

    def game_over(self):
        game_over_message = games.Message(value = "Game over!",
                                          size = 90,
                                          color = color.blue,
                                          x = games.screen.width/2,
                                          y = games.screen.height/2,
                                          lifetime = 5*games.screen.fps,
                                          after_death = games.screen.quit)
        games.screen.add(game_over_message)

def main():
    wall_image = games.load_image("table2.jpg", transparent = False)
    games.screen.background = wall_image
    rocket = Rocket()
    games.screen.add(rocket)
    ball = Ball()
    games.screen.add(ball)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()
        

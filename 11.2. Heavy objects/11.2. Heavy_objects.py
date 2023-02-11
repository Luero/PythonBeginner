# Игра, где на персонаж, управляемый с помощью мыши, сверху падают тяжелые предметы, а он уворачивается
# Created by Luero, 24/07/2022

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Player(games.Sprite):
    image = games.load_image("builder1.png")
    collision = False
    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
        self.score = games.Text(value = 0,
                                size = 25,
                                color = color.black,
                                is_collideable = False,
                                top = 5,
                                right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.right > games.screen.width:
            self.right = games.screen.width
        if self.left < 0:
            self.left = 0
        self.check_collision()

    def check_collision(self):
        for object in self.overlapping_sprites:
            object.destroy()
            self.collision = True
            self.game_over()

    def score_count(self):
        self.score.value += 10
        self.score.right = games.screen.width - 10

    def game_over(self):
        game_over_message = games.Message(value = "Game over!",
                                          size = 90,
                                          color = color.blue,
                                          x = games.screen.width/2,
                                          y = games.screen.height/2,
                                          lifetime = 5*games.screen.fps,
                                          after_death = games.screen.quit)
        games.screen.add(game_over_message)

class Object(games.Sprite):
    image = games.load_image("box1.jpg")    
    def __init__(self, player):
        super(Object, self).__init__(image = Object.image,
                                     x = random.randrange(0, games.screen.width),
                                     dy = random.randrange(1, 3),
                                     bottom = 0)
        self.player = player
           
    def update(self):
        self.drop_box()
        if self.bottom == games.screen.height and self.player.collision == False:
            self.destroy()
            self.player.score_count()

    def drop_box(self):       
        if self.bottom == games.screen.height/2 and self.player.collision == False:
            new_object = Object(self.player)
            games.screen.add(new_object)

def main():
    wall_image = games.load_image("grass.png", transparent = False)
    games.screen.background = wall_image
    the_player = Player()
    games.screen.add(the_player)
    the_object = Object(the_player)
    games.screen.add(the_object)
    the_object2 = Object(the_player)
    games.screen.add(the_object2)
    the_object3 = Object(the_player)
    games.screen.add(the_object3)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()

    

    


                                    


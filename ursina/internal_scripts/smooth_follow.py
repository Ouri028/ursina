from ursina import *

class SmoothFollow(object):

    def __init__(self, target=None, offset=(0,0,0), speed=8, rotation_speed=0, rotation_offset=(0,0,0)):
        self.target = target
        self.offset = offset
        self.speed = speed

        self.rotation_speed = rotation_speed
        self.rotation_offset = rotation_offset


    def update(self):
        if not self.target:
            return

        self.entity.position = lerp(
            self.entity.world_position,
            self.target.world_position + self.offset,
            time.dt * self.speed)

        if self.rotation_speed > 0:
            self.entity.rotation = lerp(
            self.entity.world_rotation,
            self.target.world_rotation + self.rotation_offset,
            time.dt * self.rotation_speed)




if __name__ == '__main__':
    app = Ursina()

    class Player(Entity):
        def __init__(self):
            super().__init__(model='cube', color=color.orange)

        def update(self):
            self.x += held_keys['d'] * .1
            self.x -= held_keys['a'] * .1

    player = Player()
    Entity(model='cube').add_script(SmoothFollow(target=player, offset=(0,2,0)))
    app.run()
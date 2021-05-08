from pygame         import *
scr         = display.set_mode((400,600))
scrrect     = scr.get_rect()
font.init()
police = font.Font('Roboto.ttf',50)
from lib.enemi      import enemi
from lib.shotenemi  import shotenemi
from lib.shotami    import shotami
from lib.ship       import ship
from lib.particle   import explosion
from lib.layer      import bulletlayer, osdlayer
from lib.background import Background
from lib.levelmess  import Levelmess
from lib.bonus      import bonus

joystick.init()
if joystick.get_count(): joystick.Joystick(0).init()
    
class Game(object):
    
    levels     = ['Level1']
    levelcount = 1
    ck0        = time.Clock()
    
    
    def run(self):
        while self.levels:
            levelname = self.levels[0]
            level     = __import__('lib.levels',None,None,[levelname])
            level     = getattr(level,levelname)
            Game().clear(level)
            display.set_caption('Defender <Level {0}>'.format(self.levelcount))
            Levelmess.update(level.__doc__)
            endlevelflag = 0
            while True:
                ev = event.poll()
                if ev.type == QUIT: exit()
                statuslevel = level.update()
                if not statuslevel and not endlevelflag:
                    Levelmess.update('Level Done')
                    endlevelflag = 1
                Background.render()
                bulletlayer.render()
                osdlayer.render()
                explosion.render()
                statusship      = ship.update(ev)
                Background.update()
                statusmess = Levelmess.render()
                if not any((statuslevel,explosion.status,statusmess)):
                    self.levels.pop(0)
                    self.levelcount += 1
                    break
                shotami.update()
                enemi.update()
                bonus.update()
                shotenemi.update()
                display.flip()
                if not any((statusship,explosion.status)):
                    Levelmess.update('Level Reloaded')
                    self.clear(level)
                self.ck0.tick(50)
            scr.fill(0)
            Levelmess.update('Thanks for testing')
            Levelmess.render()
            display.update()
        time.wait(3000)
    
    def clear(self,level):
        enemi[:] = []
        shotami[:] = []
        shotenemi[:] = []
        ship.clear()
        level.clear()
    
        

        
        
if __name__ == "__main__":
    game = Game()
    game.run()
    
    

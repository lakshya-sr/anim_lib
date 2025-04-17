import pygame as pg
from animation import QUIT, KEY, MOUSE, Event


def update():
    events = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            events.append(Event(QUIT, None))
    pg.display.flip()
    screen.fill("black")
    return events
        
def init(screen_size):
    global screen
    pg.init()
    screen = pg.display.set_mode(screen_size)

def draw_circle(pos, radius, color, filled=True):
    pg.draw.circle(screen, color, pos, radius, 0 if filled else 1)

def draw_rect(pos, w, h, rot, color, filled=True):
    if rot == 0:
        pg.draw.rect(screen, color, (pos[0], pos[1], w, h), 0 if filled else 1)
    else:
        rectRotated(screen, color, (pos[0], pos[1], w, h), 0 if filled else 1, 1, rot)

def draw_image(pos, data, scale, rot):
    s = pg.transform.rotate(data, rot)
    s = pg.transform.scale_by(s, scale)
    screen.blit(s, pos)






def rectRotated( surface, color, pos, fill, border_radius, rotation_angle, rotation_offset_center = (0,0), nAntialiasingRatio = 1 ):
    """
    - rotation_angle: in degree
    - rotation_offset_center: moving the center of the rotation: (-100,0) will turn the rectangle around a point 100 above center of the rectangle,
                                         if (0,0) the rotation is at the center of the rectangle
    - nAntialiasingRatio: set 1 for no antialising, 2/4/8 for better aliasing
    """
    nRenderRatio = nAntialiasingRatio
    
    sw = pos[2]+abs(rotation_offset_center[0])*2
    sh = pos[3]+abs(rotation_offset_center[1])*2

    surfcenterx = sw//2
    surfcentery = sh//2
    s = pg.Surface( (sw*nRenderRatio,sh*nRenderRatio) )
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    
    rw2=pos[2]//2 # halfwidth of rectangle
    rh2=pos[3]//2

    pg.draw.rect( s, color, ((surfcenterx-rw2-rotation_offset_center[0])*nRenderRatio,(surfcentery-rh2-rotation_offset_center[1])*nRenderRatio,pos[2]*nRenderRatio,pos[3]*nRenderRatio), fill*nRenderRatio, border_radius=border_radius*nRenderRatio )
    s = pg.transform.rotate( s, rotation_angle )        
    if nRenderRatio != 1: s = pg.transform.smoothscale(s,(s.get_width()//nRenderRatio,s.get_height()//nRenderRatio))
    incfromrotw = (s.get_width()-sw)//2
    incfromroth = (s.get_height()-sh)//2
    surface.blit( s, (pos[0]-surfcenterx+rotation_offset_center[0]+rw2-incfromrotw,pos[1]-surfcentery+rotation_offset_center[1]+rh2-incfromroth) )
    

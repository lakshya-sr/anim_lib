import animation
from animation import Circle, Animation, Rect, Image
from functions import *
import easings
import time

animation.init((800, 600))

c1 = Circle((100,300), 0, 1, 20, "white", True)
r1 = Rect((100,300), 0, 1, 100, 100, "white", True)



anim = Animation()
anim.add(c1, goto_pos(c1, (400, 100), easings.inout_quad), duration=2)
anim.add(c1, goto_pos(c1, (700, 300), easings.inout_quad), duration=2)
anim.add(c1, goto_pos(c1, (400, 500), easings.inout_quad), duration=2)
anim.add(c1, goto_pos(c1, (100, 300), easings.inout_quad), duration=2)

animation.run(anim)

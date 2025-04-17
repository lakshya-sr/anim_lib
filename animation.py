import easings
import time

QUIT = 0
KEY = 1
MOUSE = 2

def init(screen_size, backend_name="pygame"):
    global backend
    if backend_name == "pygame":
        import backend_pygame
        backend = backend_pygame 
    
    backend.init(screen_size)

def run(anim):
    running = True 
    prev_frame_time = time.perf_counter()
    anim.play()
    while running:
        current_time = time.perf_counter()
        dt = current_time - prev_frame_time
        prev_frame_time = current_time
        
        for event in backend.update():
            if event.type == QUIT:
                running = False
            
        
        anim.update(dt)
        # print(c1.position, anim.time)


class Event:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        

class Animation:
    def __init__(self):
        self.anims = []
        self.time = 0
        self.playing = False
        self.total_time = 0

    def add(self, obj, func, start_time=None, end_time=None, duration=None, easing_func=easings.linear):
        if start_time == None:
            start_time = self.total_time
            end_time = start_time + duration
        elif end_time == None:
            end_time = start_time + duration
        else:
            print("Provide end_time or duration")
            return
        self.total_time += end_time-start_time
        self.anims.append(AnimationData(obj, func, start_time, end_time, easing_func))
        

    def update(self, dt):
        if self.playing: 
            for data in self.anims:
                if data.start_time <= self.time < data.end_time:
                    if not data.started:
                        data.start_val = data.obj.get_state()
                        data.started = True
                    data.func(data.obj, data.start_val, (self.time-data.start_time)/(data.end_time-data.start_time))
                data.obj.render()
            self.time += dt

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
                

class AnimationData:
    def __init__(self, obj, func, start_time, end_time, easing_func):
        self.obj = obj
        self.func = func
        self.start_time = start_time
        self.end_time = end_time
        self.easing_func = easing_func
        self.started = False
        self.start_val = 0



class Object:
    def __init__(self, position=(0,0), rotation=0, scale=0):
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.visible = True

    def render(self):
        pass

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def get_state(self):
        return self.position, self.rotation, self.scale

class Circle(Object):
    def __init__(self, position, rotation, scale, radius, color, filled):
        super().__init__(position, rotation, scale)
        self.radius = radius
        self.color = color
        self.filled = filled

    def render(self):
        if self.visible:
            backend.draw_circle(self.position, self.radius*self.scale, self.color, self.filled)

class Rect(Object):
    def __init__(self, position, rotation, scale, w, h, color, filled):
        super().__init__(position, rotation, scale)
        self.w = w
        self.h = h
        self.color = color
        self.filled = filled

    def render(self):
        if self.visible:
            backend.draw_rect(self.position, self.w*self.scale, self.h*self.scale, self.rotation, self.color, self.filled)

class Image(Object):
    def __init__(self, position, rotation, scale, data):
        super().__init__(position, rotation, scale)
        
        self.data = data

    def render(self):
        if self.visible:
            backend.draw_image(self.position, self.data, self.scale, self.rotation, pivot="center")

    

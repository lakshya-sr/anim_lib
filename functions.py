def goto_pos(obj, end, easing_func):
    start = obj.position
    def func(obj, start_state, t):
        start = start_state[0]
        obj.position = start[0] + (end[0]-start[0])*easing_func(t), start[1] + (end[1]-start[1])*easing_func(t)
    return func

def goto_x(obj, end, easing_func):
    def func(obj, start_state, t):
        start = start_state[0][0]
        obj.position = start + (end-start)*easing_func(t), obj.position[1]
    return func

def goto_y(obj, end, easing_func):
    start = obj.position[1]
    def func(obj, start_state, t):
        start = start_state[0][0]
        obj.position = start + (end-start)*easing_func(t), obj.position[1]
    return func

def rotate(obj, end, easing_func):
    start = obj.rotation
    def func(obj, start_state, t):
        start = start_state[1]
        obj.rotation = start + (end-start)*easing_func(t)
    return func

def scale(obj, end, easing_func):
    start = obj.scale
    def func(obj, start_state, t):
        start = start_state[2]
        obj.scale = start + (end-start)*easing_func(t)
    return func



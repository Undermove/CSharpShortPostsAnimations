from manim import *

class Decrement(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#BBFF33'
        sharp_color = '#00FF00'

        line1 = Line((-1,0,0),(1,0,0), stroke_width = 20, color = sharp_color)
        # line2 = Line((0,-1,0),(0,1,0), stroke_width = 20, color = sharp_color)
        self.play(Create(line1), run_time=speed)
        
        # line1.generate_target()
        # line1.target.move_to(LEFT)
        # self.play(MoveToTarget(line1), run_time=speed)
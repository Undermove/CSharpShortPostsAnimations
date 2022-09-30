from manim import *

class Fuck(Scene):
    def construct(self):
        speed = 0.2
        f_color = '#FF0000'
        sharp_color = '#00FF00'
        c_color = '#0000FF'
        k_color = '#F1F114'

        f = Line((-1.08,1,0),(0.75,1,0), stroke_width = 20, color = f_color)
        f_line2 = Line((-1,0.1,0),(0.5,0.1,0), stroke_width = 20, color = f_color)
        f_line3 = Line((-1,-1,0),(-1,1,0), stroke_width = 20, color = f_color)
        f.add(f_line2).add(f_line3)
        f.scale(2)
        self.play(Create(f), run_time=speed)

        sharp = Line((-2,1,0),(2,1,0), stroke_width = 20, color = sharp_color)
        sharp_line5 = Line((1,-2,0),(1,2,0), stroke_width = 20, color = sharp_color)
        sharp_line6 = Line((-2,-1,0),(2,-1,0), stroke_width = 20, color = sharp_color)
        sharp_line7 = Line((-1,-2,0),(-1,2,0), stroke_width = 20, color = sharp_color)
        sharp.add(sharp_line5).add(sharp_line6).add(sharp_line7)
        self.play(Create(sharp, run_time=speed))

        c = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Create(c), run_time=speed)

        k = Line((-1,0,0),(0.75,1,0), stroke_width = 20, color = k_color)
        k_line2 = Line((-0.75,0.18,0),(0.75,-1,0), stroke_width = 20, color = k_color)
        k_line3 = Line((-1,-1,0),(-1,1,0), stroke_width = 20, color = k_color)
        k.add(k_line2).add(k_line3)
        k.scale(2)

        self.play(f.animate.scale(0.5), sharp.animate.scale(0.5), c.animate.scale(0.5))
        self.play(f.animate.shift(3*LEFT), sharp.animate.shift(1.2*LEFT), c.animate.shift(1.2*RIGHT))

        self.wait(0.2)
        k.scale(0.5)
        k.shift(3*RIGHT)
        self.play(Create(k, run_time=speed))
        self.wait(1)
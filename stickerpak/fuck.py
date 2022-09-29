from manim import *

class Fuck(Scene):
    def construct(self):
        speed = 0.3
        f_color = '#FF0000'
        sharp_color = '#00FF00'
        c_color = '#0000FF'
        k_color = '#00FFFF'

        line1 = Line((-1,1,0),(0.75,1,0), stroke_width = 20, color = f_color)
        line2 = Line((-1,0.1,0),(0.5,0.1,0), stroke_width = 20, color = f_color)
        line3 = Line((-1,-1,0),(-1,1,0), stroke_width = 20, color = f_color)
        line1.add(line2).add(line3)
        self.play(Create(line1), run_time=speed)
        self.play(line1.animate.scale(2), run_time=speed)

        line4 = Line((-2,1,0),(2,1,0), stroke_width = 20, color = sharp_color)
        line5 = Line((1,-2,0),(1,2,0), stroke_width = 20, color = sharp_color)
        line6 = Line((-2,-1,0),(2,-1,0), stroke_width = 20, color = sharp_color)
        line7 = Line((-1,-2,0),(-1,2,0), stroke_width = 20, color = sharp_color)
        line4.add(line5).add(line6).add(line7)
        self.play(Create(line4, run_time=speed))
        # self.play(line1.animate.shift(1.5*LEFT), line4.animate.shift(1.5*RIGHT), run_time=speed)

        line4_copy = line4.copy()

        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Transform(line4_copy, s2), run_time=speed)
        self.wait(1)

        k_line1 = Line((-1,0,0),(0.75,1,0), stroke_width = 20, color = k_color)
        k_line2 = Line((-0.75,0.18,0),(0.75,-1,0), stroke_width = 20, color = k_color)
        k_line3 = Line((-1,-1,0),(-1,1,0), stroke_width = 20, color = k_color)
        k_line1.add(k_line2).add(k_line3)
        k_line1.scale(2)
        self.play(Create(k_line1, run_time=speed))
        self.wait(1)
from manim import *

class Plusuyu(Scene):
    def construct(self):
        speed = 0.3
        c_color = '#FF81FF'
        sharp_color = '#f000ff'

        line1 = Line((-1,0,0),(1,0,0), stroke_width = 20, color = sharp_color)
        line2 = Line((0,-1,0),(0,1,0), stroke_width = 20, color = sharp_color)
        line1.add(line2)
        line3 = line1.copy()
        self.play(Create(line1), run_time=speed)
        
        line1.generate_target()
        line1.target.move_to(LEFT)
        self.play(MoveToTarget(line1), run_time=speed)
        self.play(Create(line3.next_to(line1)), run_time=speed)
        self.wait(1)

        s = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        s.generate_target()
        self.play(Create(s), run_time=speed)
        s.target.move_to(1.5*LEFT)
        self.play(MoveToTarget(s), run_time=speed)
    
        text2 = MarkupText("<span style=\"italic\" size=\"x-large\">ПЛЮСУЮ!</span>")
        self.play(Create(text2.next_to(line3, direction=5*DOWN)), run_time=speed)
        self.wait(1)
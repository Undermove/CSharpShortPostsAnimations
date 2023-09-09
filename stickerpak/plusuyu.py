from manim import *

class Plusuyu(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#FF81FF'
        sharp_color = '#f000ff'

        line1 = Line((-2,0,0),(2,0,0), stroke_width = 40, color = sharp_color)
        line2 = Line((0,-2,0),(0,2,0), stroke_width = 40, color = sharp_color)
        line1.add(line2)
        line3 = line1.copy()
        self.play(Create(line1), run_time=speed)
        
        line1.generate_target()
        line1.target.move_to(LEFT)
        self.play(MoveToTarget(line1), run_time=speed)
        self.play(Create(line3.next_to(line1)), run_time=speed)
        self.wait(0.3)

        s = AnnularSector(inner_radius=3.5, outer_radius=4.5, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        s.generate_target()
        self.play(Create(s), run_time=speed)
        s.target.move_to(1.5*LEFT)
        self.play(MoveToTarget(s), run_time=speed)
    
        text2 = MarkupText(f'<span color=\"{sharp_color}\" style=\"italic\" size=\"25pt\">ПЛЮСУЮ!</span>')
        self.play(Create(text2.next_to(line3, direction=11*DOWN).shift(2.2*LEFT)), run_time=speed)
        self.wait(0.5)
from manim import *

class LyutoPlusuyu(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#BBFF33'
        sharp_color = '#00FF00'

        line1 = Line((-1,0,0),(1,0,0), stroke_width = 20, color = sharp_color)
        line2 = Line((0,-1,0),(0,1,0), stroke_width = 20, color = sharp_color)
        line1.add(line2)
        line3 = line1.copy()
        self.play(Create(line1), run_time=speed)
        
        line1.generate_target()
        line1.target.move_to(LEFT)
        self.play(MoveToTarget(line1), run_time=speed)
        self.play(Create(line3.next_to(line1)), run_time=speed)

        line4 = line1.add(line3).copy()
        self.play(Create(line4.next_to(line1, direction=DOWN)), run_time=speed)
        
        line4.add(line1)
        self.play(line4.animate.scale(0.5), run_time=speed)
        self.play(line4.animate.shift(UP*1.1), run_time=speed)

        s = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        s.generate_target()
        s.target.move_to(1.5*LEFT)
        # self.play(Create(s), run_time=speed)

        self.play(Create(s), MoveToTarget(s), run_time=speed)
    
        text2 = MarkupText(f'<span color=\"{sharp_color}\" style=\"italic\" size=\"large\">ЛЮТО ПЛЮСУЮ!</span>')
        self.play(Create(text2.next_to(line4, direction=5*DOWN)), run_time=speed)
        self.wait(1)
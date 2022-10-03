from manim import *

class CsharpSticker(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#F78D3F'
        sharp_color = '#500000'

        text = MarkupText(f'<span color=\"{c_color}\" size=\"xx-large\">Цэ</span>')
        self.play(Create(text), run_time=speed)
        self.wait(1)

        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Transform(text, s2), run_time=speed)

        text2 = MarkupText(f'<span color=\"{sharp_color}\" style=\"italic\" size=\"large\">РЕШЁТКА!</span>')
        self.play(Create(text2), run_time=speed)
        self.wait(1)

        line1 = Line((-2,1,0),(2,1,0), stroke_width = 20, color = sharp_color)
        line2 = Line((1,-2,0),(1,2,0), stroke_width = 20, color = sharp_color)
        line3 = Line((-2,-1,0),(2,-1,0), stroke_width = 20, color = sharp_color)
        line4 = Line((-1,-2,0),(-1,2,0), stroke_width = 20, color = sharp_color)
        line1.add(line2).add(line3).add(line4)
        self.play(Transform(text2,line1), run_time=speed)
        self.wait(1)

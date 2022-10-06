from manim import *

class Soryan(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#F78D3F'
        sharp_color = '#500000'

        point1 = Circle(radius=1, color=c_color, fill_opacity=1)
        point2 = Circle(radius=1, color=c_color, fill_opacity=1)
        point3 = Circle(radius=1, color=c_color, fill_opacity=1)
        
        self.play(Create(point1.shift(2.2*LEFT)), Create(point2.next_to(point1)), Create(point3.next_to(point2)), run_time=speed)
        self.wait(1)

        text_c = MarkupText(f'<span color=\"{c_color}\" size=\"xx-large\">.c</span>')
        text_p1 = MarkupText(f'<span color=\"{c_color}\" size=\"xx-large\">p</span>')
        text_p2 = MarkupText(f'<span color=\"{c_color}\" size=\"xx-large\">p</span>')
        self.play(Transform(point1, text_c), run_time=speed)
        self.play(Transform(point2, text_p1.next_to(text_c)), run_time=speed)
        self.play(Transform(point3, text_p2.next_to(text_p1)), run_time=speed)
        self.wait(1)


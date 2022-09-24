from manim import *

class TochkaNet(Scene):
    def construct(self):
        speed = 0.3
        c_color = '#FF813F'
        sharp_color = '#ffffff'

        text = MarkupText("<span size=\"x-large\">ТОЧКА!</span>")
        self.play(Create(text), run_time=speed)
        self.wait(1)

        circle = Circle(radius=1.0, color=c_color, fill_opacity=1)
        self.play(Transform(text, circle), run_time=speed)
        self.wait(1)
        
        circle2 = Circle(radius=1.3, color=c_color, fill_opacity=1)
        self.play(Transform(text, circle2), run_time=speed)
        self.play(Create(circle2.next_to(circle)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=LEFT)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=UP*1)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=DOWN*1)), run_time=speed)
        self.wait(1)

        text2 = MarkupText("<span style=\"italic\" size=\"x-large\">НЭТ!</span>")
        self.play(Transform(circle2, text2), run_time=speed)
        self.wait(1)
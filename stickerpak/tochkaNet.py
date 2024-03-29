from manim import *

class TochkaNet(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.17
        c_color = '#008500'
        text_color = '#FF7800'

        text = MarkupText(f'<span color=\"{text_color}\" size=\"75pt\">НЭТ!</span>')
        self.add(text)
        self.wait(speed)

        circle = Circle(radius=1.0, color=c_color, fill_opacity=1)
        self.play(Transform(text, circle), run_time=speed)
        self.wait(speed)
        
        circle2 = Circle(radius=3, color=c_color, fill_opacity=1)
        self.play(Transform(text, circle2), run_time=speed)
        self.play(Create(circle2.next_to(circle)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=LEFT)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=UP*1)), run_time=speed)
        self.play(Create(circle2.next_to(circle, direction=DOWN*1)), run_time=speed)
        self.wait(speed)

        text2 = MarkupText(f'<span color=\"{text_color}\" style=\"italic\" size=\"40pt\">И ТОЧКА!</span>')
        self.play(Transform(circle2, text2), run_time=speed)
        self.wait(speed)

        text3 = MarkupText(f'<span color=\"{text_color}\" style=\"italic\" size=\"75pt\">.NET</span>')
        self.play(Transform(circle2, text3), run_time=speed)
        self.wait(0.5)

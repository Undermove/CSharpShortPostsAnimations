from manim import *

class Spasibo(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        red_color = '#FF0000'
        orange_color = '#F78D3F'
        green_color = '#00FF3F'
        blue_color = '#0055FF'

        point1 = Circle(radius=1, color=red_color, fill_opacity=1)
        point2 = Circle(radius=1, color=green_color, fill_opacity=1)
        
        self.play(Create(point1.shift(2.2*LEFT)), Create(point2.next_to(point1)), run_time=speed)
        self.wait(1)

        text_c = MarkupText(f'<span color=\"{blue_color}\" size=\"x-large\">async</span>')
        text_p1 = MarkupText(f'<span color=\"{orange_color}\" size=\"x-large\">Спасибо()</span>')
        self.play(Transform(point1, text_c.shift(2.4*LEFT)), run_time=speed)
        self.play(Transform(point2, text_p1.next_to(text_c).shift(0.1*UP)), run_time=speed)
        self.wait(1)

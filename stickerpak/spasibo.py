from manim import *

class Spasibo(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        blue_color = '#0055FF'
        orange_color = '#F78D3F'
        orange2_color = '#F7AF3F'

        point1 = Circle(radius=1, color=blue_color, fill_opacity=1)
        point2 = Circle(radius=1, color=orange_color, fill_opacity=1)
        point3 = Circle(radius=1, color=orange2_color, fill_opacity=1)
        
        self.play(Create(point1.shift(2.2*LEFT)), Create(point2.next_to(point1)), Create(point3.next_to(point2)), run_time=speed)
        self.wait(0.5)

        text_async = MarkupText(f'<span color=\"{blue_color}\" size=\"x-large\">async</span>')
        text_spasibo = MarkupText(f'<span color=\"{orange_color}\" size=\"x-large\">Spasibo</span>')
        text_parentheses = MarkupText(f'<span color=\"{orange2_color}\" size=\"x-large\">()</span>')
        self.play(Transform(point1, text_async.shift(2.4*LEFT)),
        Transform(point2, text_spasibo.next_to(text_async).shift(0.1*UP)), 
        Transform(point3, text_parentheses.next_to(text_spasibo).shift(0.1*UP)),
        run_time=speed)
        self.wait(2)

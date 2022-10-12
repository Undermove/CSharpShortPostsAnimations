from manim import *

class Pozhaluista(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        blue_color = '#0055FF'
        orange_color = '#F78D3F'
        orange2_color = '#F7AF3F'

        point1 = Circle(radius=1, color=blue_color, fill_opacity=1)
        point2 = Circle(radius=1, color=orange_color, fill_opacity=1)
        point3 = Circle(radius=1, color=orange2_color, fill_opacity=1)
        
        self.play(
            Create(point1.shift(2.2*UP)), 
            Create(point2.next_to(point1, direction=DOWN)), 
            Create(point3.next_to(point2, direction=DOWN)), 
            run_time=speed)
        self.wait(0.5)

        text_async = MarkupText(f'<span color=\"{blue_color}\" size=\"large\">{{</span>')
        text_spasibo = MarkupText(f'<span color=\"{orange_color}\" size=\"large\">await Pozhaluista();</span>')
        text_parentheses = MarkupText(f'<span color=\"{blue_color}\" size=\"large\">}}</span>')
        self.play(
            Transform(point1, text_async.shift(1*UP).shift(3*LEFT)),
            Transform(point2, text_spasibo.next_to(text_async, direction=DOWN).shift(4*RIGHT)), 
            Transform(point3, text_parentheses.next_to(text_spasibo, direction=DOWN).shift(4*LEFT)),
            run_time=speed)
        self.wait(2)

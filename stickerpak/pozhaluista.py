from manim import *

class Pozhaluista(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        blue_color = '#0055FF'
        orange_color = '#F78D3F'

        point1 = Circle(radius=1, color=blue_color, fill_opacity=1)
        point2 = Circle(radius=1, color=orange_color, fill_opacity=1)
        point3 = Circle(radius=1, color=blue_color, fill_opacity=1)
        
        self.play(
            Create(point1.shift(2.2*UP)), 
            Create(point2.next_to(point1, direction=DOWN)), 
            Create(point3.next_to(point2, direction=DOWN)), 
            run_time=speed)
        self.wait(0.5)

        text_leftbrace = MarkupText(f'<span color=\"{blue_color}\" size=\"large\">{{</span>')
        text_await = MarkupText(f'<span color=\"{blue_color}\" size=\"large\">await</span>')
        text_pozhaluista = MarkupText(f'<span color=\"{orange_color}\" size=\"large\">Pozhaluista();</span>')
        text_parentheses = MarkupText(f'<span color=\"{blue_color}\" size=\"large\">}}</span>')
        self.play(
            Transform(point1, text_leftbrace.shift(1*UP).shift(3*LEFT)),
            Transform(point2, text_await.next_to(text_leftbrace, direction=DOWN).shift(2*RIGHT)), 
            Create(text_pozhaluista.next_to(text_await).shift(0.05*DOWN)), 
            Transform(point3, text_parentheses.next_to(text_await, direction=DOWN).shift(2*LEFT)),
            run_time=speed)
        self.wait(2)

from manim import *

class Soryan(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        red_color = '#FF0000'
        orange_color = '#F78D3F'
        yellow_color = '#F7FF3F'
        green_color = '#00FF3F'
        blue_color = '#0055FF'
        deepblue_color = '#0000FF'
        violet_color = '#FF00FF'

        point1 = Circle(radius=1, color=red_color, fill_opacity=1)
        point2 = Circle(radius=1, color=green_color, fill_opacity=1)
        point3 = Circle(radius=1, color=deepblue_color, fill_opacity=1)
        
        self.play(Create(point1.shift(2.2*LEFT)), Create(point2.next_to(point1)), Create(point3.next_to(point2)), run_time=speed)
        self.wait(1)

        text_c = MarkupText(f'<span color=\"{red_color}\" size=\"xx-large\">.c</span>')
        text_p1 = MarkupText(f'<span color=\"{green_color}\" size=\"xx-large\">p</span>')
        text_p2 = MarkupText(f'<span color=\"{deepblue_color}\" size=\"xx-large\">p</span>')
        text_p2.shift(0.1*DOWN)
        self.play(Transform(point1, text_c.shift(2.2*LEFT)), run_time=speed)
        self.play(Transform(point2, text_p1.shift(0.1*DOWN)), run_time=speed)
        self.play(Transform(point3, text_p2.shift(2.2*RIGHT)), run_time=speed)
        self.wait(1)

        text_o = MarkupText(f'<span color=\"{orange_color}\" size=\"xx-large\">o</span>')
        text_ya = MarkupText(f'<span color=\"{blue_color}\" size=\"xx-large\">я</span>')
        text_n = MarkupText(f'<span color=\"{violet_color}\" size=\"xx-large\">н</span>')
        self.play(text_o.animate.shift(1.0*LEFT), run_time=speed)
        
        point3.generate_target()
        point3.target.move_to(np.array((1, -0.1, 0.0)))
        self.play(MoveToTarget(point3), run_time=speed)
        self.play(text_ya.animate.shift(1.9*RIGHT), run_time=speed)
        self.play(text_n.animate.shift(2.8*RIGHT), run_time=speed)
        self.wait(1)

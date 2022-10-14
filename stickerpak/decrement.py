from manim import *

class Decrement(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#0044FF'
        sharp_color = '#000000'

        text = MarkupText(f'<span color=\"{c_color}\" size=\"xx-large\">ЦЕ</span>')
        self.play(Create(text.shift(LEFT)), run_time=speed)
        self.wait(0.5)

        mentText = MarkupText(f'<span color=\"{sharp_color}\">МЕНТ</span>')
        self.play(Create(mentText.shift(3.1*RIGHT).shift(0.06*UP)), run_time=speed)
        self.wait(0.5)

        decreText = MarkupText(f'<span color=\"{sharp_color}\">ДЕКРЕ</span>')
        self.play(Create(decreText.shift(1*RIGHT)), run_time=speed)
        self.wait(0.5)

        c = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Transform(text, c), run_time=speed)

        minus1 = Line((0,0,0),(2,0,0), stroke_width = 20, color = sharp_color)
        minus2 = Line((-1,0,0),(1,0,0), stroke_width = 20, color = sharp_color)
        self.play(Transform(decreText, minus1), run_time=speed)
        self.play(Transform(mentText, minus2.next_to(minus1)), run_time=speed)
        self.wait(1)
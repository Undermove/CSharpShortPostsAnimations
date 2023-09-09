from manim import *

class Decrement(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.1
        c_color = '#0044FF'
        sharp_color = '#000000'

        text = MarkupText(f'<span color=\"{c_color}\" size=\"30pt\">ЦЭ</span>')
        self.play(Create(text.shift(5*LEFT)), run_time=speed)

        mentText = MarkupText(f'<span color=\"{sharp_color}\" size=\"20pt\">МИНУС</span>')
        decreText = MarkupText(f'<span color=\"{sharp_color}\" size=\"20pt\">МИНУС</span>')
        
        self.play(Create(decreText.shift(LEFT)),
                  Create(mentText.shift(4.5*RIGHT),
                   run_time=speed))
        self.wait(0.2)

        c = AnnularSector(inner_radius=3.5, outer_radius=4, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Transform(text, c), run_time=speed)

        minus1 = Line((-2,0,0),(2,0,0), stroke_width = 30, color = sharp_color)
        minus2 = Line((-4,0,0),(0,0,0), stroke_width = 30, color = sharp_color)
        self.play(Transform(decreText, minus1), run_time=speed)
        self.play(Transform(mentText, minus2.next_to(minus1)), run_time=speed)
        self.wait(0.5)
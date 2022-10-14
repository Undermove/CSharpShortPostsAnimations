from manim import *

class Krut(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF00"
        speed = 0.3
        c_color = '#ff0000'
        sharp_color = '#ff5a00'

        text2 = MarkupText(f'<span color=\"{sharp_color}\" style=\"italic\" size=\"x-large\">КРУТЬ!</span>')
        self.play(Create(text2.shift(2*RIGHT)), run_time=speed)
        self.wait(1)

        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Create(s2), run_time=speed)

        s2.add(text2)

        self.play(Rotate(
                s2,
                angle=-0.5*PI,
                about_point=ORIGIN,
                rate_func=rate_functions.ease_in_out_sine,
            ), run_time=speed)
        self.play(Rotate(
                s2,
                angle=4.5*PI,
                about_point=ORIGIN,
                rate_func=rate_functions.ease_in_out_sine,
            ), run_time=speed)
        self.wait(1)

from manim import *

class Plusuyu(Scene):
    def construct(self):
        speed = 0.3
        c_color = '#FF813F'

        text = MarkupText("<span size=\"x-large\">НЭТ!</span>")
        self.play(Create(text), run_time=speed)
        self.wait(1)
from manim import *

class Testing(Scene):
    def construct(self):
        # square = Square()
        # square.width = 3

        START = (-2,0,0)
        END =   (2,0,0)
        # line1 = Line((-2,0,0),(2,0,0))
        line2 = Line((-2,1,0),(2,1,0), stroke_width = 20)
        # line3 = Line((0,2,0), (0,-2,0))
        line4 = Line((1,-2,0),(1,2,0), stroke_width = 20)
        # line2.next_to(line1, UP, buff=1)
        # line4.next_to(line3, LEFT, buff=1)

        self.play(Create(line2))
        self.play(Create(line4))
        line2.add(line4)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=RED).rotate(45 * DEGREES)

        # some animations display mobjects, ...
        self.play(FadeIn(s2))

        # some animations remove mobjects from the screen
        self.play(Transform(s2, line2))

        # ... some move or rotate mobjects around...
        self.play(Rotate(s2, PI))
        s3 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=RED).rotate(45 * DEGREES)
        self.play(FadeIn(s3))
        s2.add(line2)
        self.play(s2.animate.scale(0.5))
        self.play(s2.animate.shift(RIGHT)),
        self.wait(1)
from manim import *

class Testing(Scene):
    def construct(self):
        speed = 0.6
        c_color = '#F78D3F'
        sharp_color = '#ffffff'

        line1 = Line((-2,1,0),(2,1,0), stroke_width = 20, color = sharp_color)
        line2 = Line((1,-2,0),(1,2,0), stroke_width = 20, color = sharp_color)

        self.play(Create(line1),Create(line2), run_time=speed)
        line1.add(line2)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=sharp_color).rotate(45 * DEGREES)

        # some animations display mobjects, ...
        self.play(Create(s2), run_time=speed)

        # some animations remove mobjects from the screen
        line3 = Line((-2,1,0),(2,1,0), stroke_width = 20, color = sharp_color)
        line4 = Line((1,-2,0),(1,2,0), stroke_width = 20, color = sharp_color)
        line3.add(line4).rotate(PI)
        self.play(Transform(s2, line3), run_time=speed)
        
        s3 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=270 * DEGREES, color=c_color).rotate(45 * DEGREES)
        self.play(Create(s3), run_time=speed)
        
        s2.add(line1)
        
        self.play(s2.animate.scale(0.5), run_time=speed)
        self.play(s2.animate.shift(RIGHT), run_time=speed),
        
        s4 = s2.add(s3).copy()
    
        bool_ops_text = MarkupText("<span size=\"x-large\">Short Posts (18+)</span>").next_to(s2, DOWN * 3, aligned_edge=ORIGIN)
        self.play(Transform(s4, bool_ops_text), run_time=speed)
        self.wait(1)

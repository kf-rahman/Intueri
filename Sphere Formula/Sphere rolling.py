from manimlib.imports import *
import math
class ExampleThreeD(ThreeDScene):
    CONFIG = {
        "camera_class": ThreeDCamera,




        }

    def construct(self):
        sphere= Sphere()

        self.add(sphere)




        self.set_camera_orientation(phi=60*DEGREES,theta=-45*DEGREES)


        self.move_camera(gamma=0,run_time=1)  #currently broken in manim
        self.move_camera(phi=1/2*PI, theta=-PI/2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)


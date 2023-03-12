__all__ = ['circle_perimeter', 'circle_area']
from math import pi


def circle_perimeter():
    per = (2*pi*default_radius)
    return per


def circle_area():
    ar = (pi*default_radius**2)
    return ar


default_radius = 5

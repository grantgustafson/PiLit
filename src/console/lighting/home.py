from lighting.wave import Wave
from lighting.basic import SingleColor, SingleIntensity
from lighting.color_transition import ColorTransition
from lighting.intensity_wave import IntensityWave

start_color = .45
warm_color = .04

WARM_UP_COLOR = ColorTransition(start_color=start_color,
                                end_color = warm_color,
                                nextc=[SingleColor(hue=.04)])

WARM_UP_I = SingleIntensity()

OFF_I = SingleIntensity(i=0.0)

ON_COLOR = SingleColor(hue=start_color)
ON_I = SingleIntensity(i=1.0)

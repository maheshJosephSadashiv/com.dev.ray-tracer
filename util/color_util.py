def intensity_multiplier(color, I):
    red = round(color[0] * I)
    green = round(color[1] * I)
    blue = round(color[2] * I)
    if red > 255:
        red = 255
    if blue > 255:
        blue = 255
    if green > 255:
        green = 255
    return (red, green, blue)

def color_add(color1, color2):
    red = color1[0]+color2[0]
    green = color1[1]+color2[1]
    blue = color1[2]+color2[2]
    if red > 255:
        red = 255
    if blue > 255:
        blue = 255
    if green > 255:
        green = 255
    return (red, green, blue)
        
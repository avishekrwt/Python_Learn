band_color = {
    'black'    : 0, 
    'brown'    : 1,
    'red'      : 2,
    'orange'   : 3,
    'yellow'   : 4,
    'green'    : 5,
    'blue'     : 6,
    'violet'   : 7,
    'grey'     : 8,
    'white'    : 9
}
def label(colors):
    colors_value = int(f"{band_color[colors[0]]}{band_color[colors[1]]}")
    colors_value = colors_value * 10 ** band_color[colors[2]]
    if colors_value < 1000:
        return f"{colors_value} ohms"
    elif colors_value < 1000000:
        return f"{colors_value // 1000} kiloohms"
    elif colors_value < 1000000000 :
        return f"{colors_value // 1000000} megaohms"
    else :
        return f"{colors_value // 1000000000} gigaohms"
colors_band = {
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
tolerance_band = {
    'grey' :     0.05,
    'violet' :   0.1,   
    'blue' :     0.25,
    'green' :    0.5,
    'brown' :    1,
    'red' :      2,
    'gold' :     5,
    'silver' :   10
}
def resistor_label(colors):
    if len(colors)>1:
        value_multiplier = colors[-2::-1]
        value_multiplier.reverse()
        prevalue = get_resistor(value_multiplier)
        return f"{prevalue} ±{tolerance_band[colors[-1]]}%"
    else:
        return f"{colors_band[colors[0]]} ohms"

def get_resistor(colors): 
    multiplier = colors_band[colors[-1]]
    colors.pop()
    if len(colors)==3:
        value_str = f"{colors_band[colors[0]]}{colors_band[colors[1]]}{colors_band[colors[2]]}"
    elif len(colors)==2:
        value_str = f"{colors_band[colors[0]]}{colors_band[colors[1]]}"   
    resistence_value = int(value_str)*(10**multiplier) 
    if resistence_value < 1000:
        return f"{resistence_value} ohms"
    if resistence_value < 1000000:
        resistence_value = resistence_value/1000
        if resistence_value.is_integer():
            resistence_value = int(resistence_value)
        return f"{resistence_value} kiloohms"
    if resistence_value < 1000000000:
        resistence_value = resistence_value/1000000
        if resistence_value.is_integer():
            resistence_value = int(resistence_value)
        return f"{resistence_value} megaohms"
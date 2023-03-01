""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

AUTHOR : AJEET KUMAR
DATE   : 26 FEB 2023
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    
    roundValue = float(value)
    Value = str(roundValue)
    if Value.find('.')==-1:
        finalValue = '%0.3f'%float(Value)
        return finalValue
    if Value.find('.')>=0:
        roundstring = Value + '000'
 
        if roundstring.find('.')==1:
            finalValue = '%0.3f'%float(roundstring)
        elif roundstring.find('.')==2:
            finalValue = '%0.2f'%float(roundstring)
        elif roundstring.find('.')==3:
            finalValue = '%0.1f'%float(roundstring)
        modifystring = str(finalValue)
        originalstring = modifystring[:5]
    return originalstring  
    
    

def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    Cyan = str5(cmyk.cyan)
    Magneta = str5(cmyk.magenta)
    Yellow = str5(cmyk.yellow)
    key = str5(cmyk.black)
    String = ('('+ Cyan + ', ' + Magneta + ', '+ Yellow +', ' + key + ')')
    return String


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value

    return '(' + str5(h) + ', ' + str5(s) + ', ' + str5(v)+')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255

    k = 1 - max(r, g, b)
    if k == 1.0:
        c = 0.0
        m = 0.0
        y = 0.0
    else:    
        c = (1 - r - k)/(1-k)
        m = (1 - g - k)/(1-k)
        y = (1 - b - k)/(1-k)

    return introcs.CMYK(c*100.0, m*100.0, y*100.0, k*100.0)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan/100.0
    m = cmyk.magenta/100.0
    y = cmyk.yellow/100.0
    k = cmyk.black/100.0
    r = 255*(1 - c)*(1 - k)
    g = 255*(1 - m)*(1 - k)
    b = 255*(1 - y)*(1 - k)


    return introcs.RGB(int(round(r)), int(round(g)), int(round(b)))


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    M = max(r,g,b)
    m = min(r,g,b)
    
    if M == 0:
        S = 0.0
    if M != 0:
        S = (1 - m/M)
    if M == m:
        H = 0.0
    
    else:
        if M == r and g >= b:
            H = (60.0*(g - b)/(M - m)) 
        elif M == r and g < b:
            H = (60.0*(g - b)/(M - m)) + 360.0
        elif M == b :
            H = (60.0*(r - g)/(M - m)) + 240.0
        elif M == g :
            H = (60.0*(b - r)/(M - m)) + 120.0
        
    V = M

    return introcs.HSV(H, S, V)


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    Hi = math.floor(hsv.hue/60)
    f = hsv.hue/60-Hi
    p = hsv.value*(1-hsv.saturation)
    q = hsv.value*(1-f*hsv.saturation)
    t = hsv.value*(1-(1-f)*hsv.saturation)
   
    if Hi == 0:
        R = hsv.value
        G = t
        B = p
    elif Hi == 1:
        R = q
        G = hsv.value
        B = p
    elif Hi == 2:
        R = p
        G = hsv.value
        B = t
    elif Hi == 3:
        R = p
        G = q
        B = hsv.value
    elif Hi == 4:
        R = t
        G = p
        B = hsv.value
    elif Hi == 5:
        R = hsv.value
        G = p
        B = q
   
    return introcs.RGB(int(round(R*255)),int(round(G*255)),int(round(B*255)))


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    /
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    x = value
    c = contrast
    if c == 1:
        if x >= 0.5:
            y = 1
        else:
            y = 0
    else:
        if x < (0.25 + 0.25*c):
            y = (1 - c)*x/(1 + c)

        elif x > (0.75 - 0.25*c):
            y = (1 - c)*(x - (3 - c)/4)/(1 + c) + (3 + c)/4

        else:
            y = (1 + c)*(x - (1 + c)/4)/(1 - c) + (1 - c)/4

    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255

    rgb.red = int(contrast_value(r , contrast)*255)
    rgb.green = int(contrast_value(g, contrast)*255)
    rgb.blue = int(contrast_value(b, contrast)*255)
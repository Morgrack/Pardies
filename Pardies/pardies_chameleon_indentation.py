#Credit to Katie for helping with the equation

#KIVY LIBARY
from kivy.graphics import Color, Rectangle, Triangle
from kivy.graphics.instructions import VertexInstruction




#CHAMELEON INDENTATION EQUATION (WIP)
def chameleonIndentation(block, r, g, b, cf):
    #18
    if block.block_type == "EighteenthBlock":
        ro = r
        go = g
        bo = b
        #katiecolourswag
        r = r + cf*0.07
        g = g + cf*0.20
        b = b + cf*0.34
        if r >= 1:
            katievariableswag = r//1
            r = r - katievariableswag
        if g >= 1:
            katievariableswag = g//1
            g = g - katievariableswag
        if b >= 1:
            katievariableswag = b//1
            b = b - katievariableswag
        block.upper_block_colour.canvas.clear()
        with block.upper_block_colour.canvas:
            Color(r, g ,b)
            Triangle(points = (140,35, 140,0, 0,35))
        if cf > 0:
            cf = cf - 1
        #katiecolourswag
        ro = ro + cf*0.07
        go = go + cf*0.20
        bo = bo + cf*0.34
        if ro >= 1:
            katievariableswag = ro//1
            ro = ro - katievariableswag
        if go >= 1:
            katievariableswag = go//1
            go = go - katievariableswag
        if bo >= 1:
            katievariableswag = bo//1
            bo = bo - katievariableswag
        block.lower_block_colour.canvas.clear()
        with block.lower_block_colour.canvas:
            Color(ro, go ,bo)
            Triangle(points = (0,0, 0,35, 140,0))
    #11, 12, 14, 15
    elif (block.block_type == "EleventhBlock"
    or block.block_type == "TwelfthBlock"
    or block.block_type == "FourteenthBlock"
    or block.block_type == "FifteenthBlock"):
        if cf > 0:
            cf = cf - 1
        #katiecolourswag
        r = r + cf*0.07
        g = g + cf*0.20
        b = b + cf*0.34
        if r >= 1:
            katievariableswag = r//1
            r = r - katievariableswag
        if g >= 1:
            katievariableswag = g//1
            g = g - katievariableswag
        if b >= 1:
            katievariableswag = b//1
            b = b - katievariableswag
        block.block_colour.canvas.clear()
        with block.block_colour.canvas:
            Color(r, g ,b)
            Rectangle(pos = (0,0), size = block.size)
        cf = cf + 1
    #4, 7, 10, 13, 16, 17
    elif (block.block_type == "FourthBlock"
    or block.block_type == "SeventhBlock"
    or block.block_type == "TenthBlock"
    or block.block_type == "ThirteenthBlock"
    or block.block_type == "SixteenthBlock"
    or block.block_type == "SeventeenthBlock"):
        #katiecolourswag
        r = r + cf*0.07
        g = g + cf*0.20
        b = b + cf*0.34
        if r >= 1:
            katievariableswag = r//1
            r = r - katievariableswag
        if g >= 1:
            katievariableswag = g//1
            g = g - katievariableswag
        if b >= 1:
            katievariableswag = b//1
            b = b - katievariableswag
        block.block_colour.canvas.clear()
        with block.block_colour.canvas:
            Color(r, g ,b)
            Rectangle(pos = (0,0), size = block.size)
        cf = cf + 1
    #1, 2, 3, 5, 6, 8, 9
    else:
        #katiecolourswag
        r = r + cf*0.07
        g = g + cf*0.20
        b = b + cf*0.34
        if r >= 1:
            katievariableswag = r//1
            r = r - katievariableswag
        if g >= 1:
            katievariableswag = g//1
            g = g - katievariableswag
        if b >= 1:
            katievariableswag = b//1
            b = b - katievariableswag
        block.block_colour.canvas.clear()
        with block.block_colour.canvas:
            Color(r, g ,b)
            Rectangle(pos = (0,0), size = block.size)
    return (block, cf)

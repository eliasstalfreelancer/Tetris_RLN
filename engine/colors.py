class Colors:
    dark_grey = (26,31,40)
    green = (47,230,23) #L 
    red = (232,18,18)  #J
    orange = (226,116,17) #I
    yellow = (237,234,4) #O
    purple = (166,0,247) #S
    cyan = (21,204,209) #T
    blue = (13,64,216) #Z
    white = (255,255,255) #color for font 
    dark_blue = (44,44,127) #color for background
    light_blue = (59,85,162) #color for the information boxes

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey,cls.green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]
    
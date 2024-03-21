#Métodos para la ventana
class WindowApp:

    @classmethod
    def set_width(cls, screenWidth):
        #app_width = screenWidth // 2
        app_width = 960
        return app_width

    @classmethod
    def set_height(cls, screenHeight):
        #app_height = screenHeight // 2
        app_height = 540
        return app_height
    
    @classmethod
    def set_x_position(cls, screenWidth, appWidth):
        x = (screenWidth // 2) - (appWidth // 2)
        return x

    
    @classmethod
    def set_y_position(cls, screenHeight, appHeight):
        y = (screenHeight // 2) - (appHeight // 2)
        return y
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

# Box-shadow
class BoxShadow(QGraphicsDropShadowEffect):
    def __init__(self, color: QColor, offsetX: float, offsetY: float, blur: float = 0):
        """
        :param color: define as cores da sombra atráves de um objeto QtGui.QColor
        :param offsetX: define o deslocamento da sombra no eixo x
        :param offsetY: define o deslocamento da sombra no eixo y
        :param blur: define o blur da sombra
        """

        super().__init__()
        self.setColor(color)
        self.setOffset(offsetX, offsetY)
        self.setBlurRadius(blur)

from PyQt6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure


class Grafico(QWidget):
    """
    Cria um gráfico de donut que recebe um float da porcentagem \n
    lida e da porcentagem que falta ler
    """

    def __init__(self, lido: float, faltaLer: float, parent):
        super().__init__(parent)
        self.setFixedSize(200, 250)

        # cria o espaço em que o gráfico será plotado
        self.figure = Figure(figsize=(4, 4), dpi=100, facecolor="#F0F0F0")
        self.canvas = FigureCanvas(self.figure)

        # criar o layout do gráfico
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.canvas)

        # cria um subplot 1x1 e seleciona o 1 subplot(por isso 111)
        self.ax = self.figure.add_subplot(111)

        # proporção igual para evitar a distorção
        self.ax.axis("equal")

        # Dados do gráfico
        data = [lido, faltaLer]
        labels = ["Lido", "Falta ler"]
        colors = ["#FF5733", "#33FF57"]

        # Crie o gráfico de donut
        self.ax.pie(
            data,
            labels=None,
            startangle=90,
            colors=colors,
            # se width fosse 1 seria um gráfico de pizza padrão, a largura do espaço vazio é de 40%
            wedgeprops=dict(width=0.4, edgecolor="none"),
        )

        # Crie uma legenda com as porcentagens e cores
        labelsLegenda = self.criarLabelsLegenda(labels, colors, data)

        self.legend = QLabel("<br>".join(labelsLegenda), self)
        self.layout.addWidget(self.legend)
        self.legend.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.figure.tight_layout()

    def criarLabelsLegenda(self, labels, colors, data):
        """
        Retorna uma lista com elementos HTML que possuem: \n
        Label, Cor e Valor correspondente
        """
        labelsLegenda = []
        for i, label in enumerate(labels):
            color = colors[i]
            percentage = data[i]
            legend_label = (
                # &#9632 é o caractere que será preenchido pela cor selecionada
                f'<span style="color:{color}">&#9632;</span> {label}: {percentage:.1f}%'
            )
            labelsLegenda.append(legend_label)
        return labelsLegenda

    def atualizar(self, lido: float, faltaLer: float):
        """
        Atualiza os valores do gráfico com novos valores de 'lido' e 'faltaLer'
        """
        # Limpa o gráfico atual
        self.ax.clear()

        # Dados do gráfico atualizados
        data = [lido, faltaLer]
        labels = ["Lido", "Falta ler"]
        colors = ["#FF5733", "#33FF57"]

        # Cria o gráfico de donut atualizado
        self.ax.pie(
            data,
            labels=None,
            startangle=90,
            colors=colors,
            wedgeprops=dict(width=0.4, edgecolor="none"),
        )

        # Cria uma nova legenda com os novos valores
        labelsLegenda = self.criarLabelsLegenda(labels, colors, data)

        self.legend.setText("<br>".join(labelsLegenda))

        # Redesenha o gráfico
        self.canvas.draw()

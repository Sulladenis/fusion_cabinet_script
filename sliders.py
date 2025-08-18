from .fastener import Fastener
from .base import Base


class Slader(Base):
            
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self.fasten = Fastener()
      

        panel = self.cabinet.left_panel

        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12 мм
        self.fasten.add_hole_parameters(0.5, 1.2)
        
        s1x = panel.width / 2 - 3.8
        s1y = -(panel.depth / 2 - 3.7)
        s2x = -(panel.side_thickness/2 + 3.8)

        for x in (s1x, s2x):

            self.fasten.add_hole_position(x, s1y)
            self.fasten.add_hole_position(x, s1y+3.2)
            self.fasten.add_hole_position(x, s1y+3.2+25.6)
            self.fasten.add_hole_position(x, s1y+3.2+25.6-3.2)

            self.fasten.create_hole()

        panel = self.cabinet.right_panel

        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12 мм
        self.fasten.add_hole_parameters(0.5, 1.2)
        
        s1x = -(panel.width / 2 - 3.8)
        s1y = -(panel.depth / 2 - 3.7)
        s2x = panel.side_thickness/2 + 3.8

        for x in (s1x, s2x):

            self.fasten.add_hole_position(x, s1y)
            self.fasten.add_hole_position(x, s1y+3.2)
            self.fasten.add_hole_position(x, s1y+3.2+25.6)
            self.fasten.add_hole_position(x, s1y+3.2+25.6-3.2)

            self.fasten.create_hole()




from .fastener import Fastener
from .base import Base


class Confirmats(Base):
            
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self.fasten = Fastener()
      

        panels =  self.cabinet.top_panel, self.cabinet.bottom_panel, cabinet.left_panel, self.cabinet.right_panel
        for panel in panels:

            self.fasten.add_panel(panel) # добавили панель для отверстий
            self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз

            # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина all
            self.fasten.add_hole_parameters(0.5, panel.side_thickness)

            x = panel.width / 2 / 3
            y = panel.depth / 2 - (panel.side_thickness/2)


            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x*2, y)
            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x*2, y)

            self.fasten.create_hole()

        # Выбераем панель: если joint_type = Side-on-bottom 
        if self.cabinet.joint_type == 'Side-on-bottom':
            panels =  self.cabinet.top_panel, self.cabinet.bottom_panel
        else:
        # Иначе берем сначала верхнюю панель
            panels = self.cabinet.left_panel, self.cabinet.right_panel

        for panel in panels:
            self.fasten.add_panel(panel) # добавили панель для отверстий
            self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
            # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина all
            self.fasten.add_hole_parameters(0.5, panel.side_thickness)
            
            # Рассчет отверстий от середины 0.0 
            x = panel.width / 2 - (panel.side_thickness/2)
            y = panel.depth / 2 - 15

            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x, -y)
            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x, -y)

            self.fasten.create_hole()

        
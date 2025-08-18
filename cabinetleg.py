from .fastener import Fastener
from .base import Base


class CabinetLeg(Base):
            
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self.fasten = Fastener()
      

        panel = self.cabinet.bottom_panel

        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 10 мм (1) глубина all
        self.fasten.add_hole_parameters(1, panel.side_thickness)
        
        sx = panel.width / 2 - 5
        sy = panel.depth / 2 - 6

        self.fasten.add_hole_position(sx, sy)
        self.fasten.add_hole_position(sx, -sy)
        self.fasten.add_hole_position(-sx, sy)
        self.fasten.add_hole_position(-sx, -sy)
        
        self.fasten.create_hole()
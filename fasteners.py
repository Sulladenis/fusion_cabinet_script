from .base import Base
from .fastener import Fastener


class FasZip17_Zip15(Base):
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self._palettes.writeText(f'Создан Zip152_Zip151 для {cabinet.name}')
        self.fas152 = Fastener()

        # Выбераем панель: если joint_type = Side-on-bottom то правую панель
        if self.cabinet.joint_type == 'Side-on-bottom':
            self.panel_for_152 = self.cabinet.left_panel
        else:
        # Иначе берем сначала верхнюю панель
            self.panel_for_152 =  self.cabinet.top_panel
        
        self.fas152.add_panel(self.panel_for_152)
        self.fas152.add_sketch(f'fas_{self.panel_for_152.name}')
        # Устанавливаем параметры отверстия диаметр 15 мм (1.5) глубина 13 мм (1.3)
        self.fas152.add_hole_parameters(1.5, 1.3)
        
        # Расчет координат отверстий для Zip152 и Zip151
        # Zip152 - 20,5 мм (2.05) от края по width и 70 мм (7) от краёв по depth 
        # Рассчет отверстий от середины 0.0 

        x = self.panel_for_152.width / 2 - 2.05
        y = self.panel_for_152.depth / 2 - 7

        # Если боковая панель на нижней то на ней 4 отверстия
        if self.cabinet.joint_type == 'Side-on-bottom':
            self.fas152.add_hole_position(x, y)
            self.fas152.add_hole_position(x, -y)
            self.fas152.add_hole_position(-x, y)
            self.fas152.add_hole_position(-x, -y)
            
            self.fas152.create_hole()
        else:
            # Иначе 2 отверстия в верхней панели
            self.fas152.add_hole_position(x, y)
            self.fas152.add_hole_position(x, -y)
            self.fas152.create_hole()

            # Берём еще и нижню панель
            self.panel_for_152 = self.cabinet.bottom_panel
            self.fas152.add_panel(self.panel_for_152)

            self.fas152.add_sketch(f'fas_{self.panel_for_152.name}')

            # Добавляем в нее ещё 2 отверстия Zip152 с правой стороны
            self.fas152.add_hole_position(-x, y)
            self.fas152.add_hole_position(-x, -y)
            self.fas152.create_hole()

        
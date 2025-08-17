from .fastener import Fastener
from .base import Base


class Zip151TwoSides(Base):
            
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self.fasten = Fastener()
      
        # Выбераем панель: если joint_type = Side-on-bottom то правую панель
        if self.cabinet.joint_type == 'Side-on-bottom':
            panels = self.cabinet.left_panel, self.cabinet.right_panel
        else:
        # Иначе берем сначала верхнюю панель
            panels =  self.cabinet.top_panel, self.cabinet.bottom_panel


        for panel in panels:

            self.fasten.add_panel(panel) # добавили панель для отверстий
            self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз

            # Устанавливаем параметры отверстия диаметр 20 мм (2) глубина 12.5 мм (1.25)
            self.fasten.add_hole_parameters(2, 1.25)
            # Расчет координат отверстий для Zip151
            # Zip151 - 9.5 мм (0.95) от края по width и 60 мм (6) от краёв по depth 
            # Рассчет отверстий от середины 0.0 
            x = panel.width / 2 - 0.95
            y = panel.depth / 2 - 7

            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x, -y)
            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x, -y)
            self.fasten.create_hole()

        panel = self.cabinet.back_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 20 мм (2) глубина 12.5 мм (1.25)
        self.fasten.add_hole_parameters(2, 1.25)
 
        self.fasten.add_hole_position(0, panel.width/2 - 0.95)
        self.fasten.add_hole_position(panel.depth/2 - 0.95, 0)
        self.fasten.add_hole_position(0, -panel.width/2 + 0.95)
        self.fasten.add_hole_position(-panel.depth/2 + 0.95, 0)

        self.fasten.create_hole()



        if self.cabinet.joint_type == "Bottom-between-sides":
            panels = self.cabinet.left_panel, self.cabinet.right_panel
        else:
            panels =  self.cabinet.top_panel, self.cabinet.bottom_panel


        for panel in panels:

            self.fasten.add_panel(panel) # добавили панель для отверстий
            self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз

            # Устанавливаем параметры отверстия диаметр 8 мм (0.8) глубина 13 мм (1.3)
            self.fasten.add_hole_parameters(0.8, 1.3)
            # Расчет координат отверстий для Zip151
            # Zip151 - 9.5 мм (0.95) от края по width и 60 мм (6) от краёв по depth 
            # Рассчет отверстий от середины 0.0 
            x = panel.width / 2 - panel.side_thickness + 0.75
            y = panel.depth / 2 - 7

            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x, -y)
            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x, -y)
            self.fasten.create_hole()

        panel = self.cabinet.right_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 8 мм (0.8) глубина 13 мм (1.3)
        self.fasten.add_hole_parameters(0.8, 1.3)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.75)
        self.fasten.create_hole()

        panel = self.cabinet.left_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 8 мм (0.8) глубина 13 мм (1.3)
        self.fasten.add_hole_parameters(0.8, 1.3)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.75)
        self.fasten.create_hole()

        panel = self.cabinet.top_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 8 мм (0.8) глубина 13 мм (1.3)
        self.fasten.add_hole_parameters(0.8, 1.3)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.75)
        self.fasten.create_hole()

        panel = self.cabinet.bottom_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 8 мм (0.8) глубина 13 мм (1.3)
        self.fasten.add_hole_parameters(0.8, 1.3)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.75)
        self.fasten.create_hole()





        


    



    


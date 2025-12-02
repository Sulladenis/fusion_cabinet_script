from .fastener import Fastener
from .base import Base


class Genifix(Base):
            
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

            # Устанавливаем параметры отверстия диаметр 15 мм (1.5) глубина 11.5 мм (1.15)
            self.fasten.add_hole_parameters(1.5, 1.15)
            # Расчет координат отверстий для Zip151
            # Zip151 - 3.6 мм (0.36) от края по width и 70 мм (7) от краёв по depth 
            # Рассчет отверстий от середины 0.0 
            x = panel.width / 2 - 0.36
            y = panel.depth / 2 - 7

            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x-1.12, y)
            self.fasten.add_hole_position(x-(1.12*2), y)

            self.fasten.add_hole_position(x, -y)
            self.fasten.add_hole_position(x-1.12, -y)
            self.fasten.add_hole_position(x-(1.12*2), -y)


            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x+1.12, y)
            self.fasten.add_hole_position(-x+(1.12*2), y)

            self.fasten.add_hole_position(-x, -y)
            self.fasten.add_hole_position(-x+1.12, -y)
            self.fasten.add_hole_position(-x+(1.12*2), -y)
            self.fasten.create_hole()

        panel = self.cabinet.back_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 15 мм (1.5) глубина 11.5 мм (1.15)
        self.fasten.add_hole_parameters(1.5, 1.15)
 
        self.fasten.add_hole_position(panel.depth/2 - 10, panel.width/2 - 0.36)
        self.fasten.add_hole_position(panel.depth/2 - 10, panel.width/2 - 0.36-1.12)
        self.fasten.add_hole_position(panel.depth/2 - 10, panel.width/2 - 0.36-1.12-1.12)

        self.fasten.add_hole_position(-(panel.depth/2 - 10), panel.width/2 - 0.36)
        self.fasten.add_hole_position(-(panel.depth/2 - 10), panel.width/2 - 0.36-1.12)
        self.fasten.add_hole_position(-(panel.depth/2 - 10), panel.width/2 - 0.36-1.12-1.12)

        self.fasten.add_hole_position(-2, panel.width/2 - 0.36)
        self.fasten.add_hole_position(-2, panel.width/2 - 0.36-1.12)
        self.fasten.add_hole_position(-2, panel.width/2 - 0.36-1.12-1.12)

        self.fasten.add_hole_position(panel.depth/2 - 0.36, 0)
        self.fasten.add_hole_position(panel.depth/2 - 0.36-1.12, 0)
        self.fasten.add_hole_position(panel.depth/2 - 0.36-1.12-1.12, 0)

        self.fasten.add_hole_position(panel.depth/2 - 10, -panel.width/2 + 0.36)
        self.fasten.add_hole_position(panel.depth/2 - 10, -panel.width/2 + 0.36+1.12)
        self.fasten.add_hole_position(panel.depth/2 - 10, -panel.width/2 + 0.36+1.12+1.125)

        self.fasten.add_hole_position(-(panel.depth/2 - 10), -panel.width/2 + 0.36)
        self.fasten.add_hole_position(-(panel.depth/2 - 10), -panel.width/2 + 0.36+1.12)
        self.fasten.add_hole_position(-(panel.depth/2 - 10), -panel.width/2 + 0.36+1.12+1.125)

        self.fasten.add_hole_position(-2, -panel.width/2 + 0.36)
        self.fasten.add_hole_position(-2, -panel.width/2 + 0.36+1.12)
        self.fasten.add_hole_position(-2, -panel.width/2 + 0.36+1.12+1.125)

        self.fasten.add_hole_position(-panel.depth/2 + 0.36, 0)
        self.fasten.add_hole_position(-panel.depth/2 + 0.36+1.12, 0)
        self.fasten.add_hole_position(-panel.depth/2 + 0.36+1.12+1.125, 0)

        self.fasten.create_hole()


        if self.cabinet.joint_type == "Bottom-between-sides":
            panels = self.cabinet.left_panel, self.cabinet.right_panel            
            ot = 10 + panels[0].side_thickness
        else:
            panels =  self.cabinet.top_panel, self.cabinet.bottom_panel
            ot = 10


        for panel in panels:

            self.fasten.add_panel(panel) # добавили панель для отверстий
            self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз

            # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12.5 мм (1.25)
            self.fasten.add_hole_parameters(0.5, 1.25)
            # Расчет координат отверстий для Zip151
            # Zip151 - 5 мм (0.5) от края по width и 70 мм (7) от краёв по depth 
            # Рассчет отверстий от середины 0.0 
            x = panel.width / 2 - panel.side_thickness + 0.5
            y = panel.depth / 2 - 7

            self.fasten.add_hole_position(x, y)
            self.fasten.add_hole_position(x, -y)
            self.fasten.add_hole_position(-x, y)
            self.fasten.add_hole_position(-x, -y)
            self.fasten.create_hole()

        panel = self.cabinet.right_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12.5 мм (1.25)
        self.fasten.add_hole_parameters(0.5, 1.25)
        self.fasten.add_hole_position(-(panel.width/2 - ot), panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.add_hole_position(2, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.add_hole_position(panel.width/2  - ot, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.create_hole()

        panel = self.cabinet.left_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12.5 мм (1.25)
        self.fasten.add_hole_parameters(0.5, 1.25)
        self.fasten.add_hole_position(-(panel.width/2 - ot), panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.add_hole_position(-2, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.add_hole_position(panel.width/2 - ot, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.create_hole()


        panel = self.cabinet.top_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12.5 мм (1.25)
        self.fasten.add_hole_parameters(0.5, 1.25)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.create_hole()

        panel = self.cabinet.bottom_panel
        self.fasten.add_panel(panel) # добавили панель для отверстий
        self.fasten.add_sketch(f'fas_{panel.name}') # Выбрали эскиз
        # Устанавливаем параметры отверстия диаметр 5 мм (0.5) глубина 12.5 мм (1.25)
        self.fasten.add_hole_parameters(0.5, 1.25)
        self.fasten.add_hole_position(0, panel.depth/2 - panel.side_thickness + 0.5)
        self.fasten.create_hole()





        


    

import adsk.core, adsk.fusion, adsk.cam, traceback
from .confirmats import Confirmats
from .zip151twosides import Zip151TwoSides
from .kitchen_cabinet import KitchenCabinet
from .sliders import Slader
from .cabinetleg import CabinetLeg
from .shelfs import SimpleShelf
from .genifix import Genifix

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface


        cabinet = KitchenCabinet()
        cabinet.add(45, # Ширина
                    80.2, # Высота
                    60, # Глубина
                    1.63, # Толщина дсп
                    1.8, # Толщина фасада
                    'К5', # Название
                    #joint_type="Bottom-between-sides"
                    )
        cabinet.create_panels()
        
        # Делаем отверстие
        # Zip151TwoSides(cabinet)
        Genifix(cabinet)
        # Confirmats(cabinet)
        # Slader(cabinet)
        CabinetLeg(cabinet)
        SimpleShelf(cabinet)



    except:
        if ui:
            ui.messageBox('Ошибка:\n{}'.format(traceback.format_exc()))

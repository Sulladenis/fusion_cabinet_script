import adsk.core, adsk.fusion, adsk.cam, traceback

from .fasteners import FasZip17zip15
from .kitchen_cabinet import KitchenCabinet
from .fastener import Fastener

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface


        cabinet = KitchenCabinet()
        cabinet.add(60, 90, 60, 1.63, 1.8, 'Корпус')
        cabinet.create_panels()
        
        # Делаем отверстие
        faszip152zip151 = FasZip17zip15(cabinet)


        cabinet._palettes.writeText(f'{dir(cabinet)}')


    except:
        if ui:
            ui.messageBox('Ошибка:\n{}'.format(traceback.format_exc()))

import adsk.core, adsk.fusion, adsk.cam, traceback
from .confirmats import Confirmats
from .zip151twosides import Zip151TwoSides
from .kitchen_cabinet import KitchenCabinet
from .fastener import Fastener

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface


        cabinet = KitchenCabinet()
        cabinet.add(90, 80, 60, 1.63, 1.8, 'Корпус', 
                    joint_type="Bottom-between-sides"
                    )
        cabinet.create_panels()
        
        # Делаем отверстие
        Zip151TwoSides(cabinet)
        Confirmats(cabinet)
        



        cabinet._palettes.writeText(f'{dir(cabinet)}')


    except:
        if ui:
            ui.messageBox('Ошибка:\n{}'.format(traceback.format_exc()))

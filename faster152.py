import adsk.core, adsk.fusion
from .base import Base
from .fastener import Fastener

class Faster152(Fastener):
    
    def add_recess_parameters(self, width=1, depth=-1.3):
        self.recess = FastenerRecess()
        self.recess.add(width, depth)
        

    def add_recess_position(self, x, y):
        self.add_recess_parameters()
        self.recess_extrudes = self._component.features.extrudeFeatures
        self.centr_point = self.sketch.sketchPoints.add(
            adsk.core.Point3D.create(x, y, 0)
        )
        center_point = adsk.core.Point3D.create(x, y, 0)
        corner_point = adsk.core.Point3D.create(x + 0.75, y + self.recess.width/2, 0) 
        
        sketchLines = self.sketch.sketchCurves.sketchLines
        self.rectangleLines = sketchLines.addCenterPointRectangle(center_point, corner_point)


    def create_recess(self):
        pass

class FastenerRecess(Base):
    
    def add(self, width, depth):
        self.width = width
        self.depth = depth

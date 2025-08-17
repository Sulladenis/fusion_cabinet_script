import adsk.core, adsk.fusion
from .base import Base

class Fastener(Base):
    def __init__(self):
        super().__init__()
        self.hole_points = adsk.core.ObjectCollection.create()

    def add_panel(self, panel):
        self.panel = panel
        self.face = panel.inner_face
        self._component = self.face.body.parentComponent
    
    def add_hole_parameters(self, diameter, depth):
        self.hole = FastenerHole()
        self.hole.add(diameter, depth)
        self.hole_features = self._component.features.holeFeatures
    
    def add_hole_position(self, x, y):
        self.end_point = self.sketch.sketchPoints.add(
            adsk.core.Point3D.create(x, y, 0)
        )
        self.hole_points.add(self.end_point)
        

 
    def add_sketch(self, name):
        self.sketch = self._component.sketches.itemByName(name)
        if self.sketch is None:
            self.sketch = self._component.sketches.add(self.face)
            self.sketch.name = name
        self._palettes.writeText(f'Создан эскиз для крепежа: {name}')


    def create_hole(self):
        hole_input = self.hole_features.createSimpleInput(
            adsk.core.ValueInput.createByReal(self.hole.diameter)
            )
        hole_input.setPositionBySketchPoints(self.hole_points)
        hole_input.setDistanceExtent(
            adsk.core.ValueInput.createByReal(self.hole.depth)
            )
        hole_input.tipAngle = adsk.core.ValueInput.createByString('180 deg')
        hole_input.participantBodies = [self.face.body]
        
        self.hole_features.add(hole_input)
        # Сбрасываем точки для отверстий
        self.hole_points = adsk.core.ObjectCollection.create()

class FastenerHole(Base):
    
    def add(self, diameter, depth):
        self.diameter = diameter
        self.depth = depth




# class FasterFace(Base):
#     def add(self, face):
#         self.face = face
#         self._component = face.component


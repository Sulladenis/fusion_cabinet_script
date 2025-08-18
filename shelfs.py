import adsk.core, adsk.fusion
from .base import Base
from .fastener import Fastener


class SimpleShelf(Base):
    def __init__(self, cabinet):
        super().__init__()
        self.cabinet = cabinet
        self._component = cabinet._component
        self.width = cabinet.width-cabinet.side_thickness*2
        self.depth = cabinet.depth-cabinet.side_thickness
        self.name = 'shelf'
        self.side_thickness = cabinet.side_thickness
        self.plane_xy = self._root_comp.xYConstructionPlane

        self.create_shelf_plane()
        self.create_sketch()
        self.create_body()

    def create_shelf_plane(self):
        #self.zposition = -(60-self.cabinet.height/2+self.side_thickness*1.5)
        self.zposition = 0
        offset_value = adsk.core.ValueInput.createByReal(self.zposition)
        planes  = self._component.constructionPlanes
        plane_input = planes.createInput()
        plane_input.setByOffset(self.plane_xy, offset_value)
        self.shelf_plane = planes.add(plane_input)
        self.shelf_plane.name = self.name


    def create_sketch(self):

        self.sketch = self._component.sketches.add(self.shelf_plane)
        self.sketch.name = self.name 
        lines = self.sketch.sketchCurves.sketchLines
        lines.addTwoPointRectangle(
            adsk.core.Point3D.create(-self.width/2, -self.depth/2 - self.side_thickness/2, 0),
            adsk.core.Point3D.create(self.width/2, self.depth/2- self.side_thickness/2, 0)
            )
        self.profile = self.sketch.profiles.item(0)

    def create_body(self):

        extrudes = self._component.features.extrudeFeatures
        extrude_input = extrudes.createInput(
            self.profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        # Симметричное выдавливание
        distance_input = adsk.core.ValueInput.createByReal(self.side_thickness/2)
        extrude_input.setSymmetricExtent(distance_input, False)

        self.extrude = extrudes.add(extrude_input)
        self.body = self.extrude.bodies.item(0)
        self.body.name = f'{self._component.name}_{self.name }'
        self._palettes.writeText(f'Создана панель: {self.name}')



 
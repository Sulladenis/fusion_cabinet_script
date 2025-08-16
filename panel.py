import adsk.core, adsk.fusion
from .base import Base

class Panel(Base):

    def add(self, base_plane, width, depth, side_thickness, face_thickness, name):
        self.base_plane = base_plane
        self._component = base_plane.component
        self.width = width
        self.depth = depth
        self.side_thickness = side_thickness
        self.face_thickness = face_thickness
        self.name = name

        self.crate_sketch()
        self.create_bady()


    def crate_sketch(self):

        self.sketch = self._component.sketches.add(self.base_plane)
        self.sketch.name = self.name
        self._palettes.writeText(f'Создан эскиз для панели: {self.name}')
        lines = self.sketch.sketchCurves.sketchLines
        lines.addTwoPointRectangle(
            adsk.core.Point3D.create(-self.width/2, -self.depth/2, 0),
            adsk.core.Point3D.create(self.width/2, self.depth/2, 0)
            )
        self.profile = self.sketch.profiles.item(0)


    def create_bady(self):
        if self.base_plane.name == 'Bottom Plane' or self.base_plane.name == 'Left Plane':
            # Выбор направлений реализвать через словарь имен {'Top Plane': True}
            self.ext_thickness = self.side_thickness
        elif self.base_plane.name == 'Fase Plane':
            self.ext_thickness = -self.face_thickness
        else:
            self.ext_thickness = -self.side_thickness
        
            
        extrudes = self._component.features.extrudeFeatures
        extrude_input = extrudes.createInput(
            self.profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrude_input.setDistanceExtent(
            False, adsk.core.ValueInput.createByReal(self.ext_thickness))
        self.extrude = extrudes.add(extrude_input)
        self.inner_face = self.extrude.endFaces.item(0)
        self.body = self.extrude.bodies.item(0)
        self.body.name = self.name
        self._palettes.writeText(f'Создана панель: {self.name}')




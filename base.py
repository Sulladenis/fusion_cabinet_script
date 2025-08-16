import adsk.core

class Base:

    def __init__(self):
        self._app = adsk.core.Application.get()
        self._ui = self._app.userInterface
        self._palettes = self._ui.palettes.itemById('TextCommands')
        self._design = self._app.activeProduct
        self._root_comp = self._design.rootComponent
        self._occurrences = self._root_comp.occurrences

class Cabinet(Base):

    def create_component(self, name):
        self._occurrence = self._occurrences.addNewComponent(adsk.core.Matrix3D.create())
        self._component = self._occurrence.component
        self._component.name = name
        self._planes = self._component.constructionPlanes
        self._palettes.writeText(f'Создан новый компонент: {self._component.name}')


    def add(self, width, height, depth, side_thickness, face_thickness, name, joint_type="Side-on-bottom" ):
        self.width = width 
        self.height = height
        self.depth = depth - face_thickness
        self.side_thickness = side_thickness
        self.face_thickness = face_thickness
        self.name = name
        self.joint_type = joint_type
        self.create_component(self.name)
        self.createBasePlanes()
    
    def createBasePlanes(self):
        data_planes = [
            (self._component.xYConstructionPlane, -self.height/2, 'Bottom Plane'),
            (self._component.xYConstructionPlane, self.height/2, 'Top Plane'),
            (self._component.yZConstructionPlane, -self.width/2, 'Left Plane'),
            (self._component.yZConstructionPlane, self.width/2, 'Right Plane'),
            (self._component.xZConstructionPlane, -self.depth/2, 'Fase Plane'),
            (self._component.xZConstructionPlane, self.depth/2, 'Back Plane'),
        ]
        self.base_planes = []

        for plane, offset_value, name in data_planes:
            offset = adsk.core.ValueInput.createByReal(offset_value)
            plane_input = self._planes.createInput()
            plane_input.setByOffset(plane, offset)
            new_plane = self._planes.add(plane_input)
            new_plane.name = name
            self.base_planes.append(new_plane)

        self._palettes.writeText('Созданы габаритные плоскости')
        



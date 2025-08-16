import adsk.core
from .base import Cabinet
from .panel import Panel

class KitchenCabinet(Cabinet):


    def calculate_size(self):
        if self.joint_type == 'Side-on-bottom':
            hor_width = self.width - 2 * self.side_thickness      
            hor_depth = self.depth                                
            ver_width = self.height                              
            ver_depth = self.depth                               
            back_width = self.width - 2 * self.side_thickness     
            back_height = self.height - 2 * self.side_thickness   
        elif self.joint_type == 'Bottom-between-sides':
            hor_width = self.width      
            hor_depth = self.depth                                
            ver_width = self.height- 2 * self.side_thickness                               
            ver_depth = self.depth                               
            back_width = self.width - 2 * self.side_thickness     
            back_height = self.height - 2 * self.side_thickness
        else:
            raise ValueError(f'Unknown joint type: {self.joint_type}')

        size = {
            'hor_panel': {
                'width': hor_width,
                'depth': hor_depth
                },
            'ver_panel': {
                'width': ver_width,
                'depth': ver_depth
                },
            'back_panel': {
                 'width': back_width, 
                 'height': back_height
            }}

        return size
    
    def create_panels(self):

        self.all_size = self.calculate_size()
        
        size = self.all_size['hor_panel']
                
        self.bottom_panel = Panel()
        self.bottom_panel.add(
            self.base_planes[0], size['width'], size['depth'], 
            self.side_thickness, self.face_thickness, 'bottom'
            )
        
        self.top_panel = Panel()
        self.top_panel.add(
            self.base_planes[1], size['width'], size['depth'], 
            self.side_thickness, self.face_thickness, 'top'
            )
        
        size = self.all_size['ver_panel']

        self.left_panel = Panel()
        self.left_panel.add(
            self.base_planes[2], size['width'], size['depth'], 
            self.side_thickness, self.face_thickness, 'left'
            )
        
        self.right_panel = Panel()
        self.right_panel.add(
            self.base_planes[3], size['width'], size['depth'], 
            self.side_thickness, self.face_thickness, 'right'
            )
        
        size = self.all_size['back_panel']

        self.back_panel = Panel()
        self.back_panel.add(
            self.base_planes[5], size['width'], size['height'], 
            self.side_thickness, self.face_thickness, 'back'
            )
        
      
        self.face_panel = Panel()
        self.face_panel.add(
            self.base_planes[4], self.width, self.height, 
            self.side_thickness, self.face_thickness, 'face'
            )
        self.face_panel.inner_face = self.face_panel.extrude.startFaces.item(0)


    

        

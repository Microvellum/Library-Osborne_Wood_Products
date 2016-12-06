"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_classes

ARCHITECTURAL_COLUMNS_PATH = os.path.join(os.path.dirname(__file__),"Architectural Columns")
CABINET_FURNITURE_FEET_PATH = os.path.join(os.path.dirname(__file__),"Cabinet _ Furniture Feet")
CABINET_MOLDING_PATH = os.path.join(os.path.dirname(__file__),"Cabinet Molding")
CORBELS_BRACKETS_PATH = os.path.join(os.path.dirname(__file__),"Corbels _ Brackets")
KITCHEN_ISLAND_LEGS_PATH = os.path.join(os.path.dirname(__file__),"Kitchen Island Legs")
PEDESTALS_MORE_PATH = os.path.join(os.path.dirname(__file__),"Pedestals _ More")


#---------PRODUCT: Architectural Columns
        
class PRODUCT_OWP_1610(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Architectural Columns"
        self.assembly_name = "OWP 1610"
        self.appliance_path = os.path.join(ARCHITECTURAL_COLUMNS_PATH,"OWP 1610.blend")
        
class PRODUCT_OWP_1620(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Architectural Columns"
        self.assembly_name = "OWP 1620"
        self.appliance_path = os.path.join(ARCHITECTURAL_COLUMNS_PATH,"OWP 1620.blend")
        
class PRODUCT_OWP_1656(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Architectural Columns"
        self.assembly_name = "OWP 1656"
        self.appliance_path = os.path.join(ARCHITECTURAL_COLUMNS_PATH,"OWP 1656.blend")
        
class PRODUCT_OWP_1683(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Architectural Columns"
        self.assembly_name = "OWP 1683"
        self.appliance_path = os.path.join(ARCHITECTURAL_COLUMNS_PATH,"OWP 1683.blend")
        
class PRODUCT_OWP_1693(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Architectural Columns"
        self.assembly_name = "OWP 1693"
        self.appliance_path = os.path.join(ARCHITECTURAL_COLUMNS_PATH,"OWP 1693.blend")
        
#-------PRODUCT: Cabinet _ Furniture Feet

class PRODUCT_OWP_4000(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4000"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4000.blend")

class PRODUCT_OWP_4001(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4001"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4001.blend")

class PRODUCT_OWP_4002(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4002"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4002.blend")

class PRODUCT_OWP_4003(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4003"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4003.blend")

class PRODUCT_OWP_4005(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4005"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4005.blend")

class PRODUCT_OWP_4011(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4011"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4011.blend")

class PRODUCT_OWP_4012(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4012"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4012.blend")

class PRODUCT_OWP_4015(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4015"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4015.blend")

class PRODUCT_OWP_4040(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4040"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4040.blend")

class PRODUCT_OWP_4045(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4045"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4045.blend")

class PRODUCT_OWP_4050(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4050"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4050.blend")

class PRODUCT_OWP_4055(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4055"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4055.blend")

class PRODUCT_OWP_4070(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4070"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4070.blend")

class PRODUCT_OWP_4075(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4075"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4075.blend")

class PRODUCT_OWP_4076(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4076"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4076.blend")

class PRODUCT_OWP_4080(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4080"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4080.blend")

class PRODUCT_OWP_4081(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4081"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4081.blend")

class PRODUCT_OWP_4082(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4082"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4082.blend")

class PRODUCT_OWP_4084(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4084"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4084.blend")

class PRODUCT_OWP_4090(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4090"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4090.blend")

class PRODUCT_OWP_4091(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4091"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4091.blend")

class PRODUCT_OWP_4095(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4095"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4095.blend")

class PRODUCT_OWP_4097(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4097"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4097.blend")

class PRODUCT_OWP_4100(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4100"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4100.blend")

class PRODUCT_OWP_4101(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4101"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4101.blend")

class PRODUCT_OWP_4102(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4102"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4102.blend")

class PRODUCT_OWP_4113(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4113"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4113.blend")

class PRODUCT_OWP_4115(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4115"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4115.blend")

class PRODUCT_OWP_4116(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4116"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4116.blend")

class PRODUCT_OWP_4120(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4120"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4120.blend")

class PRODUCT_OWP_4125(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4125"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4125.blend")

class PRODUCT_OWP_4202(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4202"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4202.blend")

class PRODUCT_OWP_4203(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4203"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4203.blend")

class PRODUCT_OWP_4215(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4215"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4215.blend")

class PRODUCT_OWP_4220(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4220"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4220.blend")

class PRODUCT_OWP_4250(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4250"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4250.blend")

class PRODUCT_OWP_4255(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4255"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4255.blend")

class PRODUCT_OWP_4260(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4260"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4260.blend")

class PRODUCT_OWP_4265(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4265"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4265.blend")

class PRODUCT_OWP_4270(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4270"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4270.blend")

class PRODUCT_OWP_4275(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4275"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4275.blend")

class PRODUCT_OWP_4300(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4300"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4300.blend")

class PRODUCT_OWP_4301(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4301"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4301.blend")

class PRODUCT_OWP_4302(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4302"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4302.blend")

class PRODUCT_OWP_4303(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4303"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4303.blend")

class PRODUCT_OWP_4402(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 4402"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 4402.blend")

class PRODUCT_OWP_6141(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 6141"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 6141.blend")

class PRODUCT_OWP_6146(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 6146"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 6146.blend")

class PRODUCT_OWP_6151(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet _ Furniture Feet"
        self.assembly_name = "OWP 6151"
        self.appliance_path = os.path.join(CABINET_FURNITURE_FEET_PATH,"OWP 6151.blend")
        
#-------PRODUCT: CABINET MOLDINGS

class PRODUCT_OWP_6985_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.24.blend")

class PRODUCT_OWP_6985_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.36.blend")
        
class PRODUCT_OWP_6985_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.48.blend")
        
class PRODUCT_OWP_6985_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.60.blend")
        
class PRODUCT_OWP_6985_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.72.blend")
        
class PRODUCT_OWP_6985_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.84.blend")
        
class PRODUCT_OWP_6985_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6985.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6985.96.blend")
        
class PRODUCT_OWP_6986_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.24.blend")
        
class PRODUCT_OWP_6986_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.48.blend")
        
class PRODUCT_OWP_6986_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.60.blend")
        
class PRODUCT_OWP_6986_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.72.blend")
        
class PRODUCT_OWP_6986_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.84.blend")
        
class PRODUCT_OWP_6986_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6986.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6986.96.blend")
        
class PRODUCT_OWP_6988_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.24.blend")
        
class PRODUCT_OWP_6988_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.36.blend")
        
class PRODUCT_OWP_6988_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.48.blend")
        
class PRODUCT_OWP_6988_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.60.blend")
        
class PRODUCT_OWP_6988_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.72.blend")
        
class PRODUCT_OWP_6988_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.84.blend")
        
class PRODUCT_OWP_6988_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6988.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6988.96.blend")
        
class PRODUCT_OWP_6990(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6990"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6990.blend")
        
class PRODUCT_OWP_6991(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6991"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6991.blend")
        
class PRODUCT_OWP_6992(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6992"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6992.blend")
        
class PRODUCT_OWP_6995(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6995"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6995.blend")
        
class PRODUCT_OWP_6996(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6996"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6996.blend")
        
class PRODUCT_OWP_6998(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 6998"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 6998.blend")
        
class PRODUCT_OWP_7101(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7101"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7101.blend")
        
class PRODUCT_OWP_7102(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7102"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7102.blend")
        
class PRODUCT_OWP_7105_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.24.blend")
        
class PRODUCT_OWP_7105_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.36.blend")
        
class PRODUCT_OWP_7105_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.48.blend")
        
class PRODUCT_OWP_7105_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.60.blend")
        
class PRODUCT_OWP_7105_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.72.blend")
        
class PRODUCT_OWP_7105_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.84.blend")
        
class PRODUCT_OWP_7105_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7105.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7105.96.blend")
        
class PRODUCT_OWP_7106_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.24.blend")
        
class PRODUCT_OWP_7106_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.36.blend")
        
class PRODUCT_OWP_7106_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.48.blend")
        
class PRODUCT_OWP_7106_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.60.blend")
        
class PRODUCT_OWP_7106_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.72.blend")
        
class PRODUCT_OWP_7106_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.84.blend")
        
class PRODUCT_OWP_7106_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7106.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7106.96.blend")
        
class PRODUCT_OWP_7107_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.24.blend")
        
class PRODUCT_OWP_7107_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.36.blend")
        
class PRODUCT_OWP_7107_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.48.blend")
        
class PRODUCT_OWP_7107_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.60.blend")
        
class PRODUCT_OWP_7107_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.72.blend")
        
class PRODUCT_OWP_7107_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.84.blend")
        
class PRODUCT_OWP_7107_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7107.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7107.96.blend")
        
class PRODUCT_OWP_7108_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.24.blend")
        
class PRODUCT_OWP_7108_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.36.blend")
        
class PRODUCT_OWP_7108_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.48.blend")
        
class PRODUCT_OWP_7108_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.60.blend")
        
class PRODUCT_OWP_7108_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.72.blend")
        
class PRODUCT_OWP_7108_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.84.blend")
        
class PRODUCT_OWP_7108_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7108.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7108.96.blend")
        
class PRODUCT_OWP_7115(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7115"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7115.blend")
        
class PRODUCT_OWP_7121(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7121"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7121.blend")
        
class PRODUCT_OWP_7125(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7125"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7125.blend")
        
class PRODUCT_OWP_7200(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7200"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7200.blend")
        
class PRODUCT_OWP_7205_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.24.blend")
        
class PRODUCT_OWP_7205_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.36.blend")
        
class PRODUCT_OWP_7205_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.48.blend")
        
class PRODUCT_OWP_7205_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.60.blend")
        
class PRODUCT_OWP_7205_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.72.blend")
        
class PRODUCT_OWP_7205_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.84.blend")
        
class PRODUCT_OWP_7205_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7205.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7205.96.blend")
        
class PRODUCT_OWP_7206_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.24.blend")
        
class PRODUCT_OWP_7206_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.36.blend")
        
class PRODUCT_OWP_7206_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.48.blend")
        
class PRODUCT_OWP_7206_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.60.blend")
        
class PRODUCT_OWP_7206_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.72.blend")
        
class PRODUCT_OWP_7206_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.84.blend")
        
class PRODUCT_OWP_7206_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7206.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7206.96.blend")
        
class PRODUCT_OWP_7207_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.24.blend")
        
class PRODUCT_OWP_7207_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.36.blend")
        
class PRODUCT_OWP_7207_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.48.blend")
        
class PRODUCT_OWP_7207_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.60.blend")
        
class PRODUCT_OWP_7207_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.72.blend")
        
class PRODUCT_OWP_7207_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.84.blend")
        
class PRODUCT_OWP_7207_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7207.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7207.96.blend")
        
class PRODUCT_OWP_7208_24(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.24"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.24.blend")
        
class PRODUCT_OWP_7208_36(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.36"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.36.blend")
        
class PRODUCT_OWP_7208_48(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.48"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.48.blend")
        
class PRODUCT_OWP_7208_60(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.60"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.60.blend")
        
class PRODUCT_OWP_7208_72(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.72"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.72.blend")
        
class PRODUCT_OWP_7208_84(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.84"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.84.blend")
        
class PRODUCT_OWP_7208_96(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7208.96"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7208.96.blend")
        
class PRODUCT_OWP_7210(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7210"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7210.blend")
        
class PRODUCT_OWP_7211(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7211"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7211.blend")
        
class PRODUCT_OWP_7212(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7212"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7212.blend")
        
class PRODUCT_OWP_7213(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7213"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7213.blend")
        
class PRODUCT_OWP_7214(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7214"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7214.blend")
        
class PRODUCT_OWP_7215(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7215"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7215.blend")
        
class PRODUCT_OWP_7221(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7221"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7221.blend")
        
class PRODUCT_OWP_7225(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 7225"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 7225.blend")
        
#--------PRODUCT: CORBELS BRACKETS

class PRODUCT_OWP_8004(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8004"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8004.blend")        

class PRODUCT_OWP_8008(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8008"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8008.blend")        

class PRODUCT_OWP_8013(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8013"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8013.blend")        

class PRODUCT_OWP_8018(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8018"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8018.blend")        

class PRODUCT_OWP_8019(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8019"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8019.blend")        

class PRODUCT_OWP_8023(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8023"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8023.blend")        

class PRODUCT_OWP_8028(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8028"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8028.blend")        

class PRODUCT_OWP_8059(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8059"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8059.blend")        

class PRODUCT_OWP_8070(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8070"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8070.blend")        

class PRODUCT_OWP_8083(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8083"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8083.blend")        

class PRODUCT_OWP_8088(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8088"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8088.blend")        

class PRODUCT_OWP_8223(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8223"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8223.blend")        

class PRODUCT_OWP_8228(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8228"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8228.blend")        

class PRODUCT_OWP_8320(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8320"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8320.blend")        

class PRODUCT_OWP_8330(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8330"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8330.blend")        

class PRODUCT_OWP_8700(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8700"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8700.blend")        

class PRODUCT_OWP_8900(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8900"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8900.blend")        

class PRODUCT_OWP_8950(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 8950"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 8950.blend")        

class PRODUCT_OWP_80041(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80041"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80041.blend")        

class PRODUCT_OWP_80181(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80181"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80181.blend")        

class PRODUCT_OWP_80191(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80191"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80191.blend")        

class PRODUCT_OWP_80281(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80281"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80281.blend")        

class PRODUCT_OWP_80591(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80591"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80591.blend")        

class PRODUCT_OWP_80881(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 80881"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 80881.blend")        

class PRODUCT_OWP_82281(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Corbels-Brackets"
        self.assembly_name = "OWP 82281"
        self.appliance_path = os.path.join(CORBELS_BRACKETS_PATH,"OWP 82281.blend")
        
#-------PRODUCT: KITCHEN ISLAND LEGS

class PRODUCT_OWP_82281(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Cabinet Moldings"
        self.assembly_name = "OWP 82281"
        self.appliance_path = os.path.join(CABINET_MOLDING_PATH,"OWP 82281.blend")               





























































                
        
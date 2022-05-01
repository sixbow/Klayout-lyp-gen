from xml.dom.minidom import Document

## Import Ordered dict : This is similar to the type of dict used in PyClewin from sebastiaan.
import numpy as np
from collections import OrderedDict # This is a dictionary where the key-value pairs are ordered
layers = OrderedDict()
#layers = collections.OrderedDict()
layers['NbTiN_GND'] =  '0ff00ff00' # Note: '0' denotes full outline 'ff' denotes the filling in Clewin , '00ff00' denotes the HEX color value. This is appended 
# and we will slice this again to convert it in a way that is compatible with 
layers['SiC'] = '050000aa'
layers['NbTiN_Top'] = '0ff0000ff'
layers['Polyimide'] = '0ff0f000'
layers['Aluminum'] = '0fff0000'
layers['text'] = '05000000'
## /Import Ordered dict


print( layers.keys()[1])
print(layers.values()[1])

dict_length = len(layers.keys()) # Obtains the length of the user defined dict. 


doc = Document()

root = doc.createElement('layer-properties')
doc.appendChild(root)

#layer_index_arr = ['0','1','2','4','5','8','9']
#name_arr = ['NbTiN_GND','SiC','NbTiN_Top','Aluminium','text','E-beam_Alu','2inch Circle']
#color_arr = ['#ffa500','#A908B5','#ff4500','#0000ff','#gggg00','#44gg00','#0044gg']
#pattern_arr = ['I0','I9','I0','I0','I4','I5','I1']
for i in range(dict_length):
    #Begin: This block makes the name property for a layer.
    KL_layers = doc.createElement('properties')
    root.appendChild(KL_layers)
    subKL_layers = doc.createElement('name')
    KL_layers.appendChild(subKL_layers)
    text = doc.createTextNode(layers.keys[i])
    subKL_layers.appendChild(text)
    subKL_layers = doc.createElement('frame-color')
    KL_layers.appendChild(subKL_layers)
    text = doc.createTextNode(layers.value()[i])
    subKL_layers.appendChild(text)
    subKL_layers = doc.createElement('fill-color')
    KL_layers.appendChild(subKL_layers)
    text = doc.createTextNode(layers.value[i])
    subKL_layers.appendChild(text)
    subKL_layers = doc.createElement('dither-pattern')
    KL_layers.appendChild(subKL_layers)
    text = doc.createTextNode(pattern_arr[i])
    subKL_layers.appendChild(text)
    subKL_layers = doc.createElement('source')
    KL_layers.appendChild(subKL_layers)
    text = doc.createTextNode(layer_index_arr[i]+'/0@1')
    subKL_layers.appendChild(text)
    #End: of property ("Layer") block.







# End of the document contains empty name 
placehold_name = doc.createElement('name')
root.appendChild(placehold_name)


xml_str = doc.toprettyxml(indent ="\t") 
  
save_path_file = "KLayout_CKID_Layer_properties.lyp" #Name of the xml file
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
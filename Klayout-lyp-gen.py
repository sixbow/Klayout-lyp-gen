
# Python version 2.7.18 is assumed.

## Import Ordered dict : This is similar to the type of dict used in PyClewin from sebastiaan.
import numpy as np
from collections import OrderedDict # This is a dictionary where the key-value pairs are ordered
layers = OrderedDict()
#layers = collections.OrderedDict()
 # Note: '0' denotes full outline 'ff' denotes the filling in Clewin , '00ff00' denotes the HEX color value. This is appended 
# and we will slice this again to convert it in a way that is compatible with 
layers['NbTiN_GND'] =  '0f00ff00'
layers['SiC'] = '050000aa'
layers['NbTiN_Top'] = '0f0000ff'
layers['Polyimide'] = '0ff0f000'
layers['Aluminum'] = '0fff0000'
layers['text'] = '05000000'
## /Import Ordered dict

#Klayout_lyp_gen function (Part 1)
from xml.dom.minidom import Document
def Klayout_lyp_gen(layers, file_name='Klayout_layer_properties.lyp'):
    """Klayout_lyp_gen(layers, file_name= 'Klayout_layer_properties.lyp')
    Reads layer dictionary and writes .lyp file for use in Klayout.

    Parameters:
    argument1 (Ordered dict): layers file from PyClewin
    argument2 (string): file name used to write layer properties to 
    default: Klayout_layer_properties.lyp
    Example: filename[:-4]+'.lyp'    |  this way filename can be 'MyChip.cif' and then layer file becomes 'MyChip.lyp'

    Returns:
    Nothing!
    Side Effect: Writes .lyp file for use in Klayout

   """
    
    dict_length = len(layers.keys()) # Obtains the length of the user defined dict. 
    layer_index_arr = list(range(0,dict_length))
    fill_lookup = OrderedDict()
    fill_lookup['f'] = 'I0'
    fill_lookup['3'] = 'I9'
    fill_lookup['2'] = 'I5'
    fill_lookup['5'] = 'I4' # Double hatch is converted to tight hatching in Klayout because Klayout does not have this option.
    out_lookup = OrderedDict()
    out_lookup['0'] = 'I0'
    out_lookup['1'] = 'I6'
    out_lookup['2'] = 'I4'
    out_lookup['3'] = 'I5'
    out_lookup['4'] = 'I3'
    try:
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
            text = doc.createTextNode(layers.keys()[i])
            subKL_layers.appendChild(text)
            subKL_layers = doc.createElement('frame-color')
            KL_layers.appendChild(subKL_layers)
            text = doc.createTextNode('#'+layers.values()[i][2:8][::-1])
            subKL_layers.appendChild(text)
            subKL_layers = doc.createElement('fill-color')
            KL_layers.appendChild(subKL_layers)
            text = doc.createTextNode('#'+layers.values()[i][2:8][::-1])
            subKL_layers.appendChild(text)
            subKL_layers = doc.createElement('dither-pattern')
            KL_layers.appendChild(subKL_layers)
            text = doc.createTextNode(fill_lookup[layers.values()[i][1]])
            subKL_layers.appendChild(text)
            subKL_layers = doc.createElement('line-style')
            KL_layers.appendChild(subKL_layers)
            text = doc.createTextNode(out_lookup[layers.values()[i][0]])
            subKL_layers.appendChild(text)
            subKL_layers = doc.createElement('source')
            KL_layers.appendChild(subKL_layers)
            text = doc.createTextNode(str(layer_index_arr[i])+'/0@1')
            subKL_layers.appendChild(text)
            #End: of property ("Layer") block.

        # End of the document contains empty name 
        placehold_name = doc.createElement('name')
        root.appendChild(placehold_name)
        xml_str = doc.toprettyxml(indent ="\t") 
        
        
        with open(file_name, "w") as f:
            f.write(xml_str) 
        print('Klayout-lyp-gen-addon: Succes! wrote: '+file_name)
    
    except Exception,e: print("Klayout-lyp-gen-addon:"+str(e)+"\n Klayout-lyp-gen-addon: Whoops-a-daisy. These are not supported parameters for Klayout-lyp-gen-addon!. Not generating lyp file")
#/Klayout_lyp_gen function (End Part 1)

#Calling the lyp_gen. (Part 2) - This needs to be done after definition of layers, save_path_file
save_path_file = "my_Klayout_layersV0.lyp" #Name of the xml file
Klayout_lyp_gen(layers,save_path_file)
#Calling the lyp_gen. (Part 2)


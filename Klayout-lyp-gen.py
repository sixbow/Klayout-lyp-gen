


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
from xml.dom.minidom import Document



def Klayout_lyp_gen(layers, file_name ):
    print( layers.keys()[1])
    print(layers.values()[1][0])
    print(layers.values()[1][1])
    print(layers.values()[1][2:8])
    print(layers['text'])

    dict_length = len(layers.keys()) # Obtains the length of the user defined dict. 
    print(dict_length)
    layer_index_arr = list(range(0,dict_length))
    print(layer_index_arr)
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

    print(layers.values()[0][2:8])

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
        

        with open(save_path_file, "w") as f:
            f.write(xml_str) 

    except:
        print("Klayout-lyp-gen-addon: Whoops-a-daisy. These are not supported parameters for Klayout-lyp-gen-addon!. Not generating lyp file")
save_path_file = "KLayout_Layer_properties.lyp" #Name of the xml file
Klayout_lyp_gen(layers,save_path_file)
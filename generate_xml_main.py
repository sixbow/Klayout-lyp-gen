from xml.dom.minidom import Document

doc = Document()

root = doc.createElement('layer-properties')
doc.appendChild(root)

layer_index_arr = ['0','1','2','4','5','8','9']
name_arr = ['NbTiN_GND','SiC','NbTiN_Top','Aluminium','text','E-beam_Alu','2inch Circle']
color_arr = ['#ffa500','#A908B5','#ff4500','#0000ff','#gggg00','#44gg00','#0044gg']
pattern_arr = ['I0','I9','I0','I0','I4','I5','I1']
for i in range(len(name_arr)):
    #Begin: This block makes the name property for a layer.
    layers = doc.createElement('properties')
    root.appendChild(layers)
    sublayers = doc.createElement('name')
    layers.appendChild(sublayers)
    text = doc.createTextNode(name_arr[i])
    sublayers.appendChild(text)
    sublayers = doc.createElement('frame-color')
    layers.appendChild(sublayers)
    text = doc.createTextNode(color_arr[i])
    sublayers.appendChild(text)
    sublayers = doc.createElement('fill-color')
    layers.appendChild(sublayers)
    text = doc.createTextNode(color_arr[i])
    sublayers.appendChild(text)
    sublayers = doc.createElement('dither-pattern')
    layers.appendChild(sublayers)
    text = doc.createTextNode(pattern_arr[i])
    sublayers.appendChild(text)
    sublayers = doc.createElement('source')
    layers.appendChild(sublayers)
    text = doc.createTextNode(layer_index_arr[i]+'/0@1')
    sublayers.appendChild(text)
    #End: of property ("Layer") block.







# End of the document contains empty name 
placehold_name = doc.createElement('name')
root.appendChild(placehold_name)


xml_str = doc.toprettyxml(indent ="\t") 
  
save_path_file = "KLayout_CKID_Layer_properties.lyp" #Name of the xml file
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
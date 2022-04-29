from xml.dom.minidom import Document

doc = Document()

root = doc.createElement('layer-properties')
doc.appendChild(root)
layer1 = doc.createElement('properties')
root.appendChild(layer1)

sublayer1 = doc.createElement('name')
layer1.appendChild(sublayer1)


text = doc.createTextNode('Some text here')
sublayer1.appendChild(text)

xml_str = doc.toprettyxml(indent ="\t") 
  
save_path_file = "KLayout_CKID_Layer_properties.lyp" #Name of the xml file
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
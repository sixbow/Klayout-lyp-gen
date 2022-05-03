# Klayout-lyp-gen: A layer properties document creator addon for PyClewin 2.7

> Context of this tool: 
> Most of us are using Sebastiaans PyClewin code in one form or another. This creates the mask .cif files and the appropriate layer info 
> to read display the layer infomation in CleWin. However some of us like to use Klayout which works great but the problem is that you 
> don't have any layer information available. With this plugin i want to have a plug-in function that converts the Ordered dictionary > into the appropriate .lyp file (This is essentialy a XML type doc.) 

# Layers in PyClewin
Here i will give some info about what info the ordered dict of PyCleWin currently contains.
I will only discuss the options that i have currently support for.

If we look at an entry into the layers ordered dict of PyCleWin we obtain something like this:

`` layers['NbTiN_GND'] = '0ff00ff00'``

There are 3 parts in this encoding 
From first to last:
- outline 1 char
- hatching/fill 1 char
- hex color 6 char

Here i give a table with the associated values

| type outline | value | 
| --- | --- | 
| Full | 0 | 
|big dash | 1 | 
| dots | 2 | 
| dash dot | 3 | 
| dash dot dot | 4 | 

| type hatching/fill | value | 
| --- | --- | 
| fill | f |
| hatched right bottom to left top | 2 |
| hatched left bottom right top | 3 | 
| hatched dual | 5 |

Now you can append these results starting with outline then type of fill and then hex value to get the look that you want!

# \' Installing \' the code into your codebase.
There are 2 parts that need to be added to your code to make Klayout-lyp-gen work.
## Part 1 
In the code on **line ~19 (Search:(Part 1))** we can see that the ```minidom`` is included and a fuction definiton is given. 
this needs to be copied to somewhere in the beginning of the code after the inclusion of numpy.

## Part 2 
In Sebastiaan his code you make a Ordered dictonary defining the layers called ``layers``. **After** this ordered dictonary you can include part 2.
- You need to give the ordered dict ```layers`` as the first argument 
- You can optionally give a second argument that gives the name of the file you want to create. Make sure it ends in .lyp
Default: 'Klayout_layer_properties.lyp' 
If you run your code now you will get the message:
Succes! ... 
or
Whoops-a-daisy. where the error given is stated above.
I included try except so if it doesn't work your code should not crash.

Enjoy and if you note any bugs you can sent me a message!
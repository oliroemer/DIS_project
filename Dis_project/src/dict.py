
# Mangler at blive fyldt ud:
processor_brand_dict = {
    "AMD": ['A6-9225 Processor','APU Dual','Athlon Dual','Quad','Dual Core','Ryzen','Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9'] , 
    "Intel": ['Celeron Dual','Dual Core','Core','Core i3','Core i5','Core i7','Core i9','Core m3','Ever Screenpad','GeForce GTX','GeForce RTX','GEFORCE RTX','Hexa Core','Genuine Windows','Pentium Quad'],
    "M1": ['M1'], 
    "MediaTek": ['MediaTek Kompanio'],
    "Qualcomm": ['Snapdragon 7c']
} 
weight = {
    "Gaming": 1 , 
    "Casual": 2,
    "ThinNlight": 3
} 

processer_name_revert = {
    8: ['Snapdragon 7c', 'Core i9','Ryzen 9'],
    5 : ['Ryzen 3'],
    4 : ['Core i5'],
    2 : ['M1'],
    1 : ['GeForce RTX','Dual Core','Celeron Dual','Ryzen',
    'Core i7','A6-9225 Processor','Ever Screenpad','Ryzen 5',
    'Core m3','GeForce GTX', 'MediaTek Kompanio','Hexa Core', 
    'GEFORCE RTX','Genuine Windows','APU Dual','Athlon Dual',
    'Pentium Quad','Quad','Core','Pentium Silver','Core i3']
}


Processor_name = {
    'M1': 2 , 
    'GeForce RTX': 1 , 
    'Celeron Dual': 1 , 
    'Dual Core': 1 , 
    'Ryzen 9': 8 , 
    'Snapdragon 7c': 8 , 
    'Core i7': 1 , 
    'Ryzen': 1 , 
    'A6-9225 Processor': 1 , 
    'Ever Screenpad': 1 , 
    'Ryzen 5': 1 , 
    'Core m3': 1 , 
    'GeForce GTX': 1 , 
    'MediaTek Kompanio': 1 , 
    'Ryzen 7': 8 , 
    'Hexa Core': 1 , 
    'GEFORCE RTX': 1 , 
    'Core i5': 4 , 
    'Ryzen 3': 5 , 
    'Genuine Windows': 1 , 
    'APU Dual': 1 , 
    'Athlon Dual': 1 , 
    'Pentium Quad': 1 , 
    'Core i9': 8 , 
    'Quad': 1 , 
    'Core': 1 , 
    'Pentium Silver': 1 , 
    'Core i3': 1
    }



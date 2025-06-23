import math

def distance_lat_long(lat1, lon1, lat2, lon2):
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    radius = 6371.0
    
    distance = radius * c
    return distance

f = open("C:\\Users\\USER\\Downloads\\Data_Algorithims\\HW1\\sample_dataset\\trees_complex.txt", "r")
lines = [line.strip() for line in f] 

f.close()

header = lines[0].split('\t')  

id_dict = {}
latitude_dict = {}
longitude_dict = {}
tree_type_dict = {}
height_dict = {}

for line in lines[1:]:  
    parts = line.split('\t')
    
    
    id_dict[parts[0]] = parts[0]
    
    latitude_dict[parts[0]] = float(parts[1]) 
    longitude_dict[parts[0]] = float(parts[2]) 
    
    tree_type_dict[parts[0]] = parts[3]
    height_dict[parts[0]] = float(parts[4]) 


min_height = float('inf')  
max_height = float('-inf')  
min_height_id = None
max_height_id = None
min_tree_type = None
max_tree_type = None


for tree_id, height in height_dict.items():
    if height < min_height:
        min_height = height
        min_height_id = tree_id
        min_tree_type = tree_type_dict[tree_id]  

    
    if height > max_height:
        max_height = height
        max_height_id = tree_id
        max_tree_type = tree_type_dict[tree_id]  


min_tree_type = tree_type_dict[min_height_id]
max_tree_type = tree_type_dict[max_height_id]

print(f"Minimum height: {min_height} meters")
print(f"ID of minimum height: {min_height_id}")
print(f"Tree type of minimum height: {min_tree_type}")

print(f"Maximum height: {max_height} meters")
print(f"ID of maximum height: {max_height_id}")
print(f"Tree type of maximum height: {max_tree_type}")
min_lat = latitude_dict[min_height_id]
min_lon = longitude_dict[min_height_id]
max_lat = latitude_dict[max_height_id]
max_lon = longitude_dict[max_height_id]


distance = distance_lat_long(min_lat, min_lon, max_lat, max_lon)

print("Distance of minimum points to maximum height",distance)

tree_type_min_max = {}

for tree_id, tree_type in tree_type_dict.items():
    height = height_dict[tree_id]
    if tree_type not in tree_type_min_max:
        tree_type_min_max[tree_type] = {'min': {'height': float('inf'), 'id': None}, 'max': {'height': float('-inf'), 'id': None}}
    
    if height < tree_type_min_max[tree_type]['min']['height']:
        tree_type_min_max[tree_type]['min']['height'] = height
        tree_type_min_max[tree_type]['min']['id'] = tree_id
    
    if height > tree_type_min_max[tree_type]['max']['height']:
        tree_type_min_max[tree_type]['max']['height'] = height
        tree_type_min_max[tree_type]['max']['id'] = tree_id

print("\nMinimum and Maximum Height by Tree Type:")
for tree_type, min_max in tree_type_min_max.items():
    print(f"Tree Type: {tree_type}")
    print(f"  Minimum Height: {min_max['min']['height']} meters, ID: {min_max['min']['id']}")
    print(f"  Maximum Height: {min_max['max']['height']} meters, ID: {min_max['max']['id']}")

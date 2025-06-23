f = open("C:\\Users\\USER\\Downloads\\Data_Algorithims\\HW1\\sample_dataset\\trees_1.txt", "r")
with open("trees_1.txt", "r", encoding="utf-8") as file:
    liste = file.readlines()  
header = f.readline()
record = f.readline().strip("\n").split("\t")  
print(record)  

new_height = float(record[4]) + 5 
print(new_height)

f.close()
f = open("C:\\Users\\USER\\Downloads\\Data_Algorithims\\HW1\\sample_dataset\\trees_1.txt", "r")
list = [line.strip() for line in f]  
cleaned_data = []

for row in list[1:]:  
    columns = row.split('\t')
    cleaned_data.append([columns[1], columns[2], columns[3], columns[4]])


for entry in cleaned_data:
    print(entry) 
cleaned_data = []
for line in list:
    cleaned_line = line.replace('\t', ',')  
    cleaned_data.append(cleaned_line)

for line in cleaned_data:
    print(line)

numbers = cleaned_data    

min_value = numbers[0]
max_value = numbers[0]


for num in numbers:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num

print("Minimum Değer:", min_value)
print("Maksimum Değer:", max_value)
print(list)






f = open("C:\\Users\\USER\\Downloads\\Data_Algorithims\\HW1\\sample_dataset\\trees_1.txt", "r")
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
    latitude_dict[parts[0]] = parts[1]
    longitude_dict[parts[0]] = parts[2]
    tree_type_dict[parts[0]] = parts[3]
    height_dict[parts[0]] = parts[4]


print("ID Dictionary:", id_dict)
print("Latitude Dictionary:", latitude_dict)
print("Longitude Dictionary:", longitude_dict)
print("Tree Type Dictionary:", tree_type_dict)
print("Height Dictionary:", height_dict)
with open('wards.csv') as f:
    lines = f.readlines()

print("Number of lines is ", len(lines))

for line in lines:
    print(line.strip())

    # for line in lines[1:]:
    #     parts = line.strip().split(",")
    #     wards = parts[0]
    #     area = parts[1]
    #     print(wards, " has an area of", area)

# for line in lines[1:]:
#     parts = line.strip().split(",")
#     wards = parts[0]
#     area_km2 = float(parts[1])
#     area_hectares = area_km2 * 100


#     print(wards, " is ", round(area_hectares,1), "hectares")

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 20:
        size = "Large"
    else:
        size = "Small"  
    print(ward, 'is', size)
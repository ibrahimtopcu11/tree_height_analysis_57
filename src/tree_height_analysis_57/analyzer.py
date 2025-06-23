from .distancefunction import distance_lat_long

def parse_tree_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    header = lines[0].split('\t')
    data = [line.split('\t') for line in lines[1:]]

    trees = {
        "id": {}, "lat": {}, "lon": {}, "type": {}, "height": {}
    }

    for row in data:
        tid = row[0]
        trees["id"][tid] = tid
        trees["lat"][tid] = float(row[1])
        trees["lon"][tid] = float(row[2])
        trees["type"][tid] = row[3]
        trees["height"][tid] = float(row[4])
    
    return trees

def analyze_tree_heights(trees):
    min_id = min(trees["height"], key=trees["height"].get)
    max_id = max(trees["height"], key=trees["height"].get)
    
    result = {
        "min": {
            "id": min_id,
            "type": trees["type"][min_id],
            "height": trees["height"][min_id],
            "lat": trees["lat"][min_id],
            "lon": trees["lon"][min_id]
        },
        "max": {
            "id": max_id,
            "type": trees["type"][max_id],
            "height": trees["height"][max_id],
            "lat": trees["lat"][max_id],
            "lon": trees["lon"][max_id]
        },
        "distance": distance_lat_long(
            trees["lat"][min_id], trees["lon"][min_id],
            trees["lat"][max_id], trees["lon"][max_id]
        )
    }
    return result
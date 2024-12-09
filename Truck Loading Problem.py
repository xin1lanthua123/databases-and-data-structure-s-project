class Parcel:
    def __init__(self, parcel_id, customer_id, destination, weight, distance, volume):
        self.parcel_id = parcel_id
        self.customer_id = customer_id
        self.destination = destination
        self.weight = weight
        self.distance = distance
        self.volume = volume  

    def __repr__(self):
        return (f"Parcel(ID: {self.parcel_id}, Customer: {self.customer_id}, "
                f"Dest: {self.destination}, Weight: {self.weight}, "
                f"Distance: {self.distance}, Volume: {self.volume})")

parcels = [
    Parcel(1, 101, "HCMC", 10, 300, 4),  
    Parcel(2, 102, "Da Nang", 5, 100, 1),  
    Parcel(3, 103, "Da Lat", 8, 200, 2),  
    Parcel(4, 104, "Hanoi", 3, 50, 1),  
    Parcel(5, 105, "Nha Trang", 12, 400, 5),  
    Parcel(6, 106, "Hai Phong", 7, 150, 3)   
]

MAX_TRUCK_CAPACITY_WEIGHT = 20  
MAX_TRUCK_CAPACITY_VOLUME = 10  

def generate_invoice(parcel, rate_per_kg=2, rate_per_km=1):
    return (parcel.weight * rate_per_kg) + (parcel.distance * rate_per_km)


def best_fit(items, weight_capacity, volume_capacity):
    bins = []  
    bin_packing = []  


    for item in items:
        best_bin_index = -1
        min_space_left = float('inf')
        
  
        for i, (total_weight, total_volume) in enumerate(bins):
            weight_space_left = weight_capacity - total_weight
            volume_space_left = volume_capacity - total_volume
            
            if weight_space_left >= item.weight and volume_space_left >= item.volume:
            
                total_space_left = min(weight_space_left, volume_space_left)
                if total_space_left < min_space_left:
                    best_bin_index = i
                    min_space_left = total_space_left

        if best_bin_index == -1:
            bins.append((item.weight, item.volume))
            bin_packing.append([item])  
        else:
            bins[best_bin_index] = (bins[best_bin_index][0] + item.weight, 
                                    bins[best_bin_index][1] + item.volume)
            bin_packing[best_bin_index].append(item)  
    
    return len(bins), bin_packing



parcels.sort(key=lambda x: x.weight, reverse=True)


num_trucks, truck_packing = best_fit(parcels, MAX_TRUCK_CAPACITY_WEIGHT, MAX_TRUCK_CAPACITY_VOLUME)


for i, truck in enumerate(truck_packing, 1):
    total_weight = sum(parcel.weight for parcel in truck)
    total_volume = sum(parcel.volume for parcel in truck)
    print(f"\nTruck {i} (Total Weight: {total_weight} kg, Total Volume: {total_volume} m³):")
    for parcel in truck:
        print(f"Parcel: {parcel} - Invoice: ${generate_invoice(parcel)}")

print(f"\nTotal Trucks Used: {num_trucks}")

city_coordinates = {
    "HCMC": (10.8231, 106.6297),
    "Da Nang": (16.0583, 108.2208),
    "Dalat": (11.9401, 108.4550),
    "Nha Trang": (12.2384, 109.1967),
    "Hai Phong": (20.8449, 106.6881)
}

def plan_route(loaded_parcels):
    route = []
    max_stops = 5  # Limit the number of stops
    for parcel in loaded_parcels:
        destination = parcel["destination"]
        if destination not in route and len(route) < max_stops:
            route.append(destination)
    return route, get_coordinates(route)

def get_coordinates(route):
    coordinates = []
    for city in route:
        coordinates.append(city_coordinates[city])
    return coordinates

def main():
    print("Welcome to the Truck Route Planner!")
    loaded_parcels = []

    # Print the list of valid destinations
    print("Available destinations:")
    print(", ".join(city_coordinates.keys()))

    while True:
        destination = input("Enter a destination city (or type 'done' to finish): ")
        if destination.lower() == 'done':
            break
        elif destination in city_coordinates:
            loaded_parcels.append({"destination": destination})
        else:
            print("Invalid destination. Please enter a valid city from the list above.")

    # Generate route
    if loaded_parcels:
        route, coordinates = plan_route(loaded_parcels)

        # Output results
        print("\nPlanned Route:")
        for i, city in enumerate(route, start=1):
            print(f"{i}. {city} - Coordinates: {coordinates[i-1]}")
    else:
        print("No destinations entered.")

if __name__ == "__main__":
    main()

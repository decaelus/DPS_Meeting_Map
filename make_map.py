import folium

# Create a map centered on the United States
us_map = folium.Map(location=[37, -95], zoom_start=4)

# List of cities and their coordinates (you can replace with actual coordinates if available)
cities = [
    ("San Antonio", "TX", 29.4241, -98.4936),
    ("Knoxville", "TN", 35.9596, -83.9207),
    ("Provo", "UT", 40.2361, -111.6585),
    ("Pasadena", "CA", 34.1478, -118.1445),
    ("National Harbor", "MD", 38.8047, -77.0064),
    ("Tucson", "AZ", 32.2217, -110.9265),
    ("Denver", "CO", 39.7392, -104.9903),
    ("Reno", "NV", 39.5296, -119.8138),
    ("Ithaca", "NY", 42.4439, -76.4886),
    ("Orlando", "FL", 28.5383, -81.3792),
    ("Louisville", "KY", 38.2527, -85.7585),
    ("Monterey", "CA", 36.6002, -121.8948),
    ("Birmingham", "AL", 33.5207, -86.8025),
    ("New Orleans", "LA", 29.9511, -90.0715),
    ("Madison", "WI", 43.0747, -89.3844),
    ("Cambridge", "MA", 42.3736, -71.1097),
    ("Kona", "HI", 19.6380, -155.9750),
    ("Bethesda", "MD", 38.9828, -77.0946),
    ("Boulder", "CO", 40.0149, -105.2705),
    ("Palo Alto", "CA", 37.4419, -122.1430),
    ("Charlottesville", "VA", 38.0293, -78.4767),
    ("Providence", "RI", 41.8237, -71.4222),
    ("Austin", "TX", 30.2672, -97.7431),
    ("Baltimore", "MD", 39.2904, -76.6122),
    ("Kailua-Kona", "HI", 19.6871, -155.9956),
    ("Ithaca", "NY", 42.4439, -76.4886),
    ("Pittsburgh", "PA", 40.4406, -79.9959),
    ("Tucson", "AZ", 32.2217, -110.9265),
    ("St. Louis", "MO", 38.6270, -90.1994),
    ("Boston", "MA", 42.3601, -71.0542),
    ("Honolulu", "HI", 21.3069, -157.8583),
    ("Columbia", "MD", 39.1754, -76.7895),
    ("Palo Alto", "CA", 37.4419, -122.1430),
    ("Tallahassee", "FL", 30.4383, -84.2807),
    ("San Francisco", "CA", 37.7749, -122.4194),
    ("Boise", "ID", 43.6150, -116.2023)
]

# Add markers for each city
for city, state, lat, lon in cities:
    folium.Marker(location=[lat, lon], popup=f"{city}, {state}").add_to(us_map)

# Display the map
us_map.save("us_cities_map.html")

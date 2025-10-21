import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, red, yellow

#Defining emojis
walking_emoji = " 🚶"
bus_emoji = " 🚌"
plane_emoji = " ✈️"

print(blue("Welcome to the travel calculator!\n"))

#Prompt user for name of first city and country
first_city = inquirer.prompt([
    inquirer.Text('name', message = "Enter the name of the first city"),
    inquirer.Text('country', message = "Enter the name of the first country")
])

#Prompt user for name of second city and country
second_city = inquirer.prompt([
    inquirer.Text('name', message = "Enter the name of the second city"),
    inquirer.Text('country', message = "Enter the name of the second country")
])

#Get the longitute and latitude of the first city and country
first_location = f"{first_city['name'], {first_city['country']}}"
first_coords = geocoders.Nominatim(user_agent = "distance_calculator").geocode(first_location).point

#Get the longitute and latitude of the second city and country
second_location = f"{second_city['name'], {second_city['country']}}"
second_coords = geocoders.Nominatim(user_agent = "distance_calculator").geocode(second_location).point

#Calculate the distance between the two locations
walk_distance = distance.distance(first_coords, second_coords).km
drive_distance = distance.distance(first_coords, second_coords).km
fly_distance = distance.distance(first_coords, second_coords).km

#Calculate the time to walk the distance
walk_time = walk_distance / 5
#For bus
drive_time = drive_distance / 60
#For plane
fly_time = fly_distance / 800

#Print results
print(green("\nResults"))
print(f"Distance between {first_location} and {second_location} by:")
print(yellow(f"{walking_emoji} Walking: {walk_distance:.2f} km, time: {walk_time:.2f} hours"))
print(yellow(f"{bus_emoji} Driving: {drive_distance:.2f} km, time: {drive_time:.2f} hours"))
print(yellow(f"{plane_emoji} Flying: {fly_distance:.2f} km, time: {fly_time:.2f} hours"))
import os

#!/C:/Users/quent/AppData/Local/Microsoft/WindowsApps/python3.exe


# Prompt for user input
favorite_color = input('What is your favorite color? ')
hometown = input('What is the name of your hometown? ')
favorite_sport = input('What is your favorite sport? ')

# Set environment variables
os.environ["FAVORITE_COLOR"] = favorite_color
os.environ["HOMETOWN"] = hometown
os.environ["FAVORITE_SPORT"] = favorite_sport

# Print environment variables
print("Favorite Color:", os.getenv("FAVORITE_COLOR"))
print("Hometown:", os.getenv("HOMETOWN"))
print("Favorite Sport:", os.getenv("FAVORITE_SPORT"))


# ISS-Tracker-App
Simple Command Line App to alert when ISS is overhead
The program first requests a City location from the user, this is turned into co-ordinates using an API call to openweather geocoder.
The location coordinates are then compared to the current coordinates of the ISS to determine whether they are within a 5 deg square. 
This programs runs ever 60 seconds and repeats, advising the user when the ISS is overhead.

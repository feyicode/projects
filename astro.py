#from sense_hat import SenseHat
import time

start_time = time.time

while (start_time - time.time) % 30 == 0:
  print("x"import csv
from pathlib import Path
from datetime import datetime, timedelta
import time
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS

#gets folder adress that program is in
base_folder = Path(__file__).parent.resolve()

# Set a logfile
logfile(base_folder/"events.log")

logging.info("creating functions")

#create and store data in csv file func.
def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time", "Coordinates")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

#take pic func.
def capture(camera, image):
    """use 'camera' to capture an 'image' file with lat/long EXIF data."""
    camera.capture(image)


logging.info("setting up stuff")

# Set up Sense Hat
sense = SenseHat()

# Set up camera
cam = PiCamera()
cam.resolution = (1296, 972) #RESOLUTION MAY BE INCORRECT!!! CORRECT IT BY FINDING OUT ACTUAL RES.!!!!



#saves a path to data folde(where pics go)
data_file = base_folder/"data.csv"
create_csv_file(data_file)

#initialise photo counter
counter = 1

#record the start and current time
start_time = datetime.now()
now_time = datetime.now()


logging.info("beginning while loop. current time = ", start_time)

#run loop for 85 mins (I CHANGED THIS TO 1 MINUTE FOR TESTING)
while (now_time < start_time + timedelta(minutes=1)):
    try:
        location = ISS.coordinates()

        #capture image
        image_file = f"{base_folder}/photo_{counter:03d}.jpg"
        capture(cam, image_file)
        
        #take data (pic no, time, iss coords)
        data = (counter, datetime.now(), location)
        #deal with data
        add_csv_data(data_file, data)
        

        #log event
        logging.info(f"iteration {counter}")
        counter += 1
        time.sleep(5)#SLEEP TIMER NORMALLY HIGHER - CHANGED TO 5 SEC FOR TESTING

        #update time
        now_time = datetime.now()

    except Exception as e:
        logging.error(f"{e.__class__.__name__}: {e}"))
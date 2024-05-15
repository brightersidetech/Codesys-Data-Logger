# Codesys Data Logger
This simple project demostrates how to create a Codesys Data logger application to save data to a csv file using the SysFile Library. The data logger saves dat to the file with 3  fields namely
- The date the data was logged
- The time at which the data is logged
- The data point

The project uses a simple REST API implemeted in python using the flask Library to generate some random data values and send them back to the client whenever it receives a request. 

The Codesys Application implements a simple rest client to request data from the Flask API

### How it works
1. The PLC (Raspberry Pi in this case) will create a csv file at startup. The file only contains the data header fields at this stage
2. The PLC then requests data from the REST API. 
3. Whenevr a new data point in recieved, the PLC opens the csv file, writes the data (Dat, time, data point), then closes it and waits for new data


### Requirements
- You will need a Codesys Version 3.5.19.5 or higher in order to open the Project file
- You will need a python installation, recommended version 2.7 or higher to run the Flask Server
- I used a Raspberry Pi runing Codesys Runtime for Linux ARM version, but you can adapt the project to your own device
- I saved files on a removable flash disk, but you can change the file path to save the files a a preffered location

### Instructions
- Open the Codesys project and update the device to match your own device
- Install the rquired python libraries by running the following command: ```pip install -r requirements.txt```
- Start the Flask server by running the following command: ```python main.py```
- Update the REST clinet url parameter in the Codesys with the Ethernet interface on which your Flask server is running
- Update the filepath parameter with the excat location where you wish to save your files
- Upload the Codesys project to your device and start it




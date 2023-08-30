# Sensor Data Monitoring and Storage using Firebase and Arduino

This repository showcases a project that demonstrates the integration of Arduino boards, sensor data, Firebase Realtime Database, and a web interface. The project enables you to monitor sensor data collected by Arduino boards, store it in Firebase, and visualize it remotely through a web interface.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Flow](#data-flow)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project illustrates the seamless connection between Arduino boards, sensors, Firebase Realtime Database, and a web-based user interface. The project is divided into different components that work together to achieve the following:

1. **Collecting Sensor Data using Arduino**: Two Arduino code files (`arduino_code_1.ino` and `arduino_code_2.ino`) are provided, each demonstrating the integration of specific sensors. The first code involves collecting data from an MPU6050 accelerometer-gyroscope module, while the second code demonstrates data collection from an ultrasonic distance sensor (HC-SR04).

2. **Transmitting Data to Python using Serial Communication**: The Arduino code reads sensor data and sends it over a serial connection to a Python script (`main.py`). The Python script captures the live data being transmitted from the Arduino boards.

3. **Storing Data in Firebase**: The captured sensor data is then stored in the Firebase Realtime Database using the Firebase Admin SDK. The Python script uses the `firebase-admin` library to push the data into the database.

4. **Fetching Data using JavaScript**: The HTML file (`index.html`) contains JavaScript code (`script.js`) that interacts with the Firebase Realtime Database. The script fetches the stored sensor data and updates the web interface in real-time.

5. **Displaying Data on Web Interface**: The HTML and JavaScript work together to display the sensor data on a web page. When you open the `index.html` file in a web browser, it establishes a connection with Firebase, retrieves data, and updates the displayed values.

## Installation

To set up and use this project, follow these steps:

1. Clone the repository to your local machine.

2. Install the necessary Python libraries using the following command:

   ```bash
   pip install firebase-admin pyserial

    Ensure you have the required hardware components, including Arduino boards and relevant sensors.

    Upload the Arduino code (arduino_code_1.ino and arduino_code_2.ino) to your Arduino boards.

    Replace the Firebase configuration placeholders in the HTML code (index.html) and JavaScript code (script.js) with your actual Firebase project credentials.

## Usage

The project usage involves the following steps:

1.  Run the Arduino code on your boards to collect sensor data.

2. Execute the Python script (main.py) to capture the live sensor data transmitted from the Arduino boards. This script uses the Firebase Admin SDK to store the data in Firebase.

3. Open the index.html file in a web browser to visualize the real-time sensor data. The JavaScript code fetches the data from Firebase and updates the web interface accordingly.

## Data Flow

The data flow in this project can be summarized as follows:

1. Arduino -> Python: Live sensor data is read by Arduino boards and sent over a serial connection to the Python script.

2. Python -> Firebase: The Python script captures the incoming sensor data and uses the Firebase Admin SDK to store it in the Firebase Realtime Database.

3. Firebase -> Web Interface: The JavaScript code in the HTML file interacts with Firebase, fetching the stored sensor data and updating the web interface in real-time.

## File Descriptions

1. main.py: Python script to read sensor data from Arduino boards using a serial connection and store it in the Firebase Realtime Database.
2. index.html: HTML file for the web interface to display the sensor data retrieved from Firebase.
3. script.js: JavaScript code that fetches sensor data from Firebase and updates the web interface.
4. arduino_code_1.ino and arduino_code_2.ino: Arduino code for collecting sensor data using an MPU6050 accelerometer-gyroscope and an ultrasonic distance sensor (HC-SR04).
4. lms-comms-firebase-adminsdk-oknp7-a5dd828112.json: Firebase Admin SDK private key file for authentication.

## Contributing

Contributions are welcome! If you have any ideas for improvement or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

Feel free to customize and enhance this README file to match the specific details and structure of your project.
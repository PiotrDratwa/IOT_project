# **IoT Project: Real-Time Temperature and Speech Monitoring**

The IoT project consists of several integrated modules that work together to measure, process, and display data in real-time. It utilizes technologies such as **ESP8266**, **MQTT**, **Docker**, **Python**, and **Whisper AI**. Below is a detailed description of the project's main functions and the technologies used.

----------

## **Main Project Functions**

### 1. **Temperature Measurement** 🌡️

The **DS18B20** sensor connected to the **ESP8266** microcontroller collects temperature data.

-   **Data Display**: The result is displayed in the Arduino terminal and sent to the MQTT broker.

----------

### 2. **Speech-to-Text** 🗣️

The speech recognition module, based on **Python** and the **Whisper AI** model, converts audio into text.

-   **Data Transmission**: The transcribed text is displayed in the terminal and sent to the MQTT broker.
-   **ESP8266 Reception**: The ESP8266 receives data from the broker, and the result is displayed both in the Arduino terminal and on an LCD screen connected to the board.

----------

### 3. **Data Processing** ⚙️

A **Python** script subscribes to data from the MQTT broker and stores it in an **InfluxDB** database.

-   **Visualization of Changes**: Temperature changes are visualized using **Grafana** charts.

----------

## **🛠️ Technologies**

### 1. **ESP8266** with **DS18B20** sensor and LCD display

-   The microcontroller collects data from the temperature sensor and displays the results on an LCD screen.

### 2. **MQTT Broker**

-   The MQTT broker is responsible for transmitting data between devices.
-   Security mechanisms such as authentication (username, password, TLS) ensure secure communication.

### 3. **Docker**

-   **InfluxDB** and **Grafana** run in Docker containers, ensuring easy setup and environment isolation.

### 4. **Python**

-   **paho-mqtt**: A library for MQTT communication in Python.
-   **influxdb-client**: Used for writing data to the InfluxDB database.
-   **Whisper**: An AI model for speech recognition and audio-to-text conversion.

----------

## **⚙️ System Requirements**

-   **Docker Engine** and **Docker Compose**: Required for running InfluxDB and Grafana containers.
-   **Python 3.8** or later: Needed to run Python scripts and communicate with the MQTT broker.
-   **Arduino IDE**: For managing the ESP8266 microcontroller.

----------

## **🔧 System Workflow**

1.  **ESP8266 microcontroller** collects data from the DS18B20 sensor.
2.  **MQTT Broker** transmits temperature data to the application.
3.  **Whisper AI model** processes speech into text and sends the result to the MQTT broker.
4.  **Python** stores data in the **InfluxDB** database.
5.  **Grafana** visualizes the data on charts, showing temperature changes in real-time.

----------

### **Summary**

The project enables efficient data collection and processing using modern IoT and artificial intelligence technologies. By leveraging MQTT, Docker, Python, and Whisper AI, the entire system is scalable, flexible, and secure.

----------

### **Authors**  
Piotr Dratwa & Jakub Kaczmarzewski

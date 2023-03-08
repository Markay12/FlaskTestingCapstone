# Playback and Web Request using Flask and ASP.NET

Currently working on converting from using Flask to ASP.NET

## Table of Contents

1. [Flask]()
2. [test.py - Flask Version]()


---

# Flask

## test.py - Flask Version

The test.py file contains a simple Flask web application that handles HTTP requests for controlling media playback.

The application provides three endpoints:

1. `/` - the main page, returns a greeting message.

2. `/<name>` - a dynamic endpoint that takes a name parameter and returns a personalized greeting message.

3. `/Playback/clientPBState` - accepts a PUT request that takes a byte array as data, unpacks it using struct and returns the same byte array as response.

4. `/Playback/seek` - accepts a PUT request that takes a byte array as data, unpacks it using struct and returns the same byte array as response.

5. `/Playback/seekframe` - accepts a PUT request that takes a JSON object as data, unpacks it, prints the received data and returns a response.

The application uses the Flask framework and the struct module to encode and decode binary data. To run the application, simply execute the test.py file using Python. By default, the application runs on port 5001.


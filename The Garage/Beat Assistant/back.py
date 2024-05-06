from pythonosc import udp_client
import time

# Set up OSC client to communicate with Sonic Pi
client = udp_client.SimpleUDPClient("127.0.0.1", 4560)  # Change IP and port if needed

# Your machine learning code goes here
# For demonstration purposes, let's send some dummy data to Sonic Pi
for i in range(10):
    # Example: Sending a message with a value from the ML model
    ml_output = i * 0.1  # Dummy output from ML model
    client.send_message("/ml_output", ml_output)
    time.sleep(1)  # Simulate some processing time

print("Finished sending messages to Sonic Pi.")

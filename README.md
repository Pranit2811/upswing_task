# upswing_task


Prerequisites
    Docker installed on your machine.


Setup and Usage

Follow these instructions to build and run the Docker container:

1. Clone the Repository
    
    https://github.com/Pranit2811/upswing_task.git
    cd upswing_task
    
2. Build the Docker Image
   
3. Run the Docker container 

4. use below curl request for get count of each status during the specified time range.
    
    curl --location 'http://127.0.0.1:8000/status?start_date=2024-07-06%2003%3A23%3A00&end_date=2024-07-07%2003%3A26%3A00'

    Note. Change the Query params as per your requirement.


Directory Structure:
    /src
├── main.py
├── requirements.txt
└── /scripts
    ├── producer.py
    └── consumer.py

Running the Application Without Docker

1. Navigate to the Project Directory
    cd upswing_task


2. Run the Producer Script
    Navigate to the src/script folder.
    Execute the producer.py script to send messages to the queue.

3. Run the Consumer Script
    In the same src/script folder, execute the consumer.py script to consume messages from the queue.

4. Start the FastAPI Server
    Use the following command to run the FastAPI server:
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

By following these steps, you will be able to run the producer and consumer scripts as well as the FastAPI server without using Docker.
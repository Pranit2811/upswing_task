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

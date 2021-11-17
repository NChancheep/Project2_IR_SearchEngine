# Project2 Prototype IR system
## Member
Kittitad Jiraprasitchai 6288073
Chancheep Mahacharoensuk 6288092
Kantapong Matangkarat 6288160

The component that you need to use
1. Elasticsearch
2. Kibana
3. Flask
4. anime-bulk.json


How to run the program
1. First you need to run elasticsearch.bat in the bin folder of elasticsearch. (http://127.0.0.1:9200/)
2. After that you need to run kibana.bat in the other Cmd. (http://127.0.0.1:5601/app/home#/) 
3. After run this 2 program you will go to the kibana (http://127.0.0.1:5601/app/home#/) and import the anime-bulk.json (it on the json folder)
4. Set the index of anime-bulk.json to "anime_index"
5. Go to the "search_engine" folder and run the command 'flask run' on the anaconda prompt.
PS: If you encounter with the error you must install the environment by type this command.
    1. 'pip install Flask'
    2. 'set FLASK_APP=search_app.py'
    3. 'set FLASK_APP=development'
    4. 'flask run'
6. After running the flask it will show the link http://127.0.0.1:5000/
7. Enjoy!!!!

PS: This project is not for commercial use.

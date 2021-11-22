# Project2 Prototype IR system
## Member
Kittitad Jiraprasitchai 6288073<br>
Chancheep Mahacharoensuk 6288092<br>
Kantapong Matangkarat 6288160<br>

The component that you need to use<br>
1. Elasticsearch<br>
2. Kibana<br>
3. Flask<br>
4. anime-bulk.json<br>

<br>
How to run the program<br>
install these 2 first on the terminal
pip install elasticsearch
pip install ndjson

1. First you need to run elasticsearch.bat in the bin folder of elasticsearch. (http://127.0.0.1:9200/)<br>
2. After that you need to run kibana.bat in the other Cmd. (http://127.0.0.1:5601/app/home#/) <br>
3. After run this 2 program you will go to the kibana (http://127.0.0.1:5601/app/home#/) and import the anime-bulk.json (it on the json folder)<br>
4. Set the index of anime-bulk.json to "anime_index"<br>
5. Go to the "search_engine" folder and run the command 'flask run' on the anaconda prompt.<br>
PS: If you encounter with the error you must install the environment by type this command.<br>
    1. 'pip install Flask'<br>
    2. 'set FLASK_APP=search_app.py'<br>
    3. 'set FLASK_ENV=development'<br>
    4. 'flask run'<br>
6. After running the flask it will show the link http://127.0.0.1:5000/<br>
7. Enjoy!!!!<br>
<br>
PS: This project is not for commercial use.

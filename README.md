# ggmap-crawler-v1.1
# How to run :
1. Create virtual environment <br>
``` virtualenv -p $(which python3) env ```
2. Get into your environment, if you want to get out, please code line 2<br>
``` source env/bin/activate ``` 
``` deactivate ``` 
3. Install all packages in environment <br>
``` pip3 install -r requirements.txt ```
4. Set up variable of env and you should config in .env to run more exactly.<br>
``` cp .env.example .env ```
5. Edit db name at config.py => testing <br>
``` MONGODB_DB = 'foody_1'``` <br>
``` MONGODB_HOST = 'mongodb://localhost:27017/foody_1'``` 
6. Access into features -> foody.feature and run by ide pycharm
- Note: you can run each scenario and if you don't run, you can (Ctr + /) them.



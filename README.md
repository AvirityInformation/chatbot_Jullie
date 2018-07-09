## License

These codes are licensed under CC0.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

<br/>
<br/>
<br/>

# Instruction
#### 1.Make an app on Heroku


#### 2.Make a facebook page and get page access token and verify token from facebook developer page. (Replace xxx with app name and ooo with keys or tokens)
Set these tokens as heroku env var.
1. page_aceess_token
2. verify_token   

heroku config:set PAGE_ACCESS_TOKEN=ooo -a xxx    
heroku config:set VERIFY_TOKEN=ooo -a xxx

#### 3.Set jvm buildback to use stanford parser

heroku buildpacks:add heroku/jvm -a xxx  

#### 4.Then create an agent on https://dialogflow.com and set its api keys to heroku env vars.    
heroku config:set client_access_token=ooo -a xxx    
heroku config:set session_id=ooo -a xxx  

#### 5.set database and queue
heroku addons:create heroku-postgresql:hobby-dev -a xxx  
heroku addons:create redistogo:nano -a xxx

##### 6.check secret keys
Set 
1. database_url
2. redistogo_url

to heroku env variables.      

##### 7.Prepare database.
**install psql with pip if first time**  
pip install psql

**on new db, execute following commands**  
heroku pg:psql -a xxx

#### 8.Run the app
On your console, execute following commands  
**python worker.py**  
**python clock.py**  
**python app.py**
## License

These codes are licensed under CC0.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

<br/>
<br/>
<br/>

# About Jullie  
Jullie is a pattern-based chatbot that is built to give psychotherapy called Client Centered Therapy(or Rogerian Therapy).  
Jullie replies to users with compassion.

# How the system works  
1. User send message to Jullie facebook page account in Messenger app.
2. Message will be sent to webhook(endpoint of heroku app) via facebook api.
3. At endpoint of heroku that is described in app.py, the message will be saved to database 'messages' table.
4. Chatbot will wait for 20 seconds to reply after user's last message so that users can finish sending all what they want to say.
5. In message_observer.py, fetch_regularly() method finds messages sent more than 20 seconds ago and put them into queue with main() method in main.py
6. worker.py is listening to the queue so when task is in the queue, worker will execute main() function.
7. In the main() function, instances of Message, User and TherapySession class will be created and BotFactory create a bot that handle those instances to generate responses to user.
8. After creating responses, bot sends them to user via facebook api. 


# Instruction
(xxx is the name of the heroku app you create so please replace it before executing commands.)
#### 1. Make an app on Heroku
Make an app on Heroku.

Run this command in terminal(Don't forget to install heroku CLI)

heroku buildpacks:add heroku/python -a xxx  
heroku buildpacks:add heroku/jvm -a xxx  
heroku config:set VERIFY_TOKEN=ooo -a xxx  
(ooo can be any string you want)

Go to section "Deploy" and push the code to run the server.

Go to "Resources" pane and add "Heroku Postgres" in Add ons.


#### 2. Make a facebook page from facebook.
#### 3. Setting on Facebook Developer Page 
Go to facebook developer page and create your account.

https://developers.facebook.com/

Create an app there and go to its dashboard.

From "Product" section, find "Messenger" pane.

Create an page access token by selecting facebook page you created in step 2.  
Then you will get a page access token.  
Then run this code to set it as a heroku env variable.  
heroku config:set PAGE_ACCESS_TOKEN=ooo -a xxx    

From the "Webhook" section in "Messenger" pane, click on "Setup webhook" from "Messenger" section.   
Then you will see a window requiring 2 values.
"callback url": This is a url of your heroku app.    
"verify token": This is the string you set in the step 1 as "VERIFY_TOKEN". 
Also check the 'messaging', 'messaging_postback' boxes.  

After that, you have to follow the facebook page by selecting the page there.  


#### 4.Then create an agent on https://dialogflow.com and set its api keys as heroku env vars.    
Go to dialogflow console.  
Add prebuild agent 'Small Talk' from left menu "Prebuilt Agents".  
Select "Create a new Google project" when adding an agent.    

Click on the setting icon of the agent and get client access token.

Then execute following command to set it to heroku env variables.  
heroku config:set client_access_token=ooo -a xxx  
heroku config:set session_id=### -a xxx  
(Replace ### with any string)    

#### 5. set queue  
heroku addons:create redistogo:nano -a xxx  
(You'll need to verify the account to install addons)      

#### 6. Setup database
Execute this command to connect with db.  
heroku pg:psql -a xxx  

Copy the content of db/first_create.ddl and paste it in the console.  
Tables are now created.  

#### 7. Send message to your facebook page and get response!
Don't forget to start three dynos to run all the programs required.
web, worker and clock   

You can start servers from your heroku app dashboard "Resources" pane.

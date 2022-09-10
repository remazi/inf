from flask import Flask,request
import random,requests
app = Flask('app')
@app.route('/info/')
def hello_world():
    user = request.args.get("user")
    print(user)
    hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
  }
    rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()['data']['user']
    try:
        name=rer['full_name']
        fols=rer['edge_followed_by']['count']
        folg=rer['edge_follow']['count']
        id=rer['id']
        priv=rer['is_private']
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
        ree = re.json()
        dat = ree['data']
        posts=rer['edge_owner_to_timeline_media']['count']
        bio=rer['biography']
        return {"user":{"info":{"user":user, "name":name, "followers":fols, "following":folg, "id":id, "private":priv, "data":dat, "posts":posts, "bio":bio}}}
    except:
      return {"status":"False"}
app.run(host='0.0.0.0', port=6918)
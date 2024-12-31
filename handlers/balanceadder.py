import quart
import ngrok
import os
import requests

from utils.shortlinkcreator import ShortLinkCreator


slink = ShortLinkCreator()

app = quart.Quart(__name__)
@app.route(f'/{os.getenv("path_shortlink")}/<random_code>', methods=['GET'])
def checkshortlink(random_code):
    #print(random_code)
    reward = slink.completeshortlink(random_code)
    
    return reward

async def runapp():
    ngrok.set_auth_token(os.getenv("ngrok_token"))
    listener = await ngrok.forward(5000,hostname=os.getenv("ngrok_url"))
    print(listener.url())
    await app.run_task(host='0.0.0.0',port=5000)


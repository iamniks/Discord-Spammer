import time
import requests
import json
import random
import discum
import string

token = ""

bot = discum.Client(token=token)

def joinServer(token, invite):

    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "cookie": "__dcfduid=7f97c3001dd311ecb8d2c794e9dd21ac; __sdcfduid=7f97c3011dd311ecb8d2c794e9dd21ac88a85b9a1e86ce25f6972a0cfb5c2c77f7adccad0e3b5f5ef717ddf28ce03f63; _gcl_au=1.1.975698987.1632555477; _ga=GA1.2.1867591022.1632555477; _gid=GA1.2.99719911.1633679246; __stripe_mid=bec00e2a-d3dc-45af-a536-8d972f204f9957a585; locale=ko; __cfruid=18f4a135814660d2721447e960e538c913a44e92-1633750333; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+09+2021+15%3A25%3A30+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImtvLUtSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi43MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMC40NjA2LjcxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzYm9hcmQub3JnLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2JvYXJkLm9yZyIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMDgwNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    r = requests.post(f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true", headers= headers)

    if r.status_code == 200:
        name = json.loads(r.text).get("guild").get("name")
        print(json.loads(r.text))
        print(f"{name} 서버에 가입을 성공 했습니다")
        return json.loads(r.text).get("guild").get("id")
    else:
        print(f"[{r.status_code}] {r.text}")

def LeaveServer(token, guild_id):

    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "cookie": "__dcfduid=7f97c3001dd311ecb8d2c794e9dd21ac; __sdcfduid=7f97c3011dd311ecb8d2c794e9dd21ac88a85b9a1e86ce25f6972a0cfb5c2c77f7adccad0e3b5f5ef717ddf28ce03f63; _gcl_au=1.1.975698987.1632555477; _ga=GA1.2.1867591022.1632555477; _gid=GA1.2.99719911.1633679246; __stripe_mid=bec00e2a-d3dc-45af-a536-8d972f204f9957a585; locale=ko; __cfruid=18f4a135814660d2721447e960e538c913a44e92-1633750333; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+09+2021+15%3A25%3A30+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImtvLUtSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi43MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMC40NjA2LjcxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzYm9hcmQub3JnLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2JvYXJkLm9yZyIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMDgwNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers, json={"lurking": "false"})

def sendDM(token, content, userid):
    global id
    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "cookie": "__dcfduid=7f97c3001dd311ecb8d2c794e9dd21ac; __sdcfduid=7f97c3011dd311ecb8d2c794e9dd21ac88a85b9a1e86ce25f6972a0cfb5c2c77f7adccad0e3b5f5ef717ddf28ce03f63; _gcl_au=1.1.975698987.1632555477; _ga=GA1.2.1867591022.1632555477; _gid=GA1.2.99719911.1633679246; __stripe_mid=bec00e2a-d3dc-45af-a536-8d972f204f9957a585; locale=ko; __cfruid=18f4a135814660d2721447e960e538c913a44e92-1633750333; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+09+2021+16%3A27%3A26+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImtvLUtSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi43MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMC40NjA2LjcxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMDgwNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    id = getRandomInt()
    sendmsgbody = {"content": f"{content}", "nonce": f"{id}", "tts": "false"}
    createDmChannelbody = {"recipients": [f"{userid}"]}

    r = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json=createDmChannelbody)

    channel = str(json.loads(r.text).get("id"))

    r1 = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, json=sendmsgbody)


def getRandomInt():
        int_pool = string.digits
        result = ""
        for i in range(8):
            result += random.choice(int_pool)

        return result    

guild = joinServer(token, "GZ7fEThuDe")

@bot.gateway.command
def memberTest(resp):
	channel_id = ''
	if resp.event.ready_supplemental:
		bot.gateway.fetchMembers(guild, channel_id) 
	if bot.gateway.finishedMemberFetching(guild):
		bot.gateway.removeCommand(memberTest)
		bot.gateway.close()

bot.gateway.run()

mention = ""
count = 0

members = bot.gateway.session.guild(guild).members
id = bot.gateway.session.user['id']

for i in range(20):
    print("\n")

count = 0
ints = 0

for mid in members:
    ints += 1
    if ints > 5:
        try:
            if not mid == id: 
                count += 1
                sendDM(token, "hi", mid)
                print(f"{mid} 에게 메시지를 보냈습니다")
        except:
            print(f"총 {count}명에게 메시지를 보냈습니다")    
            LeaveServer(token, guild)
            print("탈퇴의 성공 했습니다")
        time.sleep(3)    

print(f"총 {count}명에게 메시지를 보냈습니다") 
LeaveServer(token, guild)
print("탈퇴의 성공 했습니다")    
  

import discum
bot = discum.Client(token='')

@bot.gateway.command
def memberTest(resp):
	guild_id = '685335068675407948'
	channel_id = '846899197247619082'
	if resp.event.ready_supplemental:
		bot.gateway.fetchMembers(guild_id, channel_id) 
	if bot.gateway.finishedMemberFetching(guild_id):
		members_lenght = len(bot.gateway.session.guild(guild_id).members)
		print(str(members_lenght)+' 명의 멤버 선택됨')
		bot.gateway.removeCommand(memberTest)
		bot.gateway.close()

bot.gateway.run()

mention = ""
count = 0

for memberID in bot.gateway.session.guild('685335068675407948').members:
    if count < 30:
        mention += f"<@{memberID}>"
    else:
        mention += "\nHello"
        count = 0
        bot.sendMessage("846899197247619082", mention)
        mention = ""
    count += 1    

if count != 0:
    mention += "\nHello"
    count = 0
    bot.sendMessage("846899197247619082", mention)
    mention = ""

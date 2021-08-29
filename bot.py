import discord
from discord import colour
from discord.embeds import Embed
import datetime
import random
import asyncio
with open('token.txt') as f:
    token = f.readline()
client = discord.Client()

@client.event
async def on_ready():
    print("봇 켜짐")
    print(client.user)
    print("======")
    game = discord.Game("무야호잇!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")
    
    if message.content == "!도움":
        embed = discord.Embed(colour=discord.Colour.blue(), title = "둘리봇이라고 합니다", description="잘 부탁드려요")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        
        embed.add_field(name="!내정보", value="디스코드 가입일을 알려줍니다", inline=False)
        embed.add_field(name="!청소 <수>", value="수 만큼의 메시지를 삭제합니다", inline=False)
        embed.add_field(name="!타이머 <n초>", value="n초만큼 타이머를 작동합니다", inline=False)
        embed.add_field(name="!채널 <보낼 채널 ID> <보낼 내용>", value="보낼 채널에 메시지가 보내집니다", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널"):
        ch = client.get_channel(int(message.content[4:22]))
        await ch.send(message.content[23:])

    if message.content == "!내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000)/ 1000)
        embed = discord.Embed(colour=discord.Colour.blue(), title = f"{user.display_name}님의 정보")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="가입일", value=f"{user.display_name}의 가입일 : {date.year}/{date.month}/{date.day}", inline=False)
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!타이머"):
        time = int(message.content[5:])
        print("타이머 시작")
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="타이머를 {0}초간 작동할게요".format(time), value="이따 봐요!")
        await message.channel.send(embed=embed)
        await asyncio.sleep(time)
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="{0}초가 지났어요!".format(time), value="다음에 또 이용해주세요")
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제")
    global yes, no, voting, msgid, lit
    if message.content.startswith("!투표"):
        if voting == False:
            voting = True
            vote = message.content[4:]
            embed = discord.Embed(colour=discord.Colour.blue(), title = "투표", description="{0}".format(vote))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
            msg = await message.channel.send(embed=embed)
            msgid = msg.id
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), title = "투표 중", description="개표 후 다시 해주세요")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
            await message.channel.send(embed=embed) 
    if message.content == "!개표":
        if voting == True:
            voting = False
            embed = discord.Embed(colour=discord.Colour.blue(), title = "투표 결과")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
            embed.add_field(name="찬성", value="{0}표".format(yes), inline=True)
            embed.add_field(name="반대", value="{0}표".format(no), inline=True)
            await message.channel.send(embed=embed)
            yes -= yes
            no -= no
            lit = [866803900921282623]
            print(yes, no, lit)
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), title = "!투표를 먼저 해주세요")
            await message.channel.send(embed=embed)
voting = False
msgid = 0
yes = 0
no = 0
lit = [866803900921282623] 
@client.event
async def on_reaction_add(reaction, user):
    global yes,no,lit,msgid, lit
    if str(reaction.emoji) == "👍" and reaction.message.id == msgid:
        id = user.id
        if lit.count(id) == 1:
            print("중복")
        elif lit.count(id) == 0:
            lit.append(id)
            print(lit)
            yes += 1
            print(yes)      
    elif str(reaction.emoji) == "👎" and reaction.message.id == msgid: 
        id = user.id
        if lit.count(id) == 1:
            print("중복")
        elif lit.count(id) == 0:
            lit.append(id)
            print(lit)
            no += 1
            print(no)




client.run(token)
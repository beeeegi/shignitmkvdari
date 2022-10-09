#25.12.2020 dawyeba
#29.12.2020 gachereba
#17.08.2021 gagrdzeleba
#10.10.2021 .js-ze gadasvla
#19.02.2022 gagrdzeleba
#23.02.2022 danebeba
#27.03.2022 gagrzeleba
#20.04.2022 danebeba

import random, time, asyncio, discord, coloredlogs, logging
from discord.ext import commands
coloredlogs.install()



client = commands.Bot(command_prefix = "-",)
client.remove_command('help')
rates = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', "28", '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
size = ['8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8=========D', '8==========D', '8===========D', '8============D', '8=============D', '8==============D', '8===============D', '8================D', '8=================D', '8=================D', '8===================D', '8====================D', '8=====================D', '8======================D', '8=======================D', '8========================D', '8==========================D','8∞D']
sites = ["https://longdogechallenge.com/","http://heeeeeeeey.com/","http://corndog.io/","https://mondrianandme.com/","https://puginarug.com","https://alwaysjudgeabookbyitscover.com","https://thatsthefinger.com/","https://cant-not-tweet-this.com/","http://eelslap.com/","http://www.staggeringbeauty.com/","http://burymewithmymoney.com/","https://smashthewalls.com/","https://jacksonpollock.org/","http://endless.horse/","https://www.trypap.com/","http://www.republiquedesmangues.fr/","http://www.movenowthinklater.com/","http://www.partridgegetslucky.com/","http://www.rrrgggbbb.com/","http://beesbeesbees.com/","http://www.koalastothemax.com/","http://www.everydayim.com/","http://randomcolour.com/","http://cat-bounce.com/","http://chrismckenzie.com/","https://thezen.zone/","http://hasthelargehadroncolliderdestroyedtheworldyet.com/","http://ninjaflex.com/","http://ihasabucket.com/","http://corndogoncorndog.com/","http://www.hackertyper.com/","https://pointerpointer.com","http://imaninja.com/","http://drawing.garden/","http://www.ismycomputeron.com/","http://www.nullingthevoid.com/","http://www.muchbetterthanthis.com/","http://www.yesnoif.com/","http://lacquerlacquer.com","http://potatoortomato.com/","http://iamawesome.com/","https://strobe.cool/","http://www.pleaselike.com/","http://crouton.net/","http://corgiorgy.com/","http://www.wutdafuk.com/","http://unicodesnowmanforyou.com/","http://chillestmonkey.com/","http://scroll-o-meter.club/","http://www.crossdivisions.com/","http://tencents.info/","https://boringboringboring.com/","http://www.patience-is-a-virtue.org/","http://pixelsfighting.com/","http://isitwhite.com/","https://existentialcrisis.com/","http://onemillionlols.com/","http://www.omfgdogs.com/","http://oct82.com/","http://chihuahuaspin.com/","http://www.blankwindows.com/","http://dogs.are.the.most.moe/","http://tunnelsnakes.com/","http://www.trashloop.com/","http://www.ascii-middle-finger.com/","http://spaceis.cool/","http://www.donothingfor2minutes.com/","http://buildshruggie.com/","http://buzzybuzz.biz/","http://yeahlemons.com/","http://wowenwilsonquiz.com","https://thepigeon.org/","http://notdayoftheweek.com/","http://www.amialright.com/","http://ooooooooooooooo.com/","https://greatbignothing.com/","https://zoomquilt.org/","https://dadlaughbutton.com/","https://www.bouncingdvdlogo.com/","https://remoji.com/","http://papertoilet.com/","https://loopedforinfinity.com/",]
roasting = ['If I throw a stick, will you leave?','You’re a gray sprinkle on a rainbow cupcake.','If your brain was dynamite, there wouldn’t be enough to blow your hat off','You are more disappointing than an unsalted pretzel.','Light travels faster than sound, which is why you seemed bright until you spoke.','We were happily married for one month, but unfortunately, we’ve been married for 10 years.','Your kid is so annoying he makes his Happy Meal cry.','You have so many gaps in your teeth it looks like your tongue is in jail.','Your secrets are always safe with me. I never even listen when you tell me them.','I’ll never forget the first time we met. But I’ll keep trying.','I forgot the world revolves around you. My apologies! How silly of me.','I only take you everywhere I go just so I don’t have to kiss you goodbye.','Hold still. I’m trying to imagine you with a personality.','Our kid must have gotten his brain from you! I still have mine.','Your face makes onions cry.','The only way my husband would ever get hurt during an activity is if the TV exploded.','You look so pretty. Not at all gross today.','It’s impossible to underestimate you.','Her teeth were so bad she could eat an apple through a fence.','I’m not insulting you; I’m describing you.','I’m not a nerd; I’m just smarter than you.','Don’t be ashamed of who you are. That’s your parents’ job.','Your face is just fine, but we’ll have to put a bag over that personality.','You bring everyone so much joy… when you leave the room.','I thought of you today. It reminded me to take out the trash.','Don’t worry about me. Worry about your eyebrows.','You are the human version of period cramps.','If you’re going to be two-faced, at least make one of them pretty.','You are like a cloud. When you disappear, it’s a beautiful day.','I’d rather treat my baby’s diaper rash than have lunch with you.','Don’t worry — the first 40 years of childhood are always the hardest.','I may love to shop, but I will never buy your bull.','I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?','OH MY GOD! IT SPEAKS!','Is your ass jealous of the amount of shit that comes out of your mouth?','Go back to Party City, where you belong!','Where’d you get your outfits, girl, American Apparently Not?','Impersonating Beyonce is not your destiny, child.','Don’t get bitter, just get better.','Child, I’ve forgotten more than you ever knew.','You just might be why the middle finger was invented in the first place.','I know you are, but what am I?','I see no evil, and I definitely don’t hear your evil.','Someday you’ll go far… and I really hope you stay there.','Oh, I’m sorry. Did the middle of my sentence interrupt the beginning of yours?','You bring everyone so much joy! You know, when you leave the room. But, still.','Oops, my bad. I could’ve sworn I was dealing with an adult.','Did I invite you to the barbecue? Then why are you all up in my grill?','I’m an acquired taste. If you don’t like me, acquire some taste.','Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.',' Yeah? Well, you smell like hot dog water.','That sounds like a you problem.','Beauty is only skin deep, but ugly goes clean to the bone.','Oh, you don’t like being treated the way you treat me? That must suck.','I’ve been called worse things by better men.','Well, the jerk store called. They’re running out of you.']

start_time = time.time()

#გაჩვენებს კონსოლში რო ბოტი მზადაა
@client.event
async def on_ready():
        print('#')
        print(f'#                         Logged in as {client.user} (ID: {client.user.id})')
        print('#')
        print(f'#                         Working on {len(client.guilds)} servers!')
        print('#\n\n')
        await client.change_presence(status = discord.Status.online, activity = discord.Game("-help"))
        
        #kai xalxi channel
        channel_id1 = 1017852391388876901
        voice_channel1 = client.get_channel(channel_id1)
        await voice_channel1.connect()

#დახმარების ბრძანება
@client.command(aliases = ['hlep', 'h'])
async def help(ctx):
            await ctx.send(
"""
```diff
-პრეფიქსი- ==> -
``````apache
help = ბოტის ყველა ბრძანება
ping = პინგი
website = გაჩვენებს რანდომ გამოუსადეგარ ვებსაიტებს
invite = ბოტის invite ლინკი რომლითაც შეგიძლიათ მოიწვიოთ ბოტი თქვენს სერვერზე, უბრალოდ დააკოპირეთ და ნებისმიერ channel-ში ჩასვით ლინკი, შემდეგ კი დააჭირეთ მას.
credits = ინფორმაცია შემქნმნელზე\n
8ball "კითხვა" = წინასწარმეტყველება
simp "წევრი" = განახებს რამდენი პროცენტით სიმპია ადამიანი
horny "წევრი" = განახებს რამდენი პროცენტით ჰორნია ადამიანი
gay "წევრი" = განახებს რამდენი პროცენტით გეია ადამიანი
penis "წევრი" = განახებს რამხელა აქვს მოცემულ ადამიანს ;)
shignitmkvdari "წევრი" = განახებს რამდენი პროცენტით შიგნით მკვდარია ადამიანი
sayred "ტექსტი" = წერს მითითებულ ტექსტს წითლად
spoiler "ტექსტი" = სვავს ნებისმიერ ტექსტს სპოილერში
roast "წევრი" = ამცირებს მითითებულ პიროვნებას რანდომ ინგლისური ფრაზებით {როცა არ დამეზარება ქართულიც იქნება}
waifu "წევრი" = განახებს რამდენად კარგი waifu-ა მითითებული ადამიანი
```
""")
            logging.info(f"{ctx.author} used -help")

#პინგი
@client.command()
async def ping(ctx):
    await ctx.send(f"""{ctx.author.mention}```css
პინგი: {round(client.latency * 1000)}ms```""")
    logging.info(f"{ctx.author} used -help")

#8ball (წინასწარმეტყველება)
@client.command(aliases = ["8ball", "ball8", 'eight_ball', 'eightball', '8-ball'])
async def _8ball(ctx, *, question = "None"):
     repsonses = [
"დარწმუნებული ვარ.",
"ეს ასეა ნამდვილად.",
"ეჭვგარეშე ეგრეა.",
"დიახ – აუცილებლად.",
"ზუსტად ეგრეა.",
"როგორც ვხედავ, კი.",
"სავარაუდოდ კი.",
"კარგად ჟღერს, შესაძლებელია.",
"დიახ.",
"ყველაფერი მიუთითებს კიზე.",
"პასუხი ბუნდოვანია, სცადე ისევ.",
"სხვა დროს მკითხე.",
"ჯობია ახლა არ გითხრა.",
"ახლა წინასწარმეტყველება შეუძლებელია.",
"კონცენტრირება მოახდინე და ისევ იკითხე.",
"იმედებს ნუ დაამყარებ მაგაზე.",
"ჩემი პასუხია - არა",
"ჩემი წყაროები ამბობენ არას.",
"დიდი ალბათობით - არა.",
"საეჭვოა."]
     if question == "None": 
        logging.info(f"{ctx.author} used -8ball")
        return await ctx.send(f"{ctx.author.mention} კითხვა არ გაქვს მითითებული, მაგ: `$8ball *კითხვა*`")
     await ctx.send(f"{ctx.author.mention}\n`კითხვა:` {question}\n`პასუხი:` {random.choice(repsonses)}")
     logging.info(f"{ctx.author} used -8ball")


#simp rate
@client.command()
async def simp(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -simp")
        await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$simp @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"saurnoli ar aris simpi")
          logging.info(f"{ctx.author} used -simp")
     elif member == "<@859866420887289877>":
          await ctx.send(f"saurnoli ar aris simpi")
          logging.info(f"{ctx.author} used -simp")
     else:
          await ctx.send(f"{member} არის {random.choice(rates)}%-ით simp-ი!")
          logging.info(f"{ctx.author} used -simp")

#horny rate
@client.command()
async def horny(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -horny")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$horny @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"lol es rato")
          logging.info(f"{ctx.author} used -horny")
     elif member == "<@859866420887289877>":
          await ctx.send(f"lol es rato")
          logging.info(f"{ctx.author} used -horny")
     else:
          await ctx.send(f"{member} არის {random.choice(rates)}%-ით horny-ი!")
          logging.info(f"{ctx.author} used -horny")

#gay rate
@client.command()
async def gay(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -gay")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$gay @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"gay shen xar")
          logging.info(f"{ctx.author} used -gay")
     elif member == "<@859866420887289877>":
          await ctx.send(f"gay shen xar")
          logging.info(f"{ctx.author} used -gay")
     else:
          await ctx.send(f"{member} არის {random.choice(rates)}%-ით gay-ი!")
          logging.info(f"{ctx.author} used -gay")

#waifu rate
@client.command()
async def waifu(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -waifu")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$waifu @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"sauroni magari waifua")
          logging.info(f"{ctx.author} used -waifu")
     elif member == "<@859866420887289877>":
          await ctx.send(f"sauroni magari waifua")
          logging.info(f"{ctx.author} used -waifu")
     else:
          await ctx.send(f"{member} არის {random.choice(rates)}/100 waifu!")
          logging.info(f"{ctx.author} used -waifu")

#shignitmkvdari rate
@client.command()
async def shignitmkvdari(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -shignitmkvdari")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$shignitmkvdari @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"jgufis shemqmneli datage tu momechvena")
          logging.info(f"{ctx.author} used -shignitmkvdari")
     elif member == "<@859866420887289877>":
          await ctx.send(f"jgufis shemqmneli datage tu momechvena")
          logging.info(f"{ctx.author} used -shignitmkvdari")
     else:
          await ctx.send(f"{member} არის {random.choice(rates)}%-ით shignitmkvdari-ი!")
          logging.info(f"{ctx.author} used -shignitmkvdari")

#penis size
@client.command()
async def penis(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -penis")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$penis @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"rato gainteresebs...")
          logging.info(f"{ctx.author} used -penis")
     elif member == "<@859866420887289877>":
          await ctx.send(f"rato gainteresebs...")
          logging.info(f"{ctx.author} used -penis")
     else:
          await ctx.send(f"{member}'s penis size\n**{random.choice(size)}** :smirk:")
          logging.info(f"{ctx.author} used -penis")

#roasting
@client.command()
async def roast(ctx, member = 'None'):
     if member == "None": 
        logging.info(f"{ctx.author} used -roast")
        return await ctx.send(f"{ctx.author.mention}, მონიშნე ვინმე, მაგ: `$roast @_saur0n#0666`")
     elif member == "<@!859866420887289877>":
          await ctx.send(f"ჩემი შემქმნელის დამცირება გინდა ჩემივე გამოყენებით? bro, thats kinda cringe")
          logging.info(f"{ctx.author} used -roast")
     elif member == "<@859866420887289877>":
          await ctx.send(f"ჩემი შემქმნელის დამცირება გინდა ჩემივე გამოყენებით? bro, thats kinda cringe")
          logging.info(f"{ctx.author} used -roast")
     else:
          await ctx.send(f"{member}, {random.choice(roasting)}")
          logging.info(f"{ctx.author} used -roast")

#წითლად წერს მითითებულ ტექსტს
@client.command()
async def sayred(ctx, *, message = 'None'):
     if message == "None":
        logging.info(f"{ctx.author} used -sayred")
        return await ctx.send(f"{ctx.author.mention}, დაწერე მესიჯი, მაგალითი: `$sayred რა მაგარი ბოტია`")
     elif "`" in message:
          logging.info(f"{ctx.author} used -sayred")
          return await ctx.send(f"{ctx.author.mention}, **dets illegal bro...** :face_in_clouds:")
     else:
          await ctx.message.delete()
          await ctx.send(
f"""
```diff
-{message}
```
"""
)
     logging.info(f"{ctx.author} used -sayred")

#ასპოილერებს მესიჯს
@client.command()
async def spoiler(ctx, *, message = 'None'):
     if message == "None":
        logging.info(f"{ctx.author} used -spoiler")
        return await ctx.send(f"{ctx.author.mention}, დაწერე მესიჯი, მაგალითი: `$spoiler რა მაგარი ბოტია`")
     await ctx.message.delete()
     await ctx.send('||' + message + '||')
     logging.info(f"{ctx.author} used -spoiler")

#random websites
@client.command()
async def website(ctx):
     await ctx.send(f"{ctx.author.mention} შენი გამოუსადეგარი ვებსაიტი:\n{random.choice(sites)}")
     logging.info(f"{ctx.author} used -website")

#invite
@client.command(aliases = ["inv"])
async def invite(ctx):
     link = "https://discord.com/api/oauth2/authorize?client_id=1017822246057812128&permissions=274914995264&scope=bot"
     await ctx.send(f"**მოიწვიე ჩემი ბოტი შენს დისქორდ სერვერზე და გააფართოვე შენი სერვერის შესაძლებლობები:**\n\n{link}")
     logging.info(f"{ctx.author} used -invite")

#credits
@client.command()
async def credits(ctx):
     bday = "25.12.2020 - ბოტის დაბადების დღე"

     embed = discord.Embed(title="ინფორმაცია დეველოპერზე", description="შენიშვნები/ხარვეზები/პრობლემები, ყველაფერზე ვწერთ მას.", color=0xffffff)
     embed.add_field(name="Facebook", value="https://www.facebook.com/sauron.gamanadgurebeli/", inline=False)
     embed.add_field(name="Instagram", value="https://www.instagram.com/saur0nnn/", inline=False)
     embed.add_field(name="Discord", value="Begi#0687", inline=False)
     embed.add_field(name="YouTube", value="https://www.youtube.com/channel/UC0QdWCuaUMyHXZqFdkDr0EQ", inline=False)
     embed.add_field(name="Steam", value="https://steamcommunity.com/id/saur0nn/", inline=False)
     embed.set_footer(text = bday)
     await ctx.send(embed=embed)
     logging.info(f"{ctx.author} used -credits")






























###########################################################################################################################################################################################
#                                                                                    MUSIC                                                                                                #
###########################################################################################################################################################################################




























































































































































































































































































#კითხულობს ბოტის ტოკენს და რთავს მას
client.run('sssss')

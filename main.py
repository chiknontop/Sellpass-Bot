import discord

from discord.ext import commands
from sellpass import SellPass

token = "bot_token_here"
prefix = "bot_prefix_here"
api_key = "api_key_here"

intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents=intents)

if __name__ == "__main__":
    sp = SellPass(
        api_key = api_key,
        debug = True,
        shop_id = 3501
        )

@client.event
async def on_ready():
    print("Sellpass+ Bot Is Online Fucker")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Sellpass+ Forgotten"))

#dumbass discord error stuff #FRICKDISCORD
@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(f"**ERROR!** \n```API LOG: \nYou do not have permission to use this command!```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"**ERROR!** \n```API LOG: \nMissing Arguments: {error}```")

#annoucement-commands
@client.command()
async def getannouncements(ctx):
    response = sp.get_announcements()
    await ctx.send(f"**Succesfully Fetched Announcements** \n```API LOG: \n{response}```")

@client.command()
async def createannouncement(ctx, title, shortdesc, desc, buttontext, buttonlink):
    response = sp.create_announcement(
        title = title,
        short_description = shortdesc,
        description = desc,
        unlisted = False,
        private = False,
        button_text = buttontext,
        button_link = buttonlink
    )
    await ctx.send(f"**Announcement Succesfully Created** \n```API LOG: \n{response}```")

@client.command()
async def editannouncement(ctx, id, title, shortdesc, desc, buttontext, buttonlink):
    response = sp.edit_announcement(
        announcement_id = id,
        title = title,
        short_description = shortdesc,
        description = desc,
        unlisted = False,
        private = False,
        button_text = buttontext,
        button_link = buttonlink
    )
    await ctx.send(f"**Announcement Succesfully Edited** \n```API LOG: \n{response}```")
    

@client.command()
async def deleteannouncement(ctx, id):
    response = sp.delete_announcement(
        announcement_id = id
    )
    await ctx.send(f"**Announcement Succesfully Deleted** \n```API LOG: \n{response}```")


#blacklist-commands
@client.command()
async def getblacklists(ctx):
    response = sp.get_blacklist()
    await ctx.send(f"**Succesfully Fetched Blacklists** \n```API LOG: \n{response}```")

@client.command()
async def blacklistinfo(ctx, id):
    response = sp.get_blocked_item(
        blocked_id = id
    )
    await ctx.send(f"**Succesfully Fetched Blacklist Info** \n```API LOG: \n{response}```")

@client.command()
async def deleteblacklist(ctx, id):
    response = sp.get_blocked_item(
        delete_blocked_item = id
    )
    await ctx.send(f"**Succesfully Deleted Blacklist** \n```API LOG: \n{response}```")
    

#customer-commands
@client.command()
async def getcustomers(ctx):
    response = sp.get_customers()
    await ctx.send(f"**Succesfully Fetched Customers** \n```API LOG: \n{response}```")

@client.command()
async def customerinfo(ctx, id):
    response = sp.get_customer()
    await ctx.send(f"**Succesfully Fetched Customer Info** \n```API LOG: \n{response}```")

@client.command()
async def customerisp(ctx, id):
    response = sp.get_customer_ips(
        customer_id = id
    )
    await ctx.send(f"**Succesfully Fetched Customer IPS** \n```API LOG: \n{response}```")


#faq-commands
@client.command()
async def getfaqs(ctx):
    response = sp.get_faqs()
    await ctx.send(f"**Succesfully Fetched FAQ's** \n```API LOG: \n{response}```")


@client.command()
async def createfaq(ctx, quest, ans):
    response = sp.create_faq(
        question = quest,
        answer = ans,
    )
    await ctx.send(f"**Succesfully Created FAQ** \n```API LOG: \n{response}```")

@client.command()
async def editfaq(ctx, quest, ans):
    response = sp.edit_faq(
        question = quest,
        answer = ans,
    )
    await ctx.send(f"**Succesfully Edited FAQ** \n```API LOG: \n{response}```")

@client.command()
async def deletefaq(ctx, id):
    response = sp.delete_faq(
        faq_id = id
    )
    await ctx.send(f"**Succesfully Deleted FAQ** \n```API LOG: \n{response}```")


#feedback-commands
@client.command()
async def getfeedback(ctx):
    response = sp.get_feedback()
    await ctx.send(f"**Succesfully Fetched Feedback** \n```API LOG: \n{response}```")

@client.command()
async def feedbackinfo(ctx, id):
    response = sp.get_feedback_item(
        feedback_id = id
    )
    await ctx.send(f"**Succesfully Fetched Feedback Info** \n```API LOG: \n{response}```")

@client.command()
async def replyfeedback(ctx, id, reply):
    response = sp.answer_feedback_item(
        feedback_id = id,
        answer = reply
    )
    await ctx.send(f"**Succesfully Replied To Feedback** \n```API LOG: \n{response}```")

@client.command()
async def appealfeedback(ctx, id, reason, desc):
    response = sp.appeal_feedback_item(
        feedback_id = id,
        reason = reason,
        description = desc
    )
    await ctx.send(f"**Succesfully Appealed Feedback** \n```API LOG: \n{response}```")



#other-commands
@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000, 1)
    await ctx.send(f"**Sellpass+** \n```{latency}ms```")

client.run(token)
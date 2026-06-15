import os  # Make sure this is at the very top of your bot.py file!
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)

# ⚙️ CONFIGURATION 
YOUR_DISCORD_USER_ID = 1297533282740600920  # 👈 Make sure your actual numerical ID is here
CLAN_ID = "BH5HGJHV" 
PRIVATE_SERVER_LINK = "https://www.roblox.com/share?code=e2bbdedd5de37e499f195764ae28d2ab&type=Server"

@bot.event
async def on_ready():
    print(f"🤖 Success! {bot.user.name} is online and armed with the secure DM system.")

# 🔒 SECURE PRIVATE SERVER COMMAND
@bot.command(name="sendps")
async def send_private_server(ctx, target_user: discord.Member = None):
    if ctx.author.id != YOUR_DISCORD_USER_ID:
        await ctx.reply("❌ You do not have permission to distribute the private server link.")
        return

    if target_user is None:
        await ctx.reply("⚠️ Please mention the user you want to send the link to! Example: `!sendps @username`")
        return

    try:
        dm_content = (
            f"👋 Hey {target_user.name}!\n\n"
            f"Welcome to the clan! Here is the secure **Private Server Link**:\n"
            f"{PRIVATE_SERVER_LINK}\n\n"
            f"*Please do not leak or share this link with anyone else. Boosting the private server is appreciated! :D*"
        )
        await target_user.send(dm_content)
        await ctx.reply(f"✅ Successfully sent the private server link to {target_user.mention}'s DMs!")
        
    except discord.Forbidden:
        await ctx.reply(f"❌ Failed to send! {target_user.mention} has their Discord Direct Messages closed. Tell them to open their DMs and try again.")
    except Exception as e:
        await ctx.reply(f"❌ An unexpected error occurred: `{e}`")

# 🔍 KEYWORD AUTO-REPLIES
# Make sure there are NO spaces at all in front of these lines:
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    user_message = message.content.lower()
    if "clan id" in user_message:
        response = f"⚔️ **Clan ID:** `{CLAN_ID}`\n👉 Make sure you type it accurately in-game to apply!"
        await message.reply(response)
        return
    await bot.process_commands(message)

# THIS LINE MUST BE FLUSH AGAINST THE LEFT WALL:
bot.run("MTUxNjE1MDA4MDQ5ODA0NTA2OQ.Gpzwh9.RAs-Xo7vEHoe_qNKEBQVr5kVS8FGYqKwo3biFY")

# Change the very last line of your file to this exact text:
bot.run(os.environ.get("MTUxNjE1MDA4MDQ5ODA0NTA2OQ.Gpzwh9.RAs-Xo7vEHoe_qNKEBQVr5kVS8FGYqKwo3biFY"))
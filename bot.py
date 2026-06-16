import os  
import discord
from discord.ext import commands
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# 🧠 FAKE WEB SERVER TO TRICK RENDER FREE TIER
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_health_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 10000))), HealthCheckHandler)
    server.serve_forever()

# Start the fake web server in the background
threading.Thread(target=run_health_server, daemon=True).start()

# --- YOUR ORIGINAL CODE STARTS HERE ---
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)

YOUR_DISCORD_USER_ID = 1297533282740600920  
CLAN_ID = "BH5HGJHV" 
PRIVATE_SERVER_LINK = "https://www.roblox.com/share?code=e4202086da54df46b6705028b8c1b2fc&type=Server"

@bot.event
async def on_ready():
    print(f"🤖 Success! {bot.user.name} is online and armed with the secure DM system.")

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

bot.run(os.environ.get("DISCORD_TOKEN"))

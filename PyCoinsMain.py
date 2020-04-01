import discord
import Commands
import json
from discord.ext import commands

bot = commands.Bot(command_prefix = "py!")

@commands.is_owner()
@bot.command()
async def logout(ctx):
    await ctx.send("Logging out...")
    await bot.logout()
    print("PyCoins logged out...")

bot.add_cog(Commands.Listener())
bot.add_cog(Commands.Commands())
print("added cogs")

with open("bal.txt", "r") as bls:
    bal = json.loads(bls.read())
with open("boost.txt", "r") as bsts:
    boost = json.loads(bsts.read())

Commands.bal = bal
Commands.boost = boost

bot.run("TOKEN")

from discord.ext import commands
import discord
import json
from Boosts import Boosts

bal = {}
boost = {}
boosts = [Boosts("If-Else", 100, 1000), \
    Boosts("For Loop", 500, 4500), \
        Boosts("For-Each Loop", 1000, 8000), \
            Boosts("Recursion", 10000, 70000)]

class Listener(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):
        print("bals", bal)
        print("boosts", boost)
        if message.author.bot:
            return
        
        print(bal.keys())
        for key in bal.keys():
            print(key)
            print(message.author.id)
            print(type(key))
            print(type(message.author.id))
            if key == str(message.author.id):
                print(True)
            else: print(False)
        print(message.author.id in bal.keys())
        if message.author.id in bal.keys():
            bal[message.author.id] = bal[message.author.id] + \
                boost[message.author.id]
            print("returning user")
        else:
            boost[message.author.id] = 5
            bal[message.author.id] = boost[message.author.id]
            print("new user")

        dump1 = json.dumps(bal)
        dump2 = json.dumps(boost)
        
        with open("boost.txt", "w") as bsts:
            bsts.write(dump2)
        
        with open("bal.txt", "w") as bls:
            bls.write(dump1)

class Commands(commands.Cog):

    @commands.command()
    async def bal(self, ctx, mentn : discord.Member = None):
        if mentn is None:
            ID = ctx.author.id
        else:
            ID = mentn.id
        try:
            balnc = bal[ID]
            bst = boost[ID]
            balembed = discord.Embed(
                title = f"{ctx.author.display_name}'s balance:",
                description = f"{balnc} PyCoins\nPyCoins per message: {bst}",
                color = discord.Color.blue()
            )
            balembed.set_thumbnail(url="https://www.enriquefvalentino.com/wp-content/uploads/2020/03/python-logo.png")
            await ctx.send(embed = balembed)
        except:
            if mentn is None:
                await ctx.send("You do not have a balance yet.")
            else:
                await ctx.send(f"{mentn.mention} does not have a balance yet.")
    
    @commands.command()
    async def store(self, ctx):
        storeinv = ""
        for bst in boosts:
            storeinv += f"{bst.get_name()}: (Boost: `{bst.get_boost()}`;" \
                f" Cost: `{bst.get_cost()}`)\n"
        
        store = discord.Embed(
            title = "PyCoins Store", 
            description = storeinv, 
            color = discord.Color.blue())
        store.set_thumbnail(url="https://www.enriquefvalentino.com/wp-content/uploads/2020/03/python-logo.png")
        await ctx.send(embed = store)

    @commands.command()
    async def buy(self, ctx, *, args):
        for bst in boosts:
            if args.lower() == bst.get_name().lower():
                if bal[ctx.author.id] >= bst.get_cost():
                    boost[ctx.author.id] += bst.get_boost()
                    bal[ctx.author.id] -= bst.get_cost()
                    await ctx.send(f"{ctx.author.mention} baught a {bst.get_name()}.")
                else:
                    await ctx.send(f"You do not have enough PyCoins to purchase a {bst.get_name()}.")
                    return
            else:
                await ctx.send(f"Sorry, there are no {args} in the store.")
                return   
import discord
from discord.ext import commands

class slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="slap")
    async def slap(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Você precisa mencionar alguém!")
            return
        await ctx.send(f"{ctx.author.mention} deu um tapa em {member.mention} ☠️")

async def setup(client):
    await client.add_cog(slap(client))

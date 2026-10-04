import discord
from discord import app_commands
from discord.ext import commands
import random

class punch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="soco", description="Dá um soco em alguém")
    @app_commands.describe(member="Quem vai levar o soco")
    async def soco(self, interaction: discord.Interaction, member: discord.Member):
        gifs = [
            "https://media.tenor.com/4x6c8v0b2nAAAAAC/anime-punch.gif",
            "https://media.tenor.com/7y9u1i3o5pAAAAAC/punch-anime.gif",
            "https://media.tenor.com/0a2s4d6f8gAAAAAC/anime-punch.gif",
        ]
        embed = discord.Embed(
            description=f"{interaction.user.mention} deu um soco em {member.mention} 👊",
            color=0xFF4500
        )
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(punch(client))

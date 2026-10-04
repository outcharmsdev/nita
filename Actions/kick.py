import discord
from discord import app_commands
from discord.ext import commands
import random

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="chute", description="Dá um chute em alguém")
    @app_commands.describe(member="Quem vai levar o chute")
    async def chute(self, interaction: discord.Interaction, member: discord.Member):
        gifs = [
            "https://media.tenor.com/7y9F3V8k5xAAAAAC/anime-kick.gif",
            "https://media.tenor.com/2x4c6v8b1nAAAAAC/kick-anime.gif",
            "https://media.tenor.com/5p7q9r2s4tAAAAAC/anime-kick.gif",
        ]
        embed = discord.Embed(
            description=f"{interaction.user.mention} deu um chute em {member.mention} 🦵",
            color=0xFFA500
        )
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(kick(client))

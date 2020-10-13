import discord
import requests
import requests_cache
from discord.ext import commands
token="redacted"
key='redacted'
url="https://api.hypixel.net/skyblock/bazaar?"
bot= commands.Bot(command_prefix ="PotatoCalc!")
@bot.command()
async def wood(ctx):
  items=["MELONS"]
  mapping={"MELONS":"melons"}
  max_price=0
  max_melon=""
  db=requests.get(f'{url}key={key}').json()['products']
  for item in items: 
      if(db[item]["sell_summary"][0]['pricePerUnit']>max_price):
        max_price=db[item]["sell_summary"][0]['pricePerUnit']
        max_melon=item
  embed=discord.Embed(title=f'The best melon is {mapping.get(max_melon)} at {max_price}',description="If something is wrong ping me. ",colour=discord.Colour.green())
  await ctx.send(embed=embed)
  
bot.run(token)

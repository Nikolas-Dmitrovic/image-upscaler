from discord.ext import commands
import requests

client = commands.Bot(command_prefix='.')

@client.command()
async def upscale(ctx, url):
    try:
        print(type(url))
        r = requests.post("https://api.deepai.org/api/waifu2x", data={'image': str(url)}, headers={'api-key': '51eeb896-1c4a-4da7-a594-f0688f9c97ae'})
        print(r.json())
        await ctx.send(r.json()['output_url'])
    except:
        await ctx.send("please input a valid image url")

# TODO put in key here
client.run()
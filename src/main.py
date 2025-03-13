from bot.bot import Bot

bot = Bot()
bot.open_new_page("https://formy-project.herokuapp.com/checkbox")

# Bot code here
print(bot.get_driver().title)
print('hello there 1')

bot.close_page()


''' 

Simple form test site:
https://formy-project.herokuapp.com/

Advanced form test site:
https://rpachallenge.com/

'''
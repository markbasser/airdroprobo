from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime
import random #ランダムモジュール忘れずに
import asyncio #なんか必要らしい

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆ワタシワエアドロップロボット‼:robot:☆Airdropの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMD（Command）も変わったりします。お楽しみに♪気長にまたコメントします:star2: \n @everyone :airplane:') 
    
    if now == '00:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('?☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \ n Very easy! I don”t know when to comment. The CMD also changes. looking forward to☆I will comment again generously. \n @everyone :airplane:')  
       
    if now == '02:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('?フフフモウイチドイイマス☆ワタシワエアドロップロボット‼:robot:☆Airdropの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMDも変わったりします。お楽しみに:star2: \n @everyone :airplane:') 
    
    if now == '02:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Say again.hehe ☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \ n Very easy! I don”t know when to comment. The CMD also changes. looking forward to☆ \n @everyone :airplane:')  
    
    if now == '02:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('キナガニキイテクダサイネ:robot: HELLO!さて、 Airdrop方法は、ダイスです:game_die:！\n 指定のコマンドで、0～100までの数字をランダムに出します。その数字によって当たりが違います。\n :airplane: Airdrop賞が【0.1.77.100番】の4/100の確立です。:star2:\n mini Drop賞が【2～76番と90～99番】です。残念が77番号を抜いた【60～89番】となっています。\n 覚えていてね:star2:！とてもほとんどが当たりです。\n BOT残高がなくなったら　お。し。ま。い。以上です。わかりましたか？適当な説明でした　:airplane::robot:')  

    if now == '02:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Please listen for a long time:robot:　HELLO! Airdrop method is dice:game_die:! The specified command will randomly output a number from 0 to 100. \n The number depends on the number. \n :airplane: The Airdrop award is the establishment of 4/100 of [0.1.77.100]:star2:. The mini Drop awards are [2-76 and 90-99]. \n Unfortunately, the number is 60-89 :star2:, which is the 77th number. Remember! \n Most of them are winning. When the BOT balance is exhausted. Then. Well. \n Yes. that"s all. Did you understand?:')

    if now == '03:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ゲームは簡単でサイコロ:game_die:振るだけ！エアドロップCommandは【!】から始まります。半角英数小文字でさて何でしょう！？【!●●】`!??` \n ヒント①：BGPTは入りません。ヒント②エアドロップですよね。ならそのスペルに関係します。以上。\n 周りに教えずにCommand打てば削除して下さいね。残高なくなれば終了する予定です。\n UzurasWalletが使える部屋と使えない部屋があります。\n　回数制限もうけてないから適度な回数でおねがいします。テキドナカイスウデ...:robot:') 
    
    if now == '03:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: The game is easy, just roll the dice:game_die:! Air Drop Command starts with [!]. What is it in half-width English letters? ? 【!●●】`!??` \n Tip ①: BGPT cannot be entered. Tip ② It"s an air drop. Is related to the spell. that"s all. \n Please delete it by typing Command without telling others. It will end when the balance is exhausted. \n Some rooms can use Uzuras Wallet and some cannot.　Since there is no limit on the number of times, please give me an appropriate number of times..... :robot:')  

    if now == '03:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: あっ！言い忘れていました！ｺﾏﾝﾄﾞは途中で変わったりします。動いている時間も不特定です。私を見つけたらｺﾏﾝﾄﾞで呼び出して下さいね☆回数制限はありませんが、連続するとボロだから..ロボでした(〃艸〃)ﾑﾌｯ止まります。ゆっくりと迷惑かからないようにお願いします。:star2:') 
    
    if now == '03:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:ah!I forgot! The command may change on the way. The time of movement is unspecified. If you find me, please call me with a command ☆ There is no limit on the number of times, but it will stop if you continue. Please do not be a nuisance slowly. I"m a bot It will break.:star2:')  
    
    if now == '10:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆ワタシハエアドロップBOT‼:robot:☆AirdropGameの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMDも変わったりします。お楽しみに:star2:') 
    
    if now == '10:56':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \ n Very easy! I don”t know when to comment. The CMD also changes. looking forward to:star2:')  
    
    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: Airdrop方法はダイスです！:game_die:\n 指定のコマンドで、0～100までの数字をランダムに出します。その数字によって当たりが違います。\n :airplane: Airdrop賞が【0.1.77.100番】の4/100の確立です。:star2:\n mini Drop賞が【2～76番と90～99番】です。残念が77番号を抜いた【60～89番】となっています。\n 覚えていてね！とてもほとんどが当たりです。\n BOT残高がなくなったら　お。し。ま。い。以上です。下手な説明わかりましたか？:star2:')  

    if now == '11:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:Airdrop method is dice game! :game_die:　\n The specified command will randomly output a number from 0 to 100. \n The number depends on the number. \n :airplane: The Airdrop award is the establishment of 4/100 of [0.1.77.100] :star2:. The mini Drop awards are [2-76 and 90-99]. \n Unfortunately, the number is 60-89, which is the 77th number. Remember! \n Most of them are winning. When the BOT balance is exhausted. Then. Well. \n Yes. that"s all. Did you understand?:star2:')

    if now == '11:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: あっ！言い忘れていました！ｺﾏﾝﾄﾞは途中で変わったりします。動いている時間も不特定です。私を見つけたらｺﾏﾝﾄﾞで呼び出して下さいね☆回数制限はありませんが、連続するとボロだから..ロボでした(〃艸〃)ﾑﾌｯ止まります。ゆっくりと迷惑かからないようにお願いします。:star2:') 
    
    if now == '11:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:ah!I forgot! The command may change on the way. The time of movement is unspecified. If you find me, please call me with a command ☆ There is no limit on the number of times, but it will stop if you continue. Please do not be a nuisance slowly. I"m a bot It will break.:star2:')  
  
    if now == '11:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ゲームは簡単でサイコロ:game_die:振るだけ！エアドロップCommandは【!】から始まります。半角英数小文字でさて何でしょう！？【!●●】`!??` \n ヒント①：BGPTは入りません。ヒント②エアドロップですよね。ならそのスペルに関係します。以上。\n 周りに教えずにCommand打てば削除して下さいね。残高なくなれば終了する予定です。\n UzurasWalletが使える部屋と使えない部屋があります。\n　回数制限もうけてないから適度な回数でおねがいします。テキドナカイスウデ...:robot:') 
    
    if now == '11:46':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: The game is easy, just roll the dice:game_die:! Air Drop Command starts with [!]. What is it in half-width English letters? ? 【!●●】`!??` \n Tip ①: BGPT cannot be entered. Tip ② It"s an air drop. Is related to the spell. that"s all. \n Please delete it by typing Command without telling others. It will end when the balance is exhausted. \n Some rooms can use Uzuras Wallet and some cannot.　Since there is no limit on the number of times, please give me an appropriate number of times.....:robot:') 


   #ループ処理実行
loop.start()



@client.event
async def on_message(message):
    """メッセージを処理"""

    if message.author.bot:  # ボットのメッセージをハネる
        return

     
    if message.content == "goodnight":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Go to bed early♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよう":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "goodevening":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん　Good evening～☆" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "hhhh":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention} ☆༺.Hello All.Everyone! Thank you!☆")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "aaaa":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんにちは☺️楽しんで！")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "kkkk":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんばんは😃🌃早く休みましょう🎵")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "b/jpxzan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info jpx")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "b/29zan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info 29coin")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "jp/jpyn":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info jpyn")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "jp/ben":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info ben")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/sprtszan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info sprts")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/kenjzan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info kenj")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/bgptzan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info bgpt")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/jpynzan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info jpyn")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "b/benzan":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/info ben")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/accept":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/accept")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/language":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/language EN")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "b/link":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/link")  # f文字列（フォーマット済み文字列リテラル）
    
   


@client.event
async def on_message(message):
    
    if message.content.startswith("!ad"):
     if client.user != message.author:
       num_random = random.randint(0, 100) #出る目を指定
       m = int(num_random)
       await message.channel.send(m)
     if 0 < m < 2: #1～1
          q = await message.channel.send(f"\n:point_right:～:game_die:  _(Dice No.**1**)_:airplane:\n:partying_face:tada: **Airdrop!** \n\n୨୧┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 2345.6789 {message.author.mention}  <:BGPT02:698471366004965406> ")
          [await q.add_reaction(i) for i in ('<:heart02:699580174911668225>', '<:BGPT02:698471366004965406>')] # for文の内包表記
          
     elif  1 < m < 29: #2～28
          q = await message.channel.send(f"\n:pinching_hand:～:game_die:  _(Dice2-29 )_ \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 11.1111 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:BGPTpink:705616860955148310>')] # for文の内包表記
          
     elif 28 < m < 30: #29
          q = await message.channel.send(f"\n:game_die::dash::leg:   _(Dice60-89)_ \n\n〓：：：：：：：：：：：：：：：：〓\n **You love Meat!DROP**:cut_of_meat: \n〓：：：：：：：：：：：：：：：：〓\n\n/tip 29coin 2929.2929 {message.author.mention}  :meat_on_bone: ")
          [await q.add_reaction(i) for i in ('<:guru:699579775500681246>', '<:kanngaeru:699072662382837881>')] # for文の内包表記
        
     elif 29 < m < 60: #30～59
          q = await message.channel.send(f"\n:point_right:～:game_die:   _(Dice30-59 )_ \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip kenj 123.456789 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:kenj:700136543003607101>')] # for文の内包表記
                           
     elif 59 < m < 77: #60～76
          await message.channel.send(f"\n:pinching_hand:～:game_die:  _(Dice60-76)_ \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7.7777 {message.author.mention}  <:BGPTpink:705616860955148310>")
          
     elif 76 < m < 78: #77～77
          q = await message.channel.send(f"\n:point_right:～:game_die:  _(Dice**77** )_ \n\n୨୧┈┈┈┈┈┈┈┈┈୨୧\n :balloon:**Jackpot!**\n\n\n:partying_face:tada: \n୨୧┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 3777.77 {message.author.mention}  <:BGPT02:698471366004965406> ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPT02:698471366004965406>')] # for文の内包表記

     elif 77 < m < 90: #78～89
          q = await message.channel.send(f"\n:game_die::dash::leg:   _(Dice60-89)_ \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n <:namida1:699577954094809088>Don't kick the dice with your foot～ \n ダイスを足で蹴ったらだめよ～!なし ")
          [await q.add_reaction(i) for i in ('<:guru:699579775500681246>', '<:kanngaeru:699072662382837881>')] # for文の内包表記

     elif 89 < m < 100: #90～99
          await message.channel.send(f"\n:point_right:～:game_die:  _(Dice90-99)_ \n\n∴‥∵‥∴‥∵‥∴‥∴‥∵‥∴\n→mini drop:candy: \n∴‥∵‥∴‥∵‥∴‥∴‥∵‥∴\n\n/tip BGPT 22.2222 {message.author.mention}  <:BGPTpink:705616860955148310>")
            
     else: #それ以外なので今回の場合100が出た時に処理される
          q = await message.channel.send(f"\n:point_right:～:game_die:  _(Dice**100**)_ \n\n୨୧┈┈┈┈┈┈┈┈┈୨୧\n:partying_face::tada: **Airdrop!** :rocket: \n୨୧┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 2345.6789 {message.author.mention}  <:BGPT02:698471366004965406> ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPT02:698471366004965406>')] # for文の内包表記



# Botの起動とDiscordサーバーへの接続
client.run(token)


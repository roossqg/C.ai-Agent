from PyCharacterAI import *
from PyCharacterAI.exceptions import SessionClosedError
import asyncio
from PyCharacterAI.types import TurnCandidate

token="YOUR TOKEN HERE"
char_id="YOUR C.AI CHARACTER ID HERE"
web_next_auth="web nex auth token (optional)"



async def main():
    client= await get_client(token=token,web_next_auth=None)

    me=await client.account.fetch_me()
    print(f"auth as : @{me.username}") #---> log in and track you



#IF YOU WANT CREATE A CHAT INSTACE

    #chat,msg=await client.chat.create_chat(char_id)
    #chat_id_now=chat.chat_id
    #print(f"{msg.author_name} : {msg.get_primary_candidate().text}")
    #print(chat.chat_id)

    

    try:
        while True:
            message=input(f"[{me.name}] : ")
            answer= await client.chat.send_message(char_id,chat_id="CHAT ID THAT YOU CREATED OR ANY WANTED FOR CHAT",message=message)
            print(f"[{answer.author_name}]: {answer.get_primary_candidate().text}")


#VOICE
            f=answer.turn_id

            cnad=list(answer.candidates.keys())
            lk=cnad[0]
                
            speech = await client.utils.generate_speech(chat_id,f,lk,voice_id="c.ai voice id")

        # It will return bytes, so we can use it for example like this:
            filepath = "voice.mp3"

            with open(filepath, 'wb') as f:
                f.write(speech)



    except SessionClosedError:
        print("session ending!")
    finally:
        await client.close_session()

asyncio.run(main())

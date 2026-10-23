import asyncio
import edge_tts

LINE = ("Imagine you are standing in room S of a huge building. Hallways lead out "
        "in every direction. How would you visit every room D F S can reach, "
        "without walking in circles? Pause, and think about it.")

VOICES = [
    "en-US-AndrewMultilingualNeural",
    "en-US-AvaMultilingualNeural",
    "en-US-BrianMultilingualNeural",
    "en-US-EmmaMultilingualNeural",
]


async def main():
    for voice in VOICES:
        name = voice.replace("en-US-", "").replace("MultilingualNeural", "")
        await edge_tts.Communicate(LINE, voice, rate="-4%").save(f"audition-{name}.mp3")
        print("wrote", name)


asyncio.run(main())

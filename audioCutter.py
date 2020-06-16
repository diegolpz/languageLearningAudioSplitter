#!/usr/bin/env python3

from pydub import AudioSegment
import sys
mp3_audio = AudioSegment.from_file("1.mp3", format="mp3")
mp3_audio = mp3_audio[(int(sys.argv[1]) * 1000):]
# file_handle = mp3_audio.export("output.mp3", format="mp3")
audioLen = len(mp3_audio)
rmsSilenceTrigger = 200
windowSize = 2000
soundBuffer = 0
j = 0
inicio =[]
fin =[]
isLastIterSilent = 0
silentCount = 0
flag1 = 0
for i, chunk in enumerate(mp3_audio):
    # if i < 3000 and i > 2000:
    #     print(i, chunk.rms)
    # if j == 0:
    if chunk.rms >= rmsSilenceTrigger and flag1 == 0:
        inicio.append(i - soundBuffer)
        flag1 = 1
        isLastIterSilent = 0
    elif chunk.rms <= rmsSilenceTrigger and flag1 == 1:
        if isLastIterSilent == 1:
            silentCount = silentCount + 1
        else:
            silentCount = 0
        if silentCount == windowSize or i == audioLen:  # the rhs of or is due to the posibility that the audio doesnt have enough silence at the end of the audio
            fin.append(i-windowSize)
            flag1 = 0
        isLastIterSilent = 1
print(inicio,len(inicio))
print(fin,len(fin))
# del inicio[0]
# del fin[0]

if len(inicio) != len(fin):
    print("not the same number of inicio and fin")
for i in range(0,len(inicio)):
    conversation = mp3_audio[inicio[i]:fin[i]]
    conversation.export("out" + str(i+1) + ".mp3", format="mp3")

import os;
import sys;
import csv;
import pinyin_jyutping_sentence;
import jieba;

jieba.set_dictionary('/home/diego/.local/lib/python3.8/site-packages/pinyin_jyutping_sentence/dict.txt.big')

myfile='in.cvs'
os.system("sed -E '/^$/d;s/ +, +/g,/;s/^ +//;s/ +$//;s/^M$//' " + sys.argv[1] + " > " + myfile)
with open('output.csv', 'w', newline='') as csvOutputFile:
    spamwriter = csv.writer(csvOutputFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open(myfile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[1] == '':
                continue
            phraseZH = ''
            phraseZS=''
            linea = ''
            i=0
            pin = pinyin_jyutping_sentence.pinyin(row[2], tone_numbers=True, spaces=True)
            PinyinZH = pinyin_jyutping_sentence.pinyin(row[2])
            tone = os.popen("sed 's/[^0-9]//g' <<< \"" + pin + '" 2>&1').read()
            tone = str(tone)
            seg_list = jieba.cut(row[4], cut_all=False)
            pin2 = pinyin_jyutping_sentence.pinyin(row[3], tone_numbers=True, spaces=True)
            PinyinZS = pinyin_jyutping_sentence.pinyin(row[3])
            tone2 = os.popen("sed 's/[^0-9]//g' <<< \"" + pin2 + '" 2>&1').read()
            tone2 = str(tone2)
            seg_list2 = jieba.cut(row[3], cut_all=False)
            audioFileZH = '[sound:GlossikaChinese' + row[0] + '.mp3]'
            audioFileZS = '[sound:GlossikaChineseZS' + row[0] + '.mp3]'
            tag = 'glossikaChinese' + str((( int(row[0]) - 1 )//50 + 1) * 50)
            baiduZH='https://fanyi.baidu.com/#zh/en/' + row[4]
            baiduZS='https://fanyi.baidu.com/#zh/en/' + row[3]
            mdbgZH='https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=' + row[4]
            mdbgZS='https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=' + row[3]
            baiduZH = '<a href="' + baiduZH + '">Baidu</a>'
            baiduZS = '<a href="' + baiduZS + '">Baidu</a>'
            mdbgZH = '<a href="' + mdbgZH + '">MBDG</a>'
            mdbgZS = '<a href="' + mdbgZS + '">MBDG</a>'

            for word in seg_list:
                for character in word:
                    if '\u4E00' <= character <=  '\u9FFF':
                        if tone[i] == '1':
                            car = '<font color="blue">' + character + '</font>'
                        if tone[i] == '2':
                            car = '<font color="green">' + character + '</font>'
                        if tone[i] == '3':
                            car = '<font color="orange">' + character + '</font>'
                        if tone[i] == '4':
                            car = '<font color="red">' + character + '</font>'
                        if tone[i] == '5':
                            car = '<font color="grey">' + character + '</font>'
                        i = i+1
                        linea = linea + car
                    else:
                        linea = linea + character
                if '\u4E00' <= word[0] <=  '\u9FFF':
                    linea = '<a href="https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=' + word + '" style="text-decoration:none;">' + linea + '</a>'
                phraseZH = phraseZH + ' ' + linea
                linea = ''
            i=0
            for word in seg_list2:
                for character in word:
                    if '\u4E00' <= character <=  '\u9FFF':
                        if tone2[i] == '1':
                            car = '<font color="blue">' + character + '</font>'
                        if tone2[i] == '2':
                            car = '<font color="green">' + character + '</font>'
                        if tone2[i] == '3':
                            car = '<font color="orange">' + character + '</font>'
                        if tone2[i] == '4':
                            car = '<font color="red">' + character + '</font>'
                        if tone2[i] == '5':
                            car = '<font color="grey">' + character + '</font>'
                        i = i+1
                        linea = linea + car
                    else:
                        linea = linea + character
                if '\u4E00' <= word[0] <=  '\u9FFF':
                    linea = '<a href="https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=' + word + '" style="text-decoration:none;">' + linea + '</a>'
                phraseZS = phraseZS + ' ' + linea
                linea = ''
            spamwriter.writerow([row[0] + '. ' + row[1],row[4],row[3],phraseZH,phraseZS,PinyinZH,PinyinZS,audioFileZH,audioFileZS,baiduZH,baiduZS,mdbgZH,mdbgZS,tag])






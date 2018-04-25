#!/usr/bin/python
# -*- coding: UTF-8 -*-


# print len(sys.argv)
# print str(sys.argv.).find(.js)


import re
import sys, getopt


def readcase(strin):
    print 'readcase'
    # print(pattern.search(strin))
    # result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', strin)
    filename=strin.replace('.spec.js','')
    fin = open(filename+'.spec.js', 'r+')
    fout = open(filename+'.txt','w')
    print fin.name,fout.name
    input=fin.read()

    # dont ask me why :D
    input = input.replace(':','###')

    # match 'sendKeys: xxx'
    #pattern_setkey_key = re.compile('\'sendKeys: [^\']+\'')
    pattern_setkey_key = re.compile('\'sendKeys## [^\']+\'')

    # match .sendKeys('xxx');    driver.sendKeys('admin');
    pattern_setkey_val = re.compile('\.sendKeys\(\'[^;]+;')

    # result1 =pattern_setkey_key.findall(input)
    # print result1

    it_key = pattern_setkey_key.finditer(input)

    # result2 =pattern_setkey_val.findall(input)
    # print result2

    it_val = pattern_setkey_val.finditer(input)

    # for match in it_key:
    #     print(match.group()),
    #     fout.write(match.group()),
    # print ""
    # fout.write("")
    #
    # for match in it_val:
    #     print(match.group()),
    #     fout.write(match.group()),
    it1 = iter(it_key)
    it2 = iter(it_val)
    while True:
        try:
            nx1=next(it1)
            print nx1.group(),':',
            # print re.search(r'[^\']+',nx1.group()).group(),':',

            nx2=next(it2)
            print re.split('[\']+',nx2.group())[1],'\n',

            fout.write(nx1.group()+': '+re.split('[\']+',nx2.group())[1]+'\n')
        except StopIteration:
            break





    return
   #  print pattern_setkey
   #  print re.findall(pattern_setkey,input)
   #  print re.compile(pattern_setkey).findall(input)
   #  #'sendKeys: admin'




    # it=re.finditer(r'^\'sendKeys: [^\']+\'+$',input)
    # for match in it:
    #     print(match.group())
    # return
def writecase(strin):
    print 'writecase'
    filename = strin.replace('.out', '')
    fin = open(filename+'.spec.js','r')
    modstr = fin.read()
    fin.close()
    fin = open(filename + '.out', 'r')
    print fin.name
    title = fin.readline().replace('###',':').replace('\'\t\'','###')
    title = title[1:-2].split('###')
    length = len(title)
    cnt = 0
    result = ''
    success = 1
    while True :
        try:
            caseline = fin.readline()[0:-1].split('\t')

            if len(caseline)<2:
                break;

            cnt=cnt+1
            print 'generate NO.',str(cnt),' case'
            # print caseline
            fout = open(filename+str(cnt)+'.spec.js','w')
            result = modstr
            for index in range(length):
                # print title[index]
                # print caseline
                result = re.sub('\.sendKeys\(\'[^;]+;','.###(\''+caseline[index]+'\');',result,1)
            fout.write(result.replace('###','sendKeys'))
        except :
            print 'failed'
            success = 0
            break



    #print re.findall(r'[^\']+',titleline)[0]


    return

def main(argv):
    specfile = ''
    pictfile = ''
    file_open_pict = ''
    try:
        opts, args = getopt.getopt(argv, "hs:p:", ["specfile=", "pictfile="])
    except getopt.GetoptError:
        print 'evolution.py -s <specfile> -p <pictfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'evolution.py -s <pictfile> -p <pictfile>'
            sys.exit()
        elif opt in ("-s", "--specfile"):
            specfile = arg
        elif opt in ("-p", "--pictfile"):
            pictfile = arg
            #file_open_pict = open(pictfile, 'w');
        else:
            print 'evolution.py -s <pictfile> -p <pictfile>'
    if (specfile != ''):
        print 'specfile name：', specfile
        readcase(specfile)

    if (pictfile != ''):
        print 'pictfile name：', pictfile
        writecase(pictfile)

if __name__ == "__main__":
    main(sys.argv[1:])

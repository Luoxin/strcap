# coding:utf-8


#NO.1
def string_add(string,little,c):
    a=[]
    count=0
    for i in string:
        if i==little:
            a.append(count)
        count+=1
    for z in a:
        string.insert(z,c)
    return string

#NO.2

def string_reverse1(string):
    return string[::-1]

def string_wordcap1(string):
    l = ""
    for i in string.split(" "):
        l+=(i.capitalize()+" ")
    return l


def string_topend_cap(a):
    def string_wordcap2(string):
        l = ""
        sgin = 0
        for i in string:
            if i == " ":
                sgin += 1
            elif sgin == 1:
                sgin -= 1
                i = i.upper();
            l += i
        return l

    a=string_wordcap1(a)
    a=string_reverse1(a)
    a=string_wordcap2(a)
    a=string_reverse1(a)
    return a

def string_end_cap(string):
    def string_delhaed(string):
        l=""
        count=0
        for i in string:
            if count==0:
                count+=1
                continue
            l+=i
        return l

    string=string_reverse1(string)
    string=string_wordcap1(string)
    string=string_reverse1(string)
    string=string_delhaed(string)
    return string

def string_top_cap(string):
    string=string_wordcap1(string)
    return string

#NO.3
def string_littlecap(string,c):
    l = ""
    for i in string:
        if i == c:
            i = i.upper();
        l += i
    return l

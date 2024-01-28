from codecs import ascii_encode
import json
ft=open("dict.json","r",encoding="utf-8")
_list=json.loads(ft.read())
__reso=[]
opedChr=[]
for i in _list:
    if len(i) == 5:
        __reso.append(i)
_list.clear()
for i in __reso:
    _list.append(i)
__reso.clear()
def _solve(i,isDelete=False,__chr='_'):
    if isDelete:
        for j in i:
            if __chr == j:
                __reso.pop(-1)
                return 
    else:
        for j in i:
            if __chr == j:
                return 
        __reso.pop(-1)
def op(isDelete=False,__chr='_'):
    if opedChr.count(__chr) !=0:
        for i in _list:
            __reso.append(i)
        print("!0")
        return 
    opedChr.append(__chr)
    for i in _list:
        __reso.append(i)
        _solve(i,isDelete=isDelete,__chr=__chr)
def check(j):
    for i in range(ord('a'),ord('z')):
        if j.count(chr(i)) > 1:
            return False
    return True
def getBestAnswer():
    for j in _list:
        if check(j):
            return j
    return _list[0]    
        
def fflush():
    ft=open("dict.json","r",encoding="utf-8")
    _list=json.loads(ft.read())
    __reso=[]
    opedChr=[]
    for i in _list:
        if len(i) == 5:
            __reso.append(i)
    _list.clear()
    for i in __reso:
        _list.append(i)
    __reso.clear()  

def solve(word,_result):
    pos=0
    for _ in _result:
        print(len(__reso),"left")
        __reso.clear()
        k=int(_)
        if k==0:
            op(isDelete=True,__chr=word[pos])
        elif k==1:
            for i in _list:
                if i[pos] == word[pos]:
                    __reso.append(i)
        elif k==2:
            op(isDelete=False,__chr=word[pos])
            _list.clear()
            for i in __reso:
                _list.append(i)
            __reso.clear()
            for i in _list:
                if i[pos] != word[pos]:
                    __reso.append(i)
        _list.clear()
        for i in __reso:
            _list.append(i)
        pos+=1
    return 

# for _ in range(1,5):
#     print(len(__reso),"left")
#     __reso.clear()
#     if len(_list) <= 100 :
#         for _ in _list:
#             print(_)
#     _id=int(input())
#     if _id == 0 :
#         _chr=input()
#         op(isDelete=True,__chr=_chr)
#     elif _id == 1 :
#         _chr=input()
#         _pos=int(input())
#         for i in _list:
#             if i[_pos-1] == _chr:
#                 __reso.append(i)
#     elif _id == 2:
#         _chr=input()
#         _pos=int(input())
#         op(isDelete=False,__chr=_chr)
#         _list.clear()
#         for i in __reso:
#             _list.append(i)
#         __reso.clear()
#         for i in _list:
#             if i[_pos-1] != _chr:
#                 __reso.append(i)
#     else:
#         fflush()
#         continue
#     _list.clear()
#     for i in __reso:
#         _list.append(i)
#     print("looped")
i=0
word="crane"
print("next:",word)
_result=input()
solve(word,_result)
word="ghost"
while True:
    print("next:",word)
    _result=input()
    solve(word,_result)
    word=getBestAnswer()
            
def jumlahhurufvokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (jumlahhuruf,vokal)
print(jumlahhurufvokal("surakarta"))
def jumlahhurufkonsonan(a):
    v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    konsonan=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)
print(jumlahhurufkonsonan("surakarta"))

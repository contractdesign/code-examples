#!/usr/bin/env python

import string


def commonChar(s):
    '''print the three most common character'''

    # initialize dictionary with an entry for each lowercase character
    d = {}
    for char in string.ascii_lowercase:
        d[char] = 0

    # scan through letters in string, incrementing dictionary for each
    for c in s:
        d[c] = d[c] + 1


    # create list of tuples
    l_tuples = [(k,v) for k,v in d.iteritems()]

    # sort by value
    l_tuples = sorted( l_tuples, key=lambda tup: tup[0])
    l_tuples = sorted( l_tuples, key=lambda tup: tup[1], reverse=True)

    for tup in l_tuples[0:3]:
        print tup[0], tup[1]


commonChar( 'ybzhgdrefvdnjyfoswjuslbpuvtvfgzvnpayvjwzxkdpnbdnrsodnqhpqspojipjwgxaltzoikuucixfsoueknofvsohtqtvxvihtsevdojscucxwnivgzjazfsznswxbjylqejlgpkppwezlxhfhwuphrnqfdiowmeikwdozhjwmcneixidypdikthxxvppjakeffvhpmsxijiolpybpntbiuehpwkobetpglwxexuoxgwdbcsfvskkczxluccfkrwmpvbknadmbivdrypxtlmbnvqvcnoyciqcfnpkenvwkkosvsnxiqibkirlikwsdcnqruirprxhlenlrxahfiyhfgvbwqehddnqdtfgzwbyudmirkqmzkhxcwqxxvyrtrrmsezyvuanpcjisbfywzqesxyxlulaxamyedjyautncorctzanmosfpuescfqhrydrsohttsohvpkqppxdjsefcnelearcrypndesagvybsnzikxjqyzsvcpiypmkjaihrouvcajsxxsnsavasoxgigbhfxhbtivoyoflmmjmtxrxrsezgzcfkqiczphapeugunnyhpzpeisgohuuuchqcjbhvzojsaiecebllqevoakkfsdwqfuaozouhdgnuludvdcojalzztzkfmqxagdrlcekwyxerosaeplyzgjxwbiowidwgdnmdekjinuseaswpvmnpolistdinevfcfzlognzzfrlfoogxhyiwrfeaplrryyvyygxwgqbpaxcgrzfbhcsmbxeinwgmkpgzbdnoxdppkdvewajsnujyrojmiuvimgpkbhjmxsgaalyyovdipfeyiaeybyyvhdyacyuljzhmhtnvoapcijurxjbjalunfhtbvaiffutjxpvaedxyvrrqckxecqkniienwmmtkpwmpqkvhjigzqmtuouuxwmhohxyauzuakyvaekvyrjuuqgtcfptsuczdbeeloffdqewalyyygokdxor' )

'''
p 49
x 49
i 47
'''

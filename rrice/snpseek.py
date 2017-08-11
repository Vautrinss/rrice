#!/usr/bin/env python3

import helper
import json

def snpSeek(contig, start, end):

    Log =  open('log.txt', 'w')
    url = 'http://snp-seek.irri.org/ws/genomics/gene/osnippo/'
    u = ''
    model = '&model=rap\n' #'&model=msu7\n'
    data = []

    Log.write(url + contig + '?' + 'start='+ start + '&end='+ end + '&model=msu7\n')
    try:
        #u = urllib.urlopen(url + contig + '?' + 'start='+ start + '&end='+ end+'&model=msu7\n')
        urlFind = url + contig + '?' + 'start='+ start + '&end='+ end +'&model=msu7'
        r = helper.connectionError(urlFind)
        # encodage en bytes et pas en string  d'ou le decode
        data = json.loads(r.content.decode('UTF-8'))
    except:
        Log.write(url + contig + '?' + 'start='+ start + '&end='+ end +'&model=msu7\n')
        pass
    locus = contig + ':' + start + '-' + end

    #retourne un tableau
    return data

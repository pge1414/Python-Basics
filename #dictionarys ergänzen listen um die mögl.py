#dictionarys ergänzen listen um die möglichkeit nicht nur die elemente selbst du wählen sondern auch die indizes
#sie bestehen schlüssel-werte-paaren

# dict1 = { "hund": "dog", "Katze": "cat"}
# dict1["fisch"] = "fish"
# dict1.update({"Esel": "donkey", "löwe": "lion"})
# wert1 = dict1["Esel"]
# print(wert1)
# deutsch1 = "schlange"
# english1 = "snake"
# dict1[deutsch1] = english1
# print(dict1)

# for key in dict1.keys():
#     print(key)

# for value in dict1.values():
#    print(value)

# for key, value in dict.items():
#    print(key, value)

# if "Katze" in dict1:
#    print("Katze"+ dict1["Katze"])

rohtext = "Goethe beginnt mit einer Würdigung von Steinbachs Werk, indem er den Gedanken verwirft, Steinbach aus Ehrerbietung ein Denkmal zu bauen, da er sich durch den Bau des Münsters bereits selbst ein Denkmal geschaffen habe. Als Goethe das erste Mal das Münster sah, war er von dem allgemein geltenden Vorurteil, alles, was gotisch ist, sei von willkürlichen Verzierungen erdrückt und überladen, eingenommen. Gotisch war für ihn, wie für die meisten seiner Zeitgenossen, alles, was sich nicht mit seiner Auffassung von Kunst vereinbaren ließ. Dieses Urteil wurde von seinen unerwarteten Empfindungen beim Anblick des Münsters entkräftet. Der Eindruck, dass alle Einzelheiten miteinander harmonierten, erfüllte seine Seele, und das Münster wirkte auf ihn wie etwas von Göttern Erschaffenes für die Ewigkeit. Somit wäre gotisch für Goethe kein passender Begriff, da er bei diesem Kunstwerk nicht genügend Ehrerbietung erzeuge."\
    +"Nach Goethes Ansicht war Steinbach der Erste, dem es gelang, bei einem Kunstwerk unzählige Einzelheiten zu einem harmonisierenden Ganzen zusammenzufügen. Außerdem habe er nur seine eigenen Ideen miteingebracht und keine fremden Gedanken zugelassen, wobei er sich vorrangig von seinen Gefühlen habe leiten lassen. Durch das Münster habe Steinbach einen ewig währenden, gottgleichen Status erreicht, da Goethe ihm die gleiche Schöpfungskraft wie den Göttern zuspricht. Des Weiteren solle er mehr Seligkeit zu den Menschen bringen als Prometheus. Damit entspricht Steinbach Goethes Vorstellungen von einem Genie. Nach Goethe ist in jedem Menschen eine bildende Natur, die deutlicher wirkt, je mehr man sich nach seinen Gefühlen richtet."\
        +"Um seine Vorstellungen von wahrer Kunst zu verdeutlichen führt Goethe das Gegenteil auf. Als Beispiel hierfür nennt er die Franzosen und Italiener, die ihre architektonischen Meisterwerke an alte Formen anlehnen und diese somit nur nachahmen würden. Hierbei sei jedoch nicht immer von Nachahmung zu sprechen, vielmehr würden sie fremdes Gedankengut verwenden und es durch ihre Bearbeitung verderben. Sie seien nicht in der Lage, ewig Währendes zu schaffen, da sie sich nicht auf ihre Gefühle verlassen hätten und somit nicht die harmonisierende Wirkung des Münsters erreicht hätten. Bei der Schaffung ihrer Kunstwerke hätten sie sich an das gehalten, was andere von ihnen verlangt haben, und somit seien keine eigenen Erschaffungen entstanden. Da immer noch aus alten Prinzipien und Regeln beschlossen werde, was richtig sei, entstehe nichts Neues, sondern nur einfältige und patriarchalische Kunst. Da die bestehenden Regeln häufig gegen die Natur gerichtet seien, würden diese Prinzipien die Kunst und deren Erkenntnis behindern. Das bedeutet, die Menschen seien dadurch unfähig, die Wahrheit zu erkennen. Für Goethe war diese durch die alte Regeln hervorgerufene Einförmigkeit unerträglich, und er glaubte, seine Seele werde durch sie unterdrückt."\
            +"Wahre Kunst äußere sich darin, dass, wie in der Natur, unzählige Einzelteile ein harmonisierendes Ganzes ergeben würden, wobei alles seinen Zweck habe und nichts nutzlos sei. Kunst entstehe aus willkürlichen Formen, da sie erst durch Empfindungen zu etwas Ganzem werde, und nur aus eigenen Ideen, ohne die nach Johann Gottfried Herder ungeliebten Einflüsse. Diese Form der Kunst sei die einzig Wahre. Goethe mag nichts Gekünsteltes, für ihn trifft dieser Zustand vor allem auf die Natur zu. Aus diesem Grund sollten die Menschen aufhören, die Dinge um sie herum (also die Natur) zu verschönern, da diese schon vollkommen seien. Goethe sieht dort Schönheit, wo viele seiner Mitmenschen nur Unkultiviertheit („Rauheit“) sehen, daher sei er auch in der Lage das Münster dementsprechend zu würdigen, wo andere vielleicht nur Verständnislosigkeit aufbringen. Diese Schönheit entsteht durch Sinneseindrücke und ist nicht rational erklärbar. Kritiker des Münsters werden dazu aufgefordert, zu den Italienern oder Franzosen zu gehen und somit der „wahren Kunst“ den Rücken zuzuwenden. Das Münster verdiene Anerkennung, und in Anbetracht dessen werde Goethe über die seiner Meinung nach fehlgeschlagenen Versuche Steinbachs hinwegsehen."\
                +"Aus diesen Gründen bringt Goethe dem Straßburger Münster und seinem Erbauer höchste Bewunderung entgegen."
text = rohtext.lower().replace("(", "").replace(")", "").replace("„", "").replace("“", "").replace(",", "").replace(".", "")
text_liste = text.split()
# print(text_liste)
# h=0
# for word in text_liste:
#     for word2 in text_liste:
#         if word == word2:
#             h = h+1
#     print(word, h)

def wörterzählen(text_liste):
    dict_wörter = {}
    for i in range(len(text_liste)):
        if text_liste[i] not in dict_wörter:
            dict_wörter.update({ text_liste[i]: 1})
        else:
            dict_wörter[text_liste[i]] += 1
    return dict_wörter

dict_wörter = wörterzählen(text_liste)
print(dict_wörter)

# def großte(dict_wörter, text_liste):
#     for key in dict_wörter:
#         p = dict_wörter[key]
#         for key2 in dict_wörter:
#             p2 = dict_wörter[key2]
#             print(p2)
#             if p <= p2:
#                 break
#     return key

# dict_wörter = großte(dict_wörter, text_liste)
# print(dict_wörter)

bisher_größte_anzahl = 0
größtes_wort = ""
for key, value in dict_wörter.items():
    if value > bisher_größte_anzahl:
        bisher_größte_anzahl = value
        größtes_wort = key
print(größtes_wort)

zweitgrößtes_wort = dict_wörter.pop(größtes_wort)
bisher_größte_anzahl = 0
größtes_wort = ""
for key, value in dict_wörter.items():
    if value > bisher_größte_anzahl:
        bisher_größte_anzahl = value
        größtes_wort = key
print(größtes_wort)

summe = 0
hy = len(text_liste)
for key, value in dict_wörter.items():
    
    summe += value
print(hy / summe)
print(hy)

anzahl = 0
for key in dict_wörter.keys():
    if key[0] == 'd':
        anzahl += 1
print(anzahl)

dict_g_wörter = {}
for key, value in dict_wörter.items():
    if key[0] == 'g':
        dict_g_wörter.update({key: value})
bisher_größte_anzahl2 = 0
größtes_wort2 = ""
for key, value in dict_g_wörter.items():
    if value > bisher_größte_anzahl2:
        bisher_größte_anzahl2 = value
        größtes_wort2 = key
print(größtes_wort2)

liste = []
for key in dict_wörter.keys():
    if key[0] not in liste:
        liste.append(key[0])
print(liste)

        

#!/usr/bin/python

import random
import copy

pot = [[['Russia', 0, 65], ['Germany', 0, 1], ['Brazil', 2, 2], ['Portugal', 0, 3], ['Argentina', 2, 4], ['Belgium', 0, 5], ['Poland', 0, 6], ['France', 0, 7]],
[['Spain', 0, 8], ['Peru', 2, 10], ['Switzerland', 0, 11], ['England', 0, 12], ['Colombia', 2, 13], ['Mexico', 4, 16], ['Uruguay', 2, 17], ['Croatia', 0, 18]],
[['Denmark', 0, 19], ['Iceland', 0, 21], ['Costa Rica', 4, 22], ['Sweden', 0, 25], ['Tunisia', 3, 28], ['Egypt', 3, 30], ['Senegal', 3, 32], ['Iran', 1, 34]],
[['Serbia', 0, 38], ['Nigeria', 3, 41], ['Australia', 1, 43], ['Japan', 1, 44], ['Morocco', 3, 48], ['Panama', 4, 49], ['South Korea', 1, 62], ['Saudi Arabia', 1, 63]]]


class group:
    def __init__(self,n):
        self.id = chr(n + 65)
        self.nations = []
        self.EU = 0
        self.AS = 0
        self.SA = 0
        self.AF = 0
        self.CN = 0
        self.totalrank = 0
    def cont_update(self,m):
        if m[1] == 0:
            self.EU += 1
        elif m[1] == 1:
            self.AS += 1
        elif m[1] == 2:
            self.SA += 1
        elif m[1] == 3:
            self.AF += 1
        elif m[1] == 4:
            self.CN += 1
        else:
            print('Wrong data in ' + m[0])

    def valid_check(self,k):
        if k[1] == 0 and self.EU == 2:
            return False
        elif k[1] == 1 and self.AS == 1:
            return False
        elif k[1] == 2 and self.SA == 1:
            return False
        elif k[1] == 3 and self.AF == 1:
            return False
        elif k[1] == 4 and self.CN == 1:
            return False
        else:
            return True

    def cont_rollback(self,m):
        if m == 0:
            self.EU -= 1
        elif m == 1:
            self.AS -= 1
        elif m == 2:
            self.SA -= 1
        elif m == 3:
            self.AF -= 1
        elif m == 4:
            self.CN -= 1

def team_select(result,pot):
    back_up = copy.deepcopy(result)
    temp = copy.deepcopy(pot)
    if ['Russia', 0, 65] in temp:
        temp2 = temp[1:]
        random.shuffle(temp2)
        temp[1:] = temp2
    else:
        random.shuffle(temp)
    for index in range(0,8):
        get_flag = False
        for key,nation in enumerate(temp):
            if result[index].valid_check(nation):
                result[index].cont_update(nation)
                result[index].nations.append(nation[0])
                temp.pop(key)
                get_flag = True
                break
        if not get_flag:
            result = copy.deepcopy(back_up)
            result = team_select(result,pot)
            break
    return result

result = []
for i in range(0,8):
    result.append(group(i))

for item in pot:
    result = team_select(result,item)

for item in result:
    print(str(item.id) + " : " + str(item.nations))

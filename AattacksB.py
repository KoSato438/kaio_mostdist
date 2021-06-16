import random

counter=0
Aloss=0
Awin=0


while counter <10000:
    print(counter+1,'回目、AがBを打ちます')
    x=random.randint(0,2)
    if x == 0:
        print('BにHitした為、次のターンにCに負けました。\n')
        Aloss += 1
        counter += 1
    else:
        print('Bに当たらず、次はBがCを打ちます')
        x=random.randint(3,5)
        if x == 3:
            print('Bの攻撃がHitしたため、AvsBのデスマッチ')
            while 1:
                y=random.randint(6,8)
                if y ==6:
                    print('Aの銃がBに命中！！A勝利！！')
                    Awin += 1
                    counter += 1
                    print('Aの勝率=',Awin / counter *100,'\n')
                    break
                else:
                    print('Aが外した！Bの番！')
                    y=random.randint(0,2)
                    if y == 0:
                          print('Bが外した！Aの番！')
                    else:
                          print('そしてBが命中！')
                          Aloss+=1
                          print('Aが',Aloss,'回目の敗北...')
                          counter += 1
                          print('Aの勝率=',Awin / counter *100,'\n')
                          break
        else:
            print('Bの銃はHITせず、BはCにやられてしまった...AとCのデスマッチ！！')
            z=random.randint(5,7)
            if z==5:
                print('Aの球がCに命中！！A勝利！！')
                Awin += 1
                counter += 1
                print('Aの勝率=',Awin / counter *100,'\n')
            else:
                print('Aの球はCに命中しなかった...AはCに敗れた...')
                Aloss += 1
                counter += 1
                print('Aの勝率=',Awin / counter *100,'\n')


print('結果発表です。')
print('Aの戦績は',counter,'戦、',Awin,'勝、',Aloss,'敗により、勝率',Awin/counter*100,'%でした')
end = input('おわり')

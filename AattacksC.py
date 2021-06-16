import random

counter=0
Aloss=0
Awin=0


while counter <10000:
    print(counter+1,'回目、AがCを打ちます')
    x=random.randint(0,2)
    if x <= 1:
        print('CにHitしなかった為、BがCに攻撃します。')
        y=random.randint(3,5)
        if y == 3:
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
        else:
            print('Bの攻撃がHitしたため、AvsBのデスマッチ')
            while 1:
                b=random.randint(6,8)
                if b <=7:
                    print('Aが外した！Bの番！')
                    c=random.randint(0,2)
                    if c == 0:
                          print('Bが外した！Aの番！')
                    else:
                          print('そしてBが命中！')
                          Aloss+=1
                          print('Aが',Aloss,'回目の敗北...')
                          counter += 1
                          print('Aの勝率=',Awin / counter *100,'\n')
                          break            

                else:
                    print('Aの銃がBに命中！！A勝利！！')
                    Awin += 1
                    counter += 1
                    print('Aの勝率=',Awin / counter *100,'\n')
                    break
                
    else:
        print('CにHitしたため、BとAのデスマッチ！！！')
        while 1:
            d=random.randint(6,8)
            if d == 6:
                print('Bが外してしまった...Aの番！！')
                e=random.randint(0,2)
                if e <= 1:
                    print('Aが外した！Bの番！')
                else:
                    print('AがBに命中！！A勝利！！')
                    Awin +=1
                    counter +=1
                    print('Aの勝率=',Awin / counter *100,'\n')
                    break
                    
            else:
                print('BがAに命中！')
                Aloss +=1
                counter +=1
                print('Aが',Aloss,'回目の敗北...')
                print('Aの勝率=',Awin / counter *100,'\n')
                break



print('結果発表です。')
print('Aの戦績は',counter,'戦、',Awin,'勝、',Aloss,'敗により、勝率',Awin/counter*100,'%でした')
end = input('おわり')

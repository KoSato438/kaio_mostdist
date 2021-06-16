import random

#これは、哲学一致までの距離が最も遠い人がいる練習場所を
#巻き込み練習のみ行った場合の哲学一致シュミレーションです。

allcount = 0

for nnn in range (1000):
    kyara=["sak","yabe","aki","ao","naka","wil","kal","biwa","kog","sek","ari"]
    kyaramas=["sak","yabe","aki","ao","naka","wil","kal","biwa","kog","sek","ari"]

    kyorimas={
        "sak":[8,8],
        "yabe":[5,6],
        "aki":[22,22],
        "ao":[10,20],
        "naka":[20,10],
        "wil":[3,11],
        "kal":[6,11],
        "biwa":[7,22],
        "kog":[22,7],
        "sek":[11,3],
        "ari":[11,6],
        }

    kyorilist={
        "sak":[8,8],
        "yabe":[5,6],
        "aki":[22,22],
        "ao":[10,20],
        "naka":[20,10],
        "wil":[3,11],
        "kal":[6,11],
        "biwa":[7,22],
        "kog":[22,7],
        "sek":[11,3],
        "ari":[11,6],
        }
    tensyonlist={"sak":"L","yabe":"L","aki":"L","ao":"L","naka":"L","wil":"L","kal":"L","biwa":"L","kog":"L","sek":"L","ari":"L"}
    basyolist={"sak":"D","yabe":"D","aki":"D","ao":"D","naka":"D","wil":"D","kal":"D","biwa":"D","kog":"D","sek":"D","ari":"D"}

    Asum=0
    Bsum=0
    Csum=0
    Dsum=0
    Esum=0
    Fsum=0

    alcount = 0

    #哲学完全一致ﾘｽﾄ
    kaniti=list()

    #A～F６つ場所を作成
    A=list()
    B=list()
    C=list()
    D=list()
    E=list()
    F=list()



    while len(kyara) > 0:
    #for tes in range(1):

        #場所合計値初期化
        Asum=0
        Bsum=0
        Csum=0
        Dsum=0
        Esum=0
        Fsum=0
        m=0

        mostdis=[]
        longlist=[]
        mosdisnow = 0
        mosdisname=list()
        

        #各場所を初期化    
        A=list()
        B=list()
        C=list()
        D=list()
        E=list()
        F=list()

        #場所を決定
        for basyo in kyara:
            x=random.randint(1,6)
            if x == 1:
                basyolist[basyo]="A"
            elif x == 2:
                basyolist[basyo]="B"
            elif x == 3:
                basyolist[basyo]="C"    
            elif x == 4:
                basyolist[basyo]="D"
            elif x == 5:
                basyolist[basyo]="E"
            else:
                basyolist[basyo]="F"

        # A～Dにいる人をリストA～Dに格納
        for i, v in basyolist.items():
            if v == "A":
                A.append(i)
            elif v == "B":
                B.append(i)
            elif v == "C":
                C.append(i)
            elif v == "D":
                D.append(i)
            elif v == "E":
                E.append(i)
            else:
                F.append(i)

        #各場所の距離合計を算出
        for j in A:
            Asum += kyorilist[j][0] + kyorilist[j][1]
        for j in B:
            Bsum += kyorilist[j][0] + kyorilist[j][1]
        for j in C:
            Csum += kyorilist[j][0] + kyorilist[j][1]
        for j in D:
            Dsum += kyorilist[j][0] + kyorilist[j][1]
        for j in E:
            Esum += kyorilist[j][0] + kyorilist[j][1]
        for j in F:
            Fsum += kyorilist[j][0] + kyorilist[j][1]

        #並び替え、で最も距離が遠い人がいる場所を抽出 nlists[0][0]
        
        for s in kyara:
            mostdis.append([s,kyorilist[s][0]+kyorilist[s][1]])
        

        mostdis.sort(key=lambda x:-x[1])
        mostdispra = mostdis[0][0]

        #mostdisで一番距離遠い人と同じく遠い人を抽出
        mosdisnow = mostdis[0][1]
        for a,b in mostdis:
            if b == mosdisnow:
                mosdisname.append(a)

        if len(mosdisname) > 1:
            for c in mosdisname:
                if c in A:
                    longlist.append([len(A),A])
                elif c in B:
                    longlist.append([len(B),B])
                elif c in C:
                    longlist.append([len(C),C])
                elif c in D:
                    longlist.append([len(D),D])
                elif c in E:
                    longlist.append([len(E),E])
                else:
                    longlist.append([len(F),F])
            longlist.sort()
            longlist.reverse()
            mostpra=longlist[0][1]
        else:    
            #最も遠い人がいる練習場所を探す
            if mostdispra in A:
                mostpra = A
            elif mostdispra in B:
                mostpra = B
            elif mostdispra in C:
                mostpra = C
            elif mostdispra in D:
                mostpra = D
            elif mostdispra in E:
                mostpra = E
            else:
                mostpra = F
        

        #並び替え、で最も距離の総和が大きい場所を抽出 nlists[0][0]

        #nlists = [(A,Asum),(B,Bsum),(C,Csum),(D,Dsum),(E,Esum),(F,Fsum)]
        #nlists.sort(key=lambda x:-x[1])
        #mostpra = nlists[0][0]

        #テンションH全キャラの距離を引く
        for q in kyara:
            if tensyonlist[q] == "H":
                kyorilist[q][0] -= 1
                kyorilist[q][1] -= 1

        #最も距離の総和が大きい場所にいるキャラから各距離を1引いてテンションH
        for k in mostpra:
                kyorilist[k][0] -= 1
                kyorilist[k][1] -= 1
                tensyonlist[k] = "H"

        #ほかのキャラのテンションをLに
        lowte = set(mostpra)^set(kyara)
        for n in lowte:
            tensyonlist[n] = "L"


        #各キャラ距離のマイナス値整理　および完全一致をﾘｽﾄから削除
        for m in kyara:
            if kyorilist[m][0] < 0 and kyorilist[m][1] < 0:
                kyorilist[m][0] = 0
                kyorilist[m][1] = 0
            elif kyorilist[m][0] < 0:
                kyorilist[m][0] = 0
            elif kyorilist[m][1] < 0:
                kyorilist[m][1] = 0
            if kyorilist[m][0] <= 0 and kyorilist[m][1] <= 0 :
                kaniti.append(m)

        for r in kaniti:
            if r in kyara:
                kyara.remove(r)
                basyolist.pop(r)


        #とりあえず状態報告

        alcount += 1

        if len(kyara)==0:
            print(nnn,"回目、全キャラが哲学一致しました。所要ターンは",alcount,"ターンでした。\n")
            allcount += alcount

print(nnn+1,"回サクセスをやった結果、合計",allcount,"ターンかかりました。")
print("平均クリアターンは",allcount / (nnn+1) ,"ターンでした。")

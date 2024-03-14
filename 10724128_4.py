#演算法分析機側
#學號 : 10724128
#姓名 : 吳宇哲
#中原大學資訊工程系
import time
def smallGroups(input,i,result,have_check):
    i_check = False
    input_check =False
    input_place = 0
    i_place = 0
    if i == len(input) :
       return
    else :
        if ( i == 0 )&(input[i] == 0) : # first
           smallGroups(input,i+1,result,have_check)

        else :
         for j in range(len(result)) :
           for k in range(len(result[j])) :
              if ( result [j][k] == i) :
                 i_place = j
                 i_check = True
              if ( result [j][k] == input[i]) :
                 input_place = j
                 input_check =True
        temp = []
        if ( input[i] == i ) : # 自己一組
           temp.append(input[i])
           result.append(temp)
        elif ( ((input_check == True)& (i_check == True))&( input_place != i_place)) : # 兩人以放入 需合併
           for j in range(len(result[input_place])) :
              result[i_place].append(result[input_place][j])
           del result[input_place]
        elif (input_check == False)& (i_check == False):  #皆無放入
           temp.append(input[i])
           temp.append(i)
           result.append(temp)
        elif input_check == False :
           result[i_place].append(input[i])
        elif i_check == False :
           result[input_place].append(i)
        smallGroups(input,i+1,result,have_check)


   
print("小群體(Small Groups)")
group_size = int(input("輸入總人數 : (輸入 0 結束執行)"))
while group_size != 0 :
    temp = []
    temp = input().split()
    input1 = []
    if len(temp) < group_size :
        print("請輸入足夠數量的整數")
    else :
      have_check = []
      for i in range(group_size) :
        n = int(temp[i])
        input1.append(n)
        have_check.append(False)
      list=[]
      first = [0]
      list.append(first)
      have_check[0] = True
      start_time = time.time()
      result = smallGroups(input1,0,list,have_check)
      print(list)
      print("result   = ",len(list))
      total_time = time.time() - start_time
      print ( "run time : ",total_time )

    group_size = int(input("輸入字串大小 : "))
"""
10
4 7 2 9 6 0 8 1 5 3
3
0 2 1
8
1 5 6 2 7 3 0 4
0
[0 1 2 3 5 6 ][4 7]
"""

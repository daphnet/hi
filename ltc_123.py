#19 執行第一個Python程式
#>python __.py


#21 進入正題： 宣告 (Declare)
#decalre(宣告)：創出變數的意思，只有第一次是宣告
#variable(變數)：一個名字，是一個標籤，裝著或對應到某個值(value)
#assignment(設值指令)：遇到等號就是設值指令，把等號右邊的值存到等號左邊的標籤(變數)。
#只有第一次是創作，之後都是改變


x = 5 #宣告變數x，它的值是5
print (x)
x = 10 #把變數x的值設成10 -> 設值指令
x = 10000
y = 2

#22 資料型別 (Data Types)
#整數(integar) int
#浮點數/小數 float
#布林值 (boolean) bool (True, False)
#字串/文字 (string) str 'Allen'

price = 10
pen = 0.38
rain = True
name = 'Daphne'

print (price)
print (pen)
print (rain)
print (name)

print(price, pen, rain, name)

#23 Input (讓使用者輸入)
name = input('please enter your name: ')
print (name)
print ('Hi,', name, '.')




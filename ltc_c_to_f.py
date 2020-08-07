# 35 [小練習] 溫度轉換程式
# 攝氏Celsius溫度轉換成華氏Fahrenheit溫度
# F = C * 9 / 5 + 32
# C = (F - 32) * 5 / 9
# 程式要讓使用者輸入攝氏溫度，印出華氏溫度。

c_temp = input ('please enter Celsius temperature: ')
f_temp = float(c_temp) * 9 / 5 + 32
print ('Celsius', c_temp, 'degree is Fahrenheit', f_temp, 'degree.')
print (c_temp, 'Celsius degree', 'is', f_temp, 'Fahrenheit degree.')


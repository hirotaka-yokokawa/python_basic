# # 例
# $ python bmi.py
# Height(m)? > 170
# Weight(kg)? > 60
# Your BMI is 20.76

# 計算式
# 　BMI＝ 体重kg ÷ (身長m)2
# 　適正体重＝ (身長m)2 ×22

input_Height = int(input("Height(cm) ? > "))
input_Weight = int(input("Weight(kg) ? > "))

formula = (input_Weight / input_Height / input_Height)#BMIを出すための体重÷身長÷身長の式
BMI = (formula * 10000)#正しい整数に直す式

text = "Your BMI is {:.2f}"#少数第二位までを表示する
print(text.format(BMI))









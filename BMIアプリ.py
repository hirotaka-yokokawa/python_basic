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

formula = pow(input_Height,2)# 身長をべき乗するための式
formula_2 = (input_Weight / formula)#BMIを出すための体重÷身長のべき乗の式
BMI = (formula_2 * 10000)#正しい整数に直す式

text = "Your BMI is {:.2f}"
print(text.format(BMI))









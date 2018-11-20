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

formula = pow(input_Height,2)
formula_2 = (input_Weight / formula)
BMI = (formula_2 * 10000)

text = "Your BMI is {:.2f}"
print(text.format(BMI))









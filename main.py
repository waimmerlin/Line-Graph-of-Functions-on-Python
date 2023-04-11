# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [6, 4, 3, 8, 0]
#
# plt.plot(x, y)
# plt.xlabel('X-ось')
# plt.ylabel('Y-ось')
# plt.title('Пример линейного графика')
# plt.show()



# import matplotlib.pyplot as plt
#
# labels = ['Яблоки', 'Апельсины', 'Груши', 'Бананы']
# sizes = [15, 30, 45, 10]
#
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title('Пример круговой диаграммы')
# plt.show()




# import matplotlib.pyplot as plt
#
# # Запрашиваем у пользователя значение, для которого нужно найти соответствующие точки на графике
# num = float(input("Введите число: "))
#
# # Создаем списки значений для оси X и Y
# x = [1, 2, 3, 4, 5]
# y = [1, 3, 4, 4, 5]
#
# # Создаем список, который будет хранить все значения по оси Y, равные заданному числу
# y_values = []
#
# # Итерируемся по всем элементам списка Y и проверяем, равен ли текущий элемент заданному числу
# for i in range(len(y)):
#     if y[i] == num:
#         y_values.append(y[i])
#
# # Строим график
# plt.plot(x, y, 'bo-')
# plt.xlabel('X-ось')
# plt.ylabel('Y-ось')
# plt.title('Пример линейного графика')
#
# # Добавляем точки на график, которые соответствуют заданному числу
# for y_val in y_values:
#     plt.plot(x[y.index(y_val)], y_val, 'ro')
#
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
#
# # Создаем списки значений для оси X и Y
# x = [1, 2, 3, 4, 5]
# y = [1, 3, 4, 4, 5]
#
# # Строим линейный график
# plt.plot(x, y)
# plt.xlabel('X-ось')
# plt.ylabel('Y-ось')
# plt.title('Пример линейного графика')
# plt.show()
#
# # Запрашиваем у пользователя значение по оси X
# x_value = float(input("Введите значение по оси X: "))
#
# # Используем метод interp для нахождения соответствующего значения на оси Y
# y_value = np.interp(x_value, x, y)
# # Выводим соответствующее значение на оси Y
# print(f"Значение по оси Y для X = {x_value} равно {y_value}")
#



import numpy as np
import matplotlib.pyplot as plt

# Set values for the X-axis
x = list(map(float,input('Enter values for the X-axis separated by a space: ').split()))
# Set values for the Y axis
y = list(map(float,input(f'Enter {len(x)} values for the y-axis separated by a space:  ').split()))


# Building a line chart
plt.plot(x, y)

#if you wish, we can save a photo of the graph
# plt.savefig('my_plot.png')

#Ask a question
ask = input('Do you want to rename the x and y axes? Yes/No :')

#Processing the response
if ask.lower() == 'yes':
    # Enter data for this or that answer
    askx = input('If you want to keep the usual name, just write the number "1" Otherwise, enter the name for the X-Axis: ')

    asky = input('If you want to keep the usual name, just write the number "1" Otherwise, enter the name for the Y-Axis: ')
    if askx == '1':
        plt.xlabel('X-axis')
    else:
        plt.xlabel(askx)
    if asky == '1':
        plt.ylabel('Y-axis')
    else:
        plt.ylabel(asky)
else:
    # Leave the names
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
#Name of our chart (optional)
plt.title('Line Graph of Functions')
plt.show()



#chart table
print('-----------------------------The table for the graph will look like this-----------------------------')
#Here we will write the values of the X-axis
eks = 'X - | '

#Here we will write the values of the Y-axis
igrik = 'Y - | '

for eksik in range(len(x)):

    # X-axis values
    eks+=f'{x[eksik]} | '

for ipchik in range(len(y)):

    # Y-axis values
    igrik+=f'{y[ipchik]} | '

#Display the graph table
print(f"{eks}\n{igrik}")

# Ask the user what he wants to measure
choice = input("What do you want to measure? Enter 'X' if you want to find a value on the y-axis, and 'Y' if you want to find values on the x-axis: ")

# If the user wants to find a value on the y-axis
if choice == 'X':
    # Ask the user for the X value
    x_value = float(input("Enter a value along the x-axis: "))

    # Use the interp method to find the corresponding value on the y-axis
    y_value = np.interp(x_value, x, y)

    # Display the corresponding value on the Y-axis
    print(f"Y-axis value for X = {x_value} is {y_value}")

# If the user wants to find values on the x-axis
elif choice == 'Y':
    # Ask the user for a Y-axis value
    y_value = float(input("Enter a Y value:"))

    # Use the where method to find the corresponding values on the x-axis
    x_values = np.where(np.array(y) == y_value)[0]

    # Plot appropriate values on the x-axis
    print(f"The x-axis values for Y = {y_value} are {', '.join([str(x[i]) for i in x_values])}")

# If the user entered an invalid option
else:
    print("You entered an invalid option")

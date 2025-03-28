def rectangle_info(side1, side2):
    perimeter = (side1 + side2) * 2
    area = side1 * side2
    return perimeter, area
side1 = float(input("შეიყვანეთ პირველი გვერდის სიგრძე: "))
side2 = float(input("შეიყვანეთ მეორე გვერდის სიგრძე: "))
perimeter, area = rectangle_info(side1, side2)
print(f"პერიმეტრი: {perimeter}")
print(f"ფართობი: {area}")
def get_digits() -> list[int]:
    num = int(input("عدد مورد نظر را وارد کنید: "))

    digits: list[int] = []
    while (num != 0):
        digits.append(num % 10)
        num //= 10
        
    return digits


def num_to_str(digits: list[int]) -> str:
    numStr: str = ""
    for i in range(len(digits) - 1, -1, -1):
        if (digits[i] == 0):
            continue
        if (i != len(digits) - 1):
            numStr += " و "
            
        if (i % 3 == 0):
            if (len(digits) > i + 1 and digits[i + 1] == 1):
                numStr = numStr[:-3]
                continue
                
            if (digits[i] == 1): numStr += "یک"
            elif (digits[i] == 2): numStr += "دو"
            elif (digits[i] == 3): numStr += "سه"
            elif (digits[i] == 4): numStr += "چهار"
            elif (digits[i] == 5): numStr += "پنج"
            elif (digits[i] == 6): numStr += "شش"
            elif (digits[i] == 7): numStr += "هفت"
            elif (digits[i] == 8): numStr += "هشت"
            elif (digits[i] == 9): numStr += "نه"
                
            if (i == 3): numStr += " هزار"
            elif (i == 6): numStr += " میلیون"
            elif (i == 9): numStr += " میلیارد"
            
        if ((i - 1) % 3 == 0):
            if (digits[i] == 1): 
                if (digits[i - 1] == 0): numStr += "ده"
                elif (digits[i - 1] == 1): numStr += "یازده"
                elif (digits[i - 1] == 2): numStr += "دوازده"
                elif (digits[i - 1] == 3): numStr += "سیزده"
                elif (digits[i - 1] == 4): numStr += "چهارده"
                elif (digits[i - 1] == 5): numStr += "پانزده"
                elif (digits[i - 1] == 6): numStr += "شانزده"
                elif (digits[i - 1] == 7): numStr += "هفتده"
                elif (digits[i - 1] == 8): numStr += "هجده"
                elif (digits[i - 1] == 9): numStr += "نوزده"
            elif (digits[i] == 2): numStr += "بیست"
            elif (digits[i] == 3): numStr += "سی"
            elif (digits[i] == 4): numStr += "چهل"
            elif (digits[i] == 5): numStr += "پنجاه"
            elif (digits[i] == 6): numStr += "شصت"
            elif (digits[i] == 7): numStr += "هفتاد"
            elif (digits[i] == 8): numStr += "هشتاد"
            elif (digits[i] == 9): numStr += "نود"
    
            if (digits[i - 1] == 0):     
                if (i == 4): numStr += " هزار"
                elif (i == 7): numStr += " میلیون"
                elif (i == 10): numStr += " میلیارد"
                
        if ((i - 2) % 3 == 0):
            if (digits[i] == 1): numStr += "صد"
            elif (digits[i] == 2): numStr += "دویست"
            elif (digits[i] == 3): numStr += "سیصد"
            elif (digits[i] == 4): numStr += "چهارصد"
            elif (digits[i] == 5): numStr += "پانصد"
            elif (digits[i] == 6): numStr += "ششصد"
            elif (digits[i] == 7): numStr += "هفتصد"
            elif (digits[i] == 8): numStr += "هشتصد"
            elif (digits[i] == 9): numStr += "نهصد"
    
            if (digits[i - 1] == 0):
                if (i == 5): numStr += " هزار"
                elif (i == 8): numStr += " میلیون"
                elif (i == 11): numStr += " میلیارد"
                    
    return numStr

def main() -> None:
    print("عدد به حروف:", num_to_str(get_digits()))

if __name__ == "__main__":
    main()

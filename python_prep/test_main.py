
def cal_avg(numbers: list) -> float:
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Exception occured: {e}")

if __name__ == "__main__":
    print("Testting the main file directly")
    number = [2,3,4,5,6]
    print(cal_avg(number))

# print("Testting the main file directly")
# number = [2,3,4,5,6]
# print(cal_avg(number))
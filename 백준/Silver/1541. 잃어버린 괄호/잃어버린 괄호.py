import sys

def main():
    exp = input().split("-")
    
    total = 0
    for i, part in enumerate(exp):
        numbers = list(map(int, part.split("+")))
        sub_total = sum(numbers)
        if i == 0:
            total += sub_total
        else:
            total -= sub_total
            
    print(total)

if __name__ == "__main__":
    main()
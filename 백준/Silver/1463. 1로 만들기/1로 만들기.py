def main():
    input_data = int(input())
    
    mem = [0] * (input_data + 1)
        
    for i in range(2, input_data + 1):
        mem[i] = mem[i-1] + 1

        if i%2 == 0:
            mem[i] = min(mem[i], mem[i//2]+ 1)
        if i%3 == 0:
            mem[i] = min(mem[i], mem[i//3] + 1)
        
    print(mem[input_data])
    
if __name__ == "__main__":
    main()
            
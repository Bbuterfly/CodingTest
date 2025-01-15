import sys
def main():
    memberList = sys.stdin.readlines()[1:]
    memberList.sort(key=lambda age : int(age.split()[0]))

    print(''.join(memberList))

if __name__ == "__main__":
    main()
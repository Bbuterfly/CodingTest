import sys

def main():
    '''
    N : 저장된 사이트 수 : 1<=N<=10^5
    M : 비밀번화를 찾으려는 사이트 수 : 1<=M<=10^5
    '''
    N, M = map(int, sys.stdin.readline().rstrip().split())
    
    password_dict = dict()
    for _ in range(N):
        url, password = sys.stdin.readline().rstrip().split()
        password_dict[url] = password
    
    passwords = []
    for _ in range(M):
        found = sys.stdin.readline().rstrip()
        passwords.append(password_dict[found])
        
    sys.stdout.write("\n".join(passwords) + "\n")

if __name__ == "__main__":
    main()
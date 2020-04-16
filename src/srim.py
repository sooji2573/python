
def srim(B, ROE, K):
    return B + (B * (ROE - K)) / K

B = int(input("자기자본 입력"))
ROE = float(input("ROE 입력"))
K = float(input("지배주주 요구수익률 입력"))

J = int(input("발행 유동주식수"))
srimVal = srim(B, ROE, K)

print("=====================")
print(srimVal)
print("=====================")
print(srimVal / J * 100000000)

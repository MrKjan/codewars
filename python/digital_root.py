
#!/usr/bin/python3

def digital_root(n):
    val = n
    sum = 0
    while True:
        if 0 == val:
            val = sum
            sum = 0
            if 10 > val:
                return val

        sum += val % 10
        val //= 10

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))

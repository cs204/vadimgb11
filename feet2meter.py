def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    v = float(v.rstrip('ft'))
    const = 0.3048
    v = const * v
    return v

main()

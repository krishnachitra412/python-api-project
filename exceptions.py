try:
    number = 10 / 0
    print(number)

except Exception as e:
    print("Error occurred")
    print(e)
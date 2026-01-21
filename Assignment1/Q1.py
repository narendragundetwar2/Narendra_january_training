def count_message(msg, count=0):
    count += 1    
    print(f"Message: {msg} | Current Count: {count}") 
    return count
count_message("Hello!")
count_message("Testing...")
count_message("Is this increasing?")

 Output:- Message: Hello! | Current Count: 1
          Message: Testing... | Current Count: 1
          Message: Is this increasing? | Current Count: 
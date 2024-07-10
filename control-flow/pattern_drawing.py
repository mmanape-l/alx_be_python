def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Validate that the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Newline after each row
        row += 1

if __name__ == "__main__":
    main()
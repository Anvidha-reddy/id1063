def firstStable(a, n, tolerance):
    for i in range(n - 1):
        diff = abs(a[i + 1] - a[i])
        
        # Add epsilon (1e-9) to avoid floating point issues
        if diff <= tolerance + 1e-9:
            return i
            
    return -1

n = int(input("Enter n: "))
    
    # Read n float values
readings = list(map(float, input("Enter the readings: ").split()))
    
tolerance = float(input("Enter tolerance: "))
    
    # Print result index
print(firstStable(readings, n, tolerance))




def binary_search(arr, target):
    """
    Binary search implementation
    Returns index of target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    # Test array (must be sorted for binary search)
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    print(f"Array: {arr}")
    print(f"Searching for: {target}")
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array")
    
    # Test with element not in array
    target2 = 10
    print(f"\nSearching for: {target2}")
    result2 = binary_search(arr, target2)
    
    if result2 != -1:
        print(f"Element found at index: {result2}")
    else:
        print("Element not found in array")

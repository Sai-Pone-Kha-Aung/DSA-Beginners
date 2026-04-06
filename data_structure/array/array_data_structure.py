# Python's built-in list is a dynamic array (mix data type)
def demo_python_list():
    print("--- Python List (Dynamic Array) ---")
    my_list = [10, 20, 30, 50, 60]
    print(f"Original list: {my_list}")

    my_list.append(40)
    print(f"\nAfter append(40): {my_list}")

    my_list.insert(1, 15)
    print(f"\nAfter insert(1, 15): {my_list}")

    my_list.pop()
    print(f"\nAfter pop(): {my_list}")

# Python's array module is a memory-efficient way to store arrays of primitive types (same data type)
def demo_python_array_module():
    from array import array
    print("\n--- Python Array Module ---")
    # 'i' stands for signed integer. This array can ONLY hold integers.
    typed_array = array('i',[1, 2, 3, 4])
    print(f"\nTyped array original:")
    print(*typed_array)

    typed_array.append(5)
    print(f"\nAfter append(5)")
    print(*typed_array)

    typed_array.insert(1, 15)
    print(f"\nAfter insert 15 at index 1")
    print(*typed_array)

    typed_array.pop()
    print(f"\nAfter pop")
    print(*typed_array)

    typed_array.remove(15)
    print(f"\nAfter remove(15)")
    print(*typed_array)

# Simulation of static array
import ctypes

class StaticArray:
    def __init__(self, size):
        self.size = size
        self.count = 0
        # Create a contiguous block of memory for 'size' elements
        ArrayType = ctypes.py_object * size
        self.array = ArrayType()
    
    def __len__(self):
        return self.count
    
    def __getitem__(self, index):
        if not 0 <= index < self.count:
            raise IndexError('Index out of bounds')
        return self.array[index]
    
    def append(self, item):
        if self.count >= self.size:
            raise OverflowError('Array is full!')
        self.array[self.count] = item
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            raise IndexError('Array is empty!')
        self.array[self.count - 1] = None
        self.count -= 1

    def __str__(self):
        items = [str(self.array[i]) for i in range(self.count)]
        return '[' + ', '.join(items) + ']'

def demo_static_array():
    print("\n--- Static Array Simulation ---")
    cust_arr = StaticArray(3)
    cust_arr.append("A")
    cust_arr.append("B")
    print(f"\nCustom array: {cust_arr}")

    cust_arr.append("C")
    print(f"\nAfter append C: {cust_arr}")

    try:
        cust_arr.pop()
        print(f"\nAfter pop: {cust_arr}")

        cust_arr.append("D")
        print(f"\nAfter append D: {cust_arr}")

        cust_arr.append("E")
        print(f"\nAfter append E: {cust_arr}")

    except OverflowError as e:
        print(f"\nError caught: {e}")


if __name__ == "__main__":
    demo_python_list()
    demo_python_array_module()
    demo_static_array()
            
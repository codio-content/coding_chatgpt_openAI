import importlib.util

def test_reverse_string():
    # Load the external python script
    spec = importlib.util.spec_from_file_location("module.name", "test2.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Use the function from the external script
    reverse_string_function = module.reverse_string

    assert reverse_string_function("Hello, World!") == "!dlroW ,olleH", "Test Case 1 Failed"
    assert reverse_string_function("Python") == "nohtyP", "Test Case 2 Failed"
    assert reverse_string_function("OpenAI") == "IAnepO", "Test Case 3 Failed"
    assert reverse_string_function("") == "", "Test Case 4 Failed"
    print("All test cases pass")

if __name__ == "__main__":
    test_reverse_string()

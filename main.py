"""
The main script for gRPC in Python course
"""


def print_hi(name: str) -> None:
    """
    Print hi to someone
    :param name: The name of the person to print hi
    :type name: str
    :return: None
    :rtype: NoneType
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# To generate the rides_pb2.py file from rides.proto, use the command:
# protoc --python_out=. rides.proto

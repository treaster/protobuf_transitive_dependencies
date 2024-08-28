from typing import reveal_type

from example.example_pb2 import ExampleWithDep


def test_protobuf_import():
    msg = ExampleWithDep()
    assert msg

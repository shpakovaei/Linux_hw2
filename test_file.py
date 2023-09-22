import cmd

from cheks import func
import pytest

folderin = "/home/user/seminar2/test"
folderout = "/home/user/seminar2/out"
folderext = "/home/user/seminar2/folder1"

def test_step1():
    assert func(f"cd {folderin}; 7z a {folderout}/arh1", "Everything is Ok"), "test_step1 FAIL"

def test_step2():
    assert func(f"cd {folderout}; 7z d arh1.7z", "Everything is Ok"), "test_step2 FAIL"

def test_step3():
    assert func(f"cd {folderext}; 7z u {folderout}/arh1", "Everything is Ok"), "test_step3 FAIL"

def test_step4():
    # Test listing files in the archive
    assert func(f"cd {folderout}; 7z l arx2.7z", "Everything is Ok"), "test_step4 FAIL"

def test_step5():
    # Test extracting with preserving paths
    assert func(f"cd {folderout}; 7z x arx2.7z {folderext}", "Everything is Ok"), "test_step5 FAIL"


if __name__ == '__min__':
    pytest.main(["-vv"])

import pytest

def test_1_passed():
	assert 1==1

def test_2_failed():
	assert 1==2

def test_3_passed():
	print("SUCCESS!!!")
	assert 1==1
	
def test_4_passed():
	for _ in range(1):
		print(f"loops {_}")
	assert 1==1

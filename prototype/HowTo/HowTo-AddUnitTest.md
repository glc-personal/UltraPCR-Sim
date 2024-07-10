# HowTo-AddUnitTest

## Summary
To add a unit test, for this project, create a python source file prefixed by *test_*.
Place this test within *tests/units*. For example, a unit test for the SPartition class
could be named *test_spartion.py*. Then the test function within this source file should
also be prefaced with *test_*.

## Performing the Unit Test
To perform the tests (be it unit or integration tests with pytest), at the tests level
execute the following:
```
pytest tests
```
If unit tests are the only piece of interest, then move into tests or stay at tests and 
execute the following:
```
pytest units
```
or for the latter
```
pytest tests/units
```

import sys

import friendly_traceback

# TODO: make sure that all these cases are captured in the documentation

# Need to add more cases, ensuring that correct object is always identified

# a = [1, 2, 3]
# b = 3, 4, 5

# b[0] > a.max  --> max(a)
# b.min == a[0]  --> min(b)
# a.length  --> len(a)
# a.len --> len(a)

# a.b -> a, b ?


def test_Generic():
    # Generic - no additional explanation
    class A:
        pass

    try:
        A.x  # testing type
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: type object 'A' has no attribute 'x'" in result
    if friendly_traceback.get_lang() == "en":
        assert "The object `A` has no attribute" in result
    return result, message


def test_Generic_different_frame():
    class A:
        attr = 1

    def f():
        class A:
            attr2 = 1
        return A()

    a = f()
    try:
        a.attr
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()

    assert "AttributeError: 'A' object has no attribute 'attr'" in result
    if friendly_traceback.get_lang() == "en":
        assert "The object `a` has no attribute" in result
        assert "Did you mean `attr2`" in result
    return result, message


def test_Generic_instance():
    class A:
        pass
    a = A()
    try:
        a.x
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: 'A' object has no attribute 'x'" in result
    if friendly_traceback.get_lang() == "en":
        assert "The object `a` has no attribute" in result
    return result, message


def test_Object_attribute_typo():
    #
    try:
        a = [1, 2, 3]
        a.appendh(4)
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: 'list' object has no attribute 'appendh'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `append`" in result
    return result, message


def test_Use_builtin():
    #
    try:
        a = [1, 2, 3]
        a.length()
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: 'list' object has no attribute 'length'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `len(a)`" in result
    return result, message


def test_Use_synonym():
    #
    try:
        a = [1, 2, 3]
        a.add(4)
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: 'list' object has no attribute 'add'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `append`" in result
    return result, message



def test_Module_attribute_typo():
    import string

    try:
        string.ascii_lowecase
    except AttributeError as e:
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: module 'string' has no attribute 'ascii_lowecase'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `ascii_lowercase`" in result

    import math

    try:
        math.cost
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: module 'math' has no attribute 'cost'" in result
    if friendly_traceback.get_lang() == "en":
        assert (
            "Instead of writing `math.cost`, perhaps you meant to write one of"
            in result
        )
    assert "cos, cosh" in result or "cosh, cos" in result
    assert not "acosh" in result
    return result, message


def test_Shadow_stdlib_module():
    import turtle

    try:
        turtle.Pen
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "AttributeError: module 'turtle' has no attribute 'Pen'" in result
    if friendly_traceback.get_lang() == "en":
        assert (
            "There is also a module named `turtle` in Python's standard library."
            in result
        )
    return result, message


def test_Nonetype():
    a = None
    try:
        a.b
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "'NoneType' object has no attribute 'b'" in result
    if friendly_traceback.get_lang() == "en":
        assert "for a variable whose value is `None`" in result

    return result, message


def test_Perhaps_comma():
    import sys
    abcd = "hello"
    defg = "world"

    # fmt: off
    try:
        a = [abcd
        .defg]
    # fmt: on
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()

    if sys.version_info >= (3, 10):
        result = "            Skipped test"
        return result, message
    assert "'str' object has no attribute 'defg'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean to separate object names by a comma" in result
    return result, message


def test_Builtin_function():
    text = 'Hello world!'
    try:
        len.text
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "'builtin_function_or_method'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `len(text)`" in result
    return result, message


def test_Builtin_module_with_no_file():
    """Issue 116"""
    import sys

    try:
        sys.foo
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "module 'sys' has no attribute 'foo'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Python tells us" in result
    return result, message


def test_Using_slots():
    """Issue 141"""

    class F:
        __slots__ = ["a"]

    f = F()
    try:
        f.b = 1
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()

    assert "'F' object has no attribute 'b'" in result
    if friendly_traceback.get_lang() == "en":
        assert "object `f` uses `__slots__`" in result
    return result, message


def test_Read_only():

    class F:
        __slots__ = ["a"]
        b = 2

    f = F()
    try:
        f.b = 1
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()

    assert "'F' object attribute 'b' is read-only" in result
    if friendly_traceback.get_lang() == "en":
        assert "The only attribute of `f` whose value can be changed is" in result
    return result, message


def test_Tuple_by_accident():
    something = "abc",  # note trailing comma
    try:
        something.upper()
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()

    assert "'tuple' object has no attribute 'upper'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you write a comma" in result

    return result, message


def test_Attribute_from_other_module():
    import math
    import keyword

    try:
        keyword.pi
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")

    result = friendly_traceback.get_output()
    assert "module 'keyword' has no attribute 'pi'" in result
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean `math`?" in result

    import cmath
    try:
        keyword.pi
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")

    result = friendly_traceback.get_output()
    if friendly_traceback.get_lang() == "en":
        assert "Did you mean one of the following modules:" in result

    return result, message


def test_Use_join_with_str():
    try:
        a = ['a', '2'].join('abc') + ['b', '3'].join('\n')
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")

    result = friendly_traceback.get_output()
    assert "'list' object has no attribute 'join'" in result
    if friendly_traceback.get_lang() == "en":
        assert "something like `'abc'.join(['a', '2'])`" in result
    return result, message


def test_Circular_import():
    from friendly_traceback.runtime_errors import stdlib_modules
    stdlib_modules.names.add("my_turtle1")
    try:
       import my_turtle1
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")

    result = friendly_traceback.get_output()
    # Different messages for python < 3.8
    assert ( "partially initialized module 'my_turtle1'" in result or
             "module 'my_turtle1' has no attribute 'something'" in result)
    if friendly_traceback.get_lang() == "en":
        assert "import a module with the same name" in result
        assert "from Python's standard library" in result
    stdlib_modules.names.pop()
    return result, message

def test_Circular_import_b():
    try:
        import circular_c
    except AttributeError as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")

    result = friendly_traceback.get_output()

    assert (
        "module 'circular_c' has no attribute 'something'" in result or
        "partially initialized module 'circular_c' has no attribute 'something'"
        in result
    )
    if friendly_traceback.get_lang() == "en":
        assert "have a circular import." in result
    return result, message


if __name__ == "__main__":
    print(test_Generic()[0])

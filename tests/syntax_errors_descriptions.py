"""In this file, descriptions is a dict whose keys are the names of
Python files that raise a SyntaxError (or subclass) when they are imported.
This is done from the file
/tests/syntax/catch_syntax_error.py

Here is the meaning of the various dict keys:

title/"title" is the heading that should appear in the documentation for
        this particular case.
        
version_dependent/"version dependent" indicates that an exception will be raised but 
   that the explanation provided by Friendly-traceback
   might vary depending on the Python version used.
   The value corresponding to this key is a list of text fragments,
   at least one of which should appear in the explanation given by Friendly-traceback.

   In this case, in_cause/"in cause" (mentioned below) is usually set to "ignored"
   as catch_syntax_error.py needs a value for all cases.

Note that, in some cases, a SyntaxError will not be raised by a given Python version.
In this case, we delete the entry at the very bottom of this file.

When the basic explanation is the same (or similar enough) for all Python versions,
which is generally the case, the following is used instead:

in_cause/"in cause" is some text that should be found in the explanation provided by
        Friendly-traceback when importing this file.

also_in_cause/"also in cause" is a list of text fragments that should
    also be found in the explanation.  Note that this can sometimes be version dependent
    in which case a change is made at the end of the file.

not_in_cause/"not in cause" is a list of text fragments that should
    not be found in the explanation.
"""
import sys

title = "title"
version_dependent = "version dependent"
in_cause = "in cause"
also_in_cause = "also in cause"
not_in_cause = "not in cause"

no_slash = "Function definitions cannot include the symbol `/` in this Python version"

descriptions = {
    "and_in_import_statement": {
        in_cause: "only be used for boolean expressions",
        title: "Using 'and' in import statement",
    },
    "and_in_import_statement_2": {
        in_cause: "only be used for boolean expressions",
        title: "Using 'and' after comma in import statement",
    },
    "annotated_name_global": {
        in_cause: "It cannot be declared to be a global variable.",
        title: "Annotated name cannot be global",
    },
    "as_instead_of_comma_in_import": {
        in_cause: "and rename it using the Python keyword `as`",
        title: "Incorrect use of 'from module import ... as ...",
    },
    "assign_instead_of_equal": {
        in_cause: "Perhaps you needed `==`",
        "version_dependent": ["`:=` instead of `=`.", "instead of `=`."],
        title: "Assign instead of equal (or walrus).",
    },
    "assign_name_before_global_1": {
        in_cause: "before declaring it as a global variable.",
        title: "Name assigned prior to global declaration",
    },
    "assign_name_before_global_2": {
        in_cause: "You used the variable `var`",
        title: "Name used prior to global declaration",
    },
    "assign_name_before_nonlocal_1": {
        in_cause: "before declaring it as a nonlocal variable.",
        title: "Name used prior to nonlocal declaration",
    },
    "assign_name_before_nonlocal_2": {
        in_cause: "You assigned a value to the variable `s`",
        title: "Name assigned prior to nonlocal declaration",
    },
    "assign_to_conditional": {
        in_cause: "conditional expression instead of the name of a variable",
        title: "Assign to conditional expression",
    },
    "assign_to_debug": {
        in_cause: "`__debug__` is a constant in Python",
        title: "Assignment to keyword (__debug__)",
    },
    "assign_to_debug2": {
        in_cause: "`__debug__` is a constant in Python",
        title: "Assignment to keyword (__debug__)",
    },
    "assign_to_ellipsis": {
        in_cause: "The ellipsis symbol `...` is a constant in Python",
        title: "Assignment to Ellipsis symbol",
    },
    "assign_to_f_string": {
        in_cause: "expression that has the f-string",
        title: "Cannot assign to f-string",
    },
    "assign_to_function_call_1": {
        in_cause: "function call and is not simply the name of a variable",
        title: "Cannot assign to function call: single = sign",
        also_in_cause: ["len('a')"],
    },
    "assign_to_function_call_2": {
        in_cause: "function call and is not simply the name of a variable",
        title: "Cannot assign to function call: two = signs",
        also_in_cause: ["^^^^^^^^^^^^"],
    },
    "assign_to_function_call_3": {
        in_cause: "function call and is not simply the name of a variable",
        title: "Cannot assign to function call: continues on second line",
        also_in_cause: ["^^^^^^^-->"],
    },
    "assign_to_generator": {
        in_cause: "generator expression instead of the name of a variable",
        title: "Assign to generator expression",
    },
    "assign_to_literal_dict": {
        in_cause: "is or includes an actual object of type `dict`",
        title: "Cannot assign to literal - 4",
    },
    "assign_to_literal_int": {
        in_cause: "is or includes an actual object of type `int`",
        title: "Cannot assign to literal int",
        also_in_cause: ["Perhaps you meant to write"],
    },
    "assign_to_literal_int_2": {
        in_cause: "is or includes an actual object of type `int`",
        title: "Cannot assign to literal int - 2",
    },
    "assign_to_literal_int_3": {
        in_cause: "is or includes an actual object",
        title: "Cannot assign to literal - 5",
    },
    "assign_to_literal_set": {
        in_cause: "is or includes an actual object of type `set`",
        title: "Cannot assign to literal - 3",
    },
    "assign_to_keyword_def": {  # = sign is flagged
        in_cause: "assign a value to the Python keyword `def`",
        title: "Assign to keyword def",
    },
    "assign_to_keyword_else": {  # else is flagged
        in_cause: "assign a value to the Python keyword `else`",
        title: "Assign to keyword else",
    },
    "assign_to_keyword_none": {
        in_cause: "`None` is a constant in Python",
        title: "Assignment to keyword (None)",
    },
    "assign_to_operation": {
        in_cause: "only used to assign a value to a variable",
        title: "Assign to math operation",
    },
    "assign_to_yield_expression": {
        in_cause: "You wrote an expression that includes the `yield` keyword",
        title: "Assign to yield expression",
        also_in_cause: ["You cannot assign a value to such an expression."],
    },
    "assignment_expression_cannot_rebind": {
        version_dependent: [
            "The augmented assignment operator is not allowed",
            "a comprehension to assign a value to the iteration variable",
        ],
        in_cause: "ignored",
        title: "Augmented assignment inside comprehension",
    },
    "assignment_expression_cannot_rebind_2": {
        version_dependent: [
            "The augmented assignment operator is not allowed",
            "a comprehension to assign a value to the iteration variable",
        ],
        in_cause: "ignored",
        title: "Augmented assignment inside comprehension - inner loop",
    },
    "async_def_missing_parens": {
        in_cause: "Did you forget parentheses?",
        title: "def: missing parentheses",
    },
    "augmented_assignment_to_literal": {
        version_dependent: [
            "walrus operator",
            "the walrus operator, with literals like",
        ],
        in_cause: "ignored",
        title: "Augmented assignment to literal",
    },
    "augmented_assigment_with_true": {
        version_dependent: ["walrus operator", "`True` is a constant in Python"],
        in_cause: "ignored",
        title: "Walrus/Named assignment depending on Python version",
    },
    "backslash_instead_of_slash": {
        in_cause: "Did you mean to divide",
        title: "Backslash instead of slash",
    },
    "bracket_instead_of_paren": {
        in_cause: "You used square brackets, `[...]` instead of parentheses.",
        title: "Brackets instead of parentheses",
    },
    "break_outside_loop": {
        in_cause: "The Python keyword `break` can only be used",
        title: "break outside loop",
    },
    "cannot_assign_to_attribute_here" : {
        in_cause: "You likely used an assignment operator `=` instead of an equality operator `==`",
        title: "Cannot assign to attribute here.",
    },
    "cannot_guess_the_cause": {
        in_cause: "Currently, I cannot guess the likely cause of this error.",
        title: "Cannot guess the cause",
    },
    "cannot_use_star": {
        in_cause: "The star operator",
        title: "Cannot use star operator",
    },
    "cannot_use_double_star": {
        in_cause: "The double star operator",
        title: "Cannot use double star operator",
    },
    "class_missing_name": {
        in_cause: "A class needs a name.",
        title: "Missing class name",
    },
    "comprehension_missing_tuple_paren": {
        in_cause: "and forgot to include parentheses around tuples",
        title: "Missing () for tuples in comprehension",
    },
    "comprehension_with_condition_no_else": {
        version_dependent: [
            "`else some_value` clause was expected after the `if` expression",
            "The correct order depends if there is an `else` clause or not",
        ],
        in_cause: "ignored",
        title: "Comprehension with condition (no else)",
    },
    "comprehension_with_condition_with_else": {
        in_cause: "The correct order depends if there is an `else` clause or not",
        title: "Comprehension with condition (with else)",
    },
    "continue_outside_loop": {
        in_cause: "The Python keyword `continue` can only be used",
        title: "continue outside loop",
    },
    "copy_pasted_code": {
        in_cause: "copy-pasted code from an interactive interpreter",
        title: "Copy/paste from interpreter",
        also_in_cause: ["`>>>`"],
    },
    "copy_pasted_code_2": {
        in_cause: "copy-pasted code from an interactive interpreter",
        title: "Copy/paste from interpreter - 2",
        also_in_cause: ["`...`"],
    },
    "debug_fstring_not_supported": {  # not allowed prior to Python 3.8
        in_cause: "You are likely using a 'debug' syntax of f-strings",
        title: "Debug-feature of f-string not supported",
    },
    "def_arg_after_kwarg": {
        in_cause: "Positional arguments must come before keyword argument",
        title: "def: positional arg after kwargs",
    },
    "def_bare_star_arg": {
        in_cause: "replace `*` by either `*arguments` or ",
        title: "def: named arguments must follow bare *",
    },
    "def_code_block": {
        in_cause: "tried to define a function and did not",
        title: "def: misused as code block",
    },
    "def_code_block_2": {
        in_cause: "tried to define a function or method and did not",
        title: "def: misused as code block - 2",
    },
    "def_dotted_argument": {
        in_cause: "You cannot use dotted names as function arguments.",
        title: "Dotted name as function argument",
        also_in_cause: ["Did you mean to write a comma?"],
    },
    "def_dotted_argument_2": {
        in_cause: "You cannot use dotted names as function arguments.",
        title: "Dotted name as function argument",
        not_in_cause: ["Did you mean to write a comma?"],
    },
    "def_dotted_function_name": {
        in_cause: "You cannot use dots in function names.",
        title: "Dotted function name",
    },
    "def_dict_as_arg": {
        in_cause: "You cannot have any explicit dict or set as function arguments",
        title: "def: dict as argument",
    },
    "def_duplicate_arg": {
        in_cause: "argument should appear only once in a function definition",
        title: "def: arguments must be unique in function definition",
    },
    "def_extra_semi_colon": {
        in_cause: "Did you write something by mistake after the colon",
        title: "def: semicolon after colon",
    },
    "def_extra_comma": {
        in_cause: "Did you mean to write `,`",
        title: "def: extra comma",
    },
    "def_forward_slash_1": {
        version_dependent: [
            no_slash,
            "You have unspecified keyword arguments that appear before",
        ],
        in_cause: "ignored",
        title: "def: unspecified keywords before /",
    },
    "def_forward_slash_2": {
        version_dependent: [
            no_slash,
            "When they are used together, `/` must appear before `*`",
        ],
        in_cause: "ignored",
        title: "def: / before star",
    },
    "def_forward_slash_3": {
        version_dependent: [
            no_slash,
            "`*arg` must appear after `/` in a function definition",
        ],
        in_cause: "ignored",
        title: "def: / before star arg",
    },
    "def_forward_slash_4": {
        version_dependent: [
            no_slash,
            "You can only use `/` once in a function definition",
        ],
        in_cause: "ignored",
        title: "def: / used twice",
    },
    "def_function_name_invalid": {
        in_cause: "The name of a function must be a valid Python identifier",
        title: "def: non-identifier as a function name",
    },
    "def_function_name_string": {
        in_cause: "use a string as a function name",
        title: "def: using a string as a function name",
    },
    "def_keyword_as_arg_1": {
        in_cause: "as an argument in the definition of a function",
        title: "def: keyword cannot be argument in def - 1",
    },
    "def_keyword_as_arg_2": {
        in_cause: "as an argument in the definition of a function",
        title: "def: keyword cannot be argument in def - 2",
    },
    "def_keyword_as_arg_3": {
        in_cause: "as an argument in the definition of a function",
        title: "def: keyword cannot be argument in def - 3",
    },
    "def_keyword_as_arg_4": {
        in_cause: "as an argument in the definition of a function",
        title: "def: keyword cannot be argument in def - 4",
    },
    "def_keyword_as_name": {
        in_cause: "You tried to use the Python keyword",
        title: "def: Python keyword as function name",
    },
    "def_list_as_arg_1": {
        in_cause: "You cannot have explicit lists as function arguments",
        title: "def: list as argument - 1",
    },
    "def_list_as_arg_2": {
        in_cause: "You cannot have explicit lists as function arguments",
        title: "def: list as argument - 2",
    },
    "def_missing_colon": {
        version_dependent: [
            "but forgot to add a colon `:` at the end",
            "Did you forget to write a colon",
        ],
        in_cause: "ignored",
        title: "def: missing colon",
    },
    "def_missing_comma": {
        in_cause: "Did you forget a comma",
        title: "def: missing comma between function args",
    },
    "def_missing_parens": {
        in_cause: "Did you forget parentheses?",
        title: "def: missing parentheses",
    },
    "def_missing_parens_2": {
        in_cause: "Did you forget parentheses?",
        title: "def: missing parentheses around arguments",
    },
    "def_missing_name": {
        in_cause: "forgot to name your function",
        title: "def: missing function name",
    },
    "def_name_is_parameter_and_global": {
        in_cause: "is a variable defined outside a function.",
        title: "def: name is parameter and global",
    },
    "def_non_default_after_default": {
        in_cause: "define functions with only positional arguments",
        title: "def: non-default argument follows default argument",
    },
    "def_number_as_arg": {
        in_cause: "You used a number as an argument",
        title: "Single number used as arg in function def",
    },
    "def_operator_after_2star": {
        in_cause: "The `**` operator needs to be followed by an identifier",
        title: "Operator after ``**``",
    },
    "def_operator_instead_of_comma": {
        in_cause: "Did you mean to write a comma",
        title: "def: operator instead of comma",
    },
    "def_operator_instead_of_equal": {
        in_cause: "Did you mean to write an equal sign",
        title: "def: operator instead of equal",
    },
    "def_operator_instead_of_name": {
        in_cause: "If you replace it by a unique variable name",
        title: "def: operator instead of name",
    },
    "def_positional_after_keyword_arg": {
        in_cause: "call functions with only positional arguments",
        title: "def: positional argument follows keyword argument",
    },
    "def_semi_colon_instead_of_colon": {
        in_cause: "You wrote `;` instead of a colon",
        title: "def: semicolon instead of colon",
    },
    "def_set_as_arg": {
        in_cause: "You cannot have any explicit dict or set as function arguments",
        title: "def: set as argument",
    },
    "def_star_arg_before_slash": {
        version_dependent: [
            "This symbol can only be used with Python versions",
            "`*arg` must appear after `/` ",
        ],
        in_cause: "ignored",
        title: "def: ``*arg`` before /",
    },
    "def_star_used_only_once": {
        in_cause: "can only use `*` once in a function definition",
        title: "def: ``*`` used twice",
        also_in_cause: ["`*arg`"],
    },
    "def_star_used_only_once_1": {
        in_cause: "can only use `*` once in a function definition",
        title: "def: ``*`` used twice",
    },
    "def_star_used_only_once_2": {
        in_cause: "can only use `*` once in a function definition",
        title: "def: ``*`` used twice",
        also_in_cause: ["`*arg`", "`*other`"],
    },
    "def_star_after_2star": {
        in_cause: "can only use `*` once in a function definition",
        title: "def: ``*`` after ``**``",
        also_in_cause: ["`**kw`"],
        not_in_cause: ["`*` operator"],
    },
    "def_star_after_2star_2": {
        in_cause: "can only use `*` once in a function definition",
        title: "def: ``*`` after ``**``",
        also_in_cause: ["`**kw`", "`*` operator"],
    },
    "def_string_as_arg": {
        in_cause: "You used a string as an argument",
        title: "Single string used as arg in function def",
    },
    "def_tuple_as_arg_1": {
        in_cause: "You cannot have explicit tuples as function arguments.",
        title: "def: tuple as function argument",
    },
    "def_tuple_as_arg_2": {
        in_cause: "You cannot have explicit tuples as function arguments.",
        title: "def: tuple as function argument - 2",
    },
    "del_paren_star_1": {
        in_cause: "The star operator `*`",
        title: "Deleting star expression - 1",
        also_in_cause: [
            "You can only delete names of objects, or items in mutable containers"
        ],
    },
    "del_paren_star_2": {
        in_cause: "The star operator `*`",
        title: "Deleting star expression - 2",
        also_in_cause: [
            "You can only delete names of objects, or items in mutable containers"
        ],
    },
    "delete_constant_keyword": {
        in_cause: "You cannot delete the constant",
        title: "Cannot delete a constant",
        also_in_cause: [
            "You can only delete names of objects, or items in mutable containers"
        ],
    },
    "delete_expression": {
        in_cause: "You cannot delete the expression",
        title: "Cannot delete expression",
        also_in_cause: [
            "You can only delete names of objects, or items in mutable containers"
        ],
    },
    "delete_function_call": {
        in_cause: "instead of deleting the function's name",
        title: "Cannot delete function call",
    },
    "delete_named_expression": {
        in_cause: "You cannot delete the named expression",
        version_dependent: [
            "You cannot delete the named expression",
            "walrus operator",
        ],
        title: "Cannot delete named expression",
    },
    "delete_names_or_items": {
        in_cause: "You can only delete names of objects, or items in mutable containers",
        title: "Delete only names or items",
    },
    "delete_string_literal": {
        in_cause: "You cannot delete the literal",
        title: "Deleting string literal",
        also_in_cause: [
            "You can only delete names of objects, or items in mutable containers"
        ],
    },
    "dict_value_missing_1": {
        in_cause: "wrote a dict key without writing the corresponding value",
        title: "Value missing in dict - 1",
    },
    "dict_value_missing_2": {
        in_cause: "Perhaps you forgot to write a value after a colon.",
        title: "Value missing in dict - 2",
    },
    "dict_value_missing_3": {
        in_cause: "wrote a dict key without writing the corresponding value",
        title: "Value missing in dict - 3",
    },
    "dict_value_missing_4": {
        in_cause: "Perhaps you forgot to write a value after a colon.",
        title: "Value missing in dict - 4",
    },
    "different_operators_in_a_row": {
        in_cause: "You cannot have these two operators, `*` and `/`",
        title: "Different operators in a row",
    },
    "dot_before_paren": {
        in_cause: "dot `.` followed by `(`",
        title: "Dot followed by parenthesis",
    },
    "duplicate_token": {
        in_cause: "wrote `,` twice in a row by mistake",
        title: "Extra token",
    },
    "elif_not_matching_if": {
        in_cause: "The `elif` keyword does not begin a code block that matches",
        title: "elif with no matching if",
    },
    "ellipsis_extra_dot": {
        in_cause: "It looks like you meant to write `...` but added an extra `.` by mistake",
        title: "Ellipsis written with extra dot"
    },
    "else_no_matching_statement": {
        in_cause: "The `else` keyword does not begin a code block that matches",
        title: "else with no matching statement",
    },
    "else_if_instead_of_elif": {
        in_cause: "wrote `else if` instead",
        title: "Write elif, not else if",
    },
    "elseif_instead_of_elif": {
        in_cause: "wrote `elseif` instead",
        title: "Write elif, not elseif",
    },
    "eol_string_literal": {
        in_cause: "ended the string with another quote",
        title: "EOL while scanning string literal",
    },
    "equal_sign_instead_of_colon": {
        in_cause: "used an equal sign `=` instead of a colon `:`",
        title: "Used equal sign instead of colon",
    },
    "except_multiple_exceptions": {
        in_cause: "with multiple exception types.",
        title: "Parens around multiple exceptions",
    },
    "extra_token": {in_cause: "wrote `==` by mistake", title: "Extra token"},
    "f_string_assign_value": {  # Python < 3.8
        in_cause: "You are likely trying to assign a value within an f-string.",
        title: "Cannot assign a value within an fstring",
    },
    "f_string_binary": {
        in_cause: "`bf` is an illegal string prefix.",
        title: "Binary f-string not allowed",
    },
    "f_string_curly_not_allowed": {
        in_cause: "You have written an f-string which has an unmatched `}`",
        title: "f-string: closing } not allowed",
    },
    "f_string_expected_curly": {
        in_cause: "You have written an f-string which has an unmatched `{`.",
        title: "f-string: missing closing }",
    },
    "f_string_unterminated": {
        in_cause: "you have another string, which starts with either",
        title: "f-string: unterminated string",
    },
    "f_string_with_backslash": {
        in_cause: "you can replace the part that contains a backslash",
        title: "f-string with backslash",
    },
    "for_missing_terms": {
        in_cause: "A `for` loop is an iteration over a sequence",
        title: "Missing terms in for statement",
    },
    "future_braces": {
        in_cause: "from __future__ import braces",
        title: "Not a chance!",
    },
    "future_import_star": {
        in_cause: "you must import specific named features",
        title: "Do not import * from __future__",
    },
    "future_must_be_first": {
        in_cause: "It must appear at the beginning of the file.",
        title: "__future__ at beginning",
    },
    "future_typo": {
        in_cause: "Did you mean `division`",
        title: "Typo in __future__",
    },
    "future_unknown": {
        in_cause: "print_function",
        title: "Unknown feature in __future__",
    },
    "generator_expression_parens": {
        in_cause: "must add parentheses enclosing",
        title: "Parenthesis around generator expression",
    },
    "hyphen_instead_of_underscore": {
        in_cause: "Did you mean `a_b`",
        title: "Space between names",
    },
    "if_missing_condition": {
        in_cause: "An `if` statement requires a condition",
        title: "Missing condition in if statement",
    },
    "imaginary_i": {
        in_cause: "Did you mean `3.0j`",
        title: "use j instead of i",
    },
    "import_from": {
        in_cause: "from turtle import pen",
        title: "Import inversion: import X from Y",
    },
    "indentation_error_1": {
        in_cause: "expected to begin a new indented block",
        title: "IndentationError: expected an indented block",
    },
    "indentation_error_2": {
        in_cause: "is more indented than expected",
        title: "IndentationError: unexpected indent",
    },
    "indentation_error_3": {
        in_cause: "is less indented than expected",
        title: "IndentationError: unindent does not match ...",
    },
    "indentation_error_4": {
        in_cause: "meant to include a continuation character",
        title: "IndentationError: missing continuation line",
    },
    "integer_with_leading_zero_1": {
        in_cause: "Did you mean `0o1`",
        title: "Forgot 'o' for octal",
    },
    "integer_with_leading_zero_2": {
        in_cause: "Did you mean `123_456`",
        title: "Integer with leading zeros",
    },
    "invalid_character_in_identifier": {
        in_cause: "unicode character",
        title: "Invalid character in identifier",
    },
    "invalid_decimal_literal1": {
        in_cause: "Valid names cannot begin with a number",
        title: "Invalid decimal literal - 1",
    },
    "invalid_encoding": {
        in_cause: "The encoding of the file was not valid.",
        title: "Invalid encoding",
    },
    "invalid_hexadecimal": {
        in_cause: "Did you made a mistake in writing an hexadecimal integer",
        title: "Invalid hexadecimal number",
    },
    "invalid_identifier": {
        in_cause: "Valid names cannot begin with a number",
        title: "Valid names cannot begin with a number",
        not_in_cause: ["complex"],
    },
    "invalid_identifier_2": {
        in_cause: "Perhaps you forgot a multiplication operator",
        title: "Valid names cannot begin with a number - 2",
        not_in_cause: ["complex"],
    },
    "invalid_identifier_3": {
        in_cause: "Perhaps you forgot a multiplication operator",
        title: "Valid names cannot begin with a number - 3",
        also_in_cause: ["complex"],
    },
    "invalid_identifier_4": {
        in_cause: "Valid names cannot begin with a number",
        title: "Valid names cannot begin with a number - 4",
        not_in_cause: ["multiplication operator"],
    },
    "invalid_identifier_5": {
        in_cause: "Valid names cannot begin with a number",
        title: "Valid names cannot begin with a number - 5",
        also_in_cause: ["complex", "multiplication operator"],
    },
    "invalid_keyword_argument": {
        in_cause: "where `invalid` is not a valid ",
        title: "Keyword can't be an expression",
    },
    "invalid_keyword_argument_2": {
        in_cause: "You cannot assign a value to `True`.",
        title: "Named argument can't be a Python keyword",
    },
    "invalid_non_printable_char": {
        in_cause: "Your code contains the invalid non-printable character",
        title: "Invalid non printable character"
    },
    "invalid_octal": {
        in_cause: "Did you made a mistake in writing an octal integer",
        title: "Invalid octal number",
    },
    "inverted_operators": {
        in_cause: "Did you write operators in an incorrect order?",
        title: "Inverted operators 1",
    },
    "inverted_operators_2": {
        in_cause: "Did you write operators in an incorrect order?",
        title: "Inverted operators 2",
        also_in_cause: ["all the syntax errors in the code you wrote"],
    },
    "iteration_unpacking_in_comprehension": {
        in_cause: "You cannot use the `*` operator to unpack the iteration variable",
        title: "Iteration variable unpacking in comprehension",
    },
    "keyword_arg_repeated": {
        in_cause: "keyword argument should appear only once in a function call",
        title: "Keyword arg only once in function call",
    },
    "keyword_as_attribute": {
        in_cause: "keyword `pass` as an attribute",
        title: "Keyword as attribute",
    },
    "lambda_with_parens": {
        in_cause: "`lambda` does not allow parentheses ",
        title: "lambda with parentheses around arguments",
    },
    "lambda_with_tuple_argument": {
        in_cause: "You cannot have explicit tuples as arguments.",
        title: "lambda with tuple as argument",
    },
    "literal_in_for_loop": {
        in_cause: "where `...` must contain only identifiers",
        title: "Assign to literal in for loop",
    },
    "missing_code_block": {  # May differ depending on Python version
        version_dependent: [
            "expected an indented block",
            "it reached the end of the file and expected more content.",
        ],
        in_cause: "it reached the end of the file and expected more content.",
        title: "IndentationError/SyntaxError depending on version",
    },
    "missing_code_block_2": {
        version_dependent: [
            "unexpected EOF while parsing",
            # do not include 'indented' below as this results in the test
            # assuming that an Indention error is raised, which is not
            # true for earlier Python versions.
            # Also do not include line number shown in the message
            # as it can be off by 1 on Github automated tests for this case.
            "identified above was expected to begin a",
        ],
        in_cause: "ignored",
        title: "IndentationError/SyntaxError depending on version - 2",
    },
    "missing_colon_if": {
        version_dependent: [
            "Did you forget a colon",
            "`if` but forgot to add a colon `:`",
        ],
        in_cause: "ignored",
        title: "Missing colon - if",
    },
    "missing_colon_while": {
        version_dependent: ["Did you forget a colon", "wrote a `while` loop but"],
        in_cause: "ignored",
        title: "Missing colon - while",
    },
    "missing_comma_in_dict": {
        in_cause: "forgot a comma",
        title: "Missing comma in a dict",
    },
    "missing_comma_in_dict_2": {
        in_cause: "I am guessing that you forgot a comma between two strings",
        title: "Missing comma between strings in a dict",
    },
    "missing_comma_in_list": {
        in_cause: "The following lines of code",
        title: "Missing comma in a list",
    },
    "missing_comma_in_set": {
        in_cause: "The following lines of code",
        title: "Missing comma in a set",
    },
    "missing_comma_in_tuple": {
        in_cause: "The following lines of code",
        title: "Missing comma in a tuple",
    },
    "missing_in_with_for": {
        in_cause: "Did you forget to write `in`?",
        title: "For loop missing 'in' operator",
    },
    "missing_parens_for_range": {
        in_cause: "you forgot to use to use parenthesis with `range`",
        title: "Missing parenthesis for range",
    },
    "misspelled_keyword": {
        in_cause: "if i in range(3)",
        title: "Misspelled Python keyword",
    },
    "name_is_global_and_nonlocal": {
        in_cause: "You declared `xy` as being both a global and nonlocal",
        title: "Name is global and nonlocal",
    },
    "name_is_param_and_nonlocal": {
        in_cause: "You used `x` as a parameter for a function",
        title: "Name is parameter and nonlocal",
    },
    "no_binding_for_nonlocal": {
        in_cause: "nonlocal variable but it cannot be found.",
        title: "nonlocal variable not found",
    },
    "nonlocal_at_module": {
        in_cause: "You used the nonlocal keyword at a module level",
        title: "nonlocal variable not found at module level",
    },
    "operator_twice_in_a_row": {
        in_cause: "You cannot have write the same operator, `**`, twice in a row",
        title: "Same operator twice in a row",
    },
    "pip_install_1": {
        in_cause: "`pip` is a command that needs to run in a terminal",
        title: "Using pip from interpreter",
    },
    "pip_install_2": {
        in_cause: "`pip` is a command that needs to run in a terminal",
        title: "Using pip from interpreter 2",
    },
    "print_is_a_function": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function",
    },
    "print_is_a_function_2": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 2",
    },
    "print_is_a_function_3": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 3",
    },
    "print_is_a_function_4": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 4",
        also_in_cause: ["print(...)"],
    },
    "print_is_a_function_5": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 5",
    },
    "print_non_paren_non_string1": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 6",
    },
    "print_non_paren_non_string2": {
        in_cause: "In older version of Python, `print` was a keyword",
        title: "print is a function 7",
    },
    "python_interpreter": {
        in_cause: " attempting to use Python to run a program",
        title: "Calling python from interpreter",
    },
    "python_not_interpreter": {
        in_cause: "Did you forget something between `a` and `b`",
        title: "problem with assigning a variable to Python",
    },
    "quote_inside_string": {
        in_cause: "Perhaps you forgot to escape a quote character",
        title: "Quote inside a string",
    },
    "raise_multiple_exceptions": {
        in_cause: "trying to raise an exception using Python 2 syntax.",
        title: "Raising multiple exceptions",
    },
    "return_outside_function": {
        in_cause: "You can only use a `return`",
        title: "Cannot use return outside function",
    },
    "scientific_notation_missing_exponent": {
        in_cause: "Did you mean `1.5e0`",
        title: "Missing exponent for scientific notation"
    },
    "semi_colon_instead_of_colon": {
        in_cause: "You wrote a semicolon, `;`, where a colon was expected.",
        title: "Semicolon instead of colon",
    },
    "semi_colon_instead_of_comma_1": {
        in_cause: "You wrote a semicolon, `;`, where a comma was expected.",
        title: "Semicolon instead of comma - 1",
    },
    "semi_colon_instead_of_comma_2": {
        in_cause: "You wrote semicolons, `;`, where commas were expected.",
        title: "Semicolon instead of commas - 2",
    },
    "semi_colon_instead_of_comma_3": {
        in_cause: "You wrote semicolons, `;`, where commas were expected.",
        title: "Semicolon instead of commas - 3",
    },
    "should_be_comprehension": {
        in_cause: "You cannot have separate code blocks inside list comprehensions.",
        title: "Code block inside comprehension",
    },
    "single_equal_with_if": {
        in_cause: "Perhaps you needed `==`",
        title: "Single = instead of double == with if",
    },
    "single_equal_with_elif": {
        in_cause: "Perhaps you needed `==`",
        title: "Single = instead of double == with elif",
    },
    "single_equal_with_while": {
        in_cause: "Perhaps you needed `==`",
        title: "Single = instead of double == with while",
    },
    "space_between_operators_1": {
        in_cause: "meant to write `**` as a single operator",
        title: "Space between operators 1",
    },
    "space_between_operators_2": {
        in_cause: "meant to write `/=` as a single operator",
        title: "Space between operators 2",
    },
    "space_in_variable_name": {
        in_cause: "You cannot have spaces in identifiers (variable names).",
        title: "Space in variable name",
    },
    "star_assignment_target": {
        in_cause: "list_or_tuple",
        title: "Wrong target for star assignment",
    },
    "too_many_nested_blocks": {
        in_cause: "you need to reduce the number",
        title: "Too many nested blocks",
        # If the word "indented" appears in "cause" for unit tests, we expect
        # that this signal an indentation error.
        also_in_cause: ["indented code blocks"],
    },
    "too_many_parentheses": {
        in_cause: "you need to reduce the number of parentheses",
        title: "Too many nested parentheses.",
    },
    "trailing_comma_in_import": {
        in_cause: "However, if you remove the last comma, there will be no syntax error",
        title: "Trailing comma in import statement",
    },
    "triple_equal": {
        in_cause: "the exact same object, use the operator `is`",
        title: "Triple-equal sign",
    },
    "unclosed_bracket": {
        in_cause: "The opening square bracket `[`",
        title: "Unclosed bracket",
    },
    "unclosed_paren_1": {
        in_cause: "The opening parenthesis `(` on line",
        title: "Unclosed parenthesis - 1",
    },
    "unclosed_paren_2": {
        in_cause: "The opening parenthesis `(` on line",
        title: "Unclosed parenthesis - 2",
    },
    "unclosed_paren_3": {
        in_cause: "The opening parenthesis `(` on line 5 is not closed",
        title: "Unclosed parenthesis - 3",
    },
    "unclosed_paren_4": {
        in_cause: "The opening parenthesis `(` on line 2 is not closed",
        title: "Unclosed parenthesis - 4",
    },
    "unexpected_after_continuation_character": {
        in_cause: "using the continuation character",
        title: "Content passed continuation line character",
    },
    "unexpected_eof": {
        in_cause: "The opening square bracket `[`",
        title: "Unexpected EOF while parsing",
    },
    "unicode_fraction": {
        in_cause: "that you meant to write the fraction",
        title: "Invalid character (unicode fraction 3/4)",
    },
    "unicode_fraction2": {
        in_cause: "that you meant to write the fraction",
        title: "Invalid character (unicode fraction 1/2)",
    },
    "unicode_fraction3": {
        in_cause: "but is different from the division operator",
        title: "Invalid character (unicode fraction slash)",
    },
    "unicode_quote": {
        in_cause: "fancy unicode quotation mark",
        title: "Invalid character (unicode quote)",
    },
    "unicode_quote2": {
        in_cause: "fancy unicode quotation mark",
        title: "Invalid character (unicode quote2)",
        not_in_cause: ["you meant to write a less than sign"],
    },
    "unicode_quote3": {
        in_cause: "fancy unicode quotation mark",
        title: "Invalid character (mistaken <)",
        also_in_cause: ["you meant to write a less than sign"],
    },
    "unicode_quote4": {
        in_cause: "fancy unicode quotation mark",
        title: "Invalid character (mistaken >)",
        also_in_cause: ["you meant to write a greater than sign"],
    },
    "unicode_quote5": {
        in_cause: "fancy unicode quotation mark",
        title: "Invalid character (mistaken comma)",
        also_in_cause: ["you meant to write a comma"],
    },
    "unmatched_closing_curly": {
        in_cause: "The closing curly bracket `}` on",
        title: "Unmatched closing curly bracket",
    },
    "unmatched_closing_paren": {
        in_cause: "The closing parenthesis `)` on",
        title: "Unmatched closing parenthesis",
    },
    "unmatched_closing_bracket_1": {
        in_cause: "The closing square bracket `]` on line",
        title: "Mismatched brackets - 1",
    },
    "unmatched_closing_bracket_2": {
        in_cause: "The closing square bracket `]` on line",
        title: "Mismatched brackets - 2",
    },
    "unmatched_closing_bracket_3": {
        in_cause: "The closing square bracket `]` on line",
        title: "Unmatched brackets - 3",
    },
    "unpacking_dict_value": {
        in_cause: "It looks like you tried to use a starred expression as a dict value",
        title: "Unpacking a dict value",
    },
    "unterminated_triple_quote_string": {
        in_cause: "You started writing a triple-quoted string",
        title: "Unterminated triple quoted string",
    },
    "tab_error": {
        in_cause: "A `TabError` indicates that you have used",
        title: "TabError",
    },
    "unescaped_backslash": {
        in_cause: "Did you forget to escape a backslash character",
        title: "EOL unescaped backslash",
    },
    "use_backquote": {
        in_cause: "use the function `repr(x)`.",
        title: "Using the backquote character",
    },
    "unicode_error": {
        in_cause: "one backslash character, `\\` followed by an uppercase `U`",
        title: "unicode error",
    },
    "walrus_does_not_exist": {  # Python < 3.8
        in_cause: "walrus operator",
        title: "Walrus operator does not exist - yet",
    },
    "walrus_instead_of_equal": {
        version_dependent: [
            "walrus operator",
            "You use the augmented assignment operator `:=` where",
        ],
        in_cause: "ignored",
        title: "Walrus instead of equal",
        also_in_cause: ["the normal assignment operator `=` was required."],
    },
    "while_missing_condition": {
        in_cause: "A `while` loop requires a condition",
        title: "Missing condition in while statement",
    },
    "would_be_type_declaration_1": {
        in_cause: "You do not need to declare variables in Python.",
        title: "Would-be variable declaration",
    },
    "would_be_type_declaration_2": {
        in_cause: "You do not need to declare variables in Python.",
        title: "Would-be variable declaration - 2",
    },
    "yield_outside_function": {
        in_cause: "You can only use a `yield`",
        title: "Cannot use yield outside function",
    },
}

if sys.version_info >= (3, 8):
    del descriptions["f_string_assign_value"]
    del descriptions["debug_fstring_not_supported"]  # introduced in Python 3.8
    del descriptions["walrus_does_not_exist"]  # := introduced in Python 3.8

if sys.version_info < (3, 9):
    del descriptions["too_many_parentheses"]  # will be a memory error instead


if (3, 9) < sys.version_info < (3, 11):
    del descriptions["missing_in_with_for"]  # problem with 3.10.1

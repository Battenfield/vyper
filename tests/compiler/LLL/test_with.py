

def test_with_depth(t, get_contract_from_lll, assert_compile_failed):
    _16_with_statements = ['with', 'var_1', 0,
                          ['with', 'var_2', 0,
                          ['with', 'var_3', 0,
                          ['with', 'var_4', 0,
                          ['with', 'var_5', 0,
                          ['with', 'var_6', 0,
                          ['with', 'var_7', 0,
                          ['with', 'var_8', 0,
                          ['with', 'var_9', 0,
                          ['with', 'var_10', 0,
                          ['with', 'var_11', 0,
                          ['with', 'var_12', 0,
                          ['with', 'var_13', 0,
                          ['with', 'var_14', 0,
                          ['with', 'var_15', 0,
                          ['mstore', 'var_1', 1]]]]]]]]]]]]]]]]
    _17_with_statements = ['with', 'var_1', 0,
                          ['with', 'var_2', 0,
                          ['with', 'var_3', 0,
                          ['with', 'var_4', 0,
                          ['with', 'var_5', 0,
                          ['with', 'var_6', 0,
                          ['with', 'var_7', 0,
                          ['with', 'var_8', 0,
                          ['with', 'var_9', 0,
                          ['with', 'var_10', 0,
                          ['with', 'var_11', 0,
                          ['with', 'var_12', 0,
                          ['with', 'var_13', 0,
                          ['with', 'var_14', 0,
                          ['with', 'var_15', 0,
                          ['with', 'var_16', 0, ['mstore', 'var_1', 1]]]]]]]]]]]]]]]]]
    get_contract_from_lll(_16_with_statements)
    assert_compile_failed(lambda: get_contract_from_lll(_17_with_statements), Exception)

from TangentS.math_tan.math_extractor import MathExtractor


def latex_math_to_slt_tuples(latex_formula):
    temp = MathExtractor.parse_from_tex(latex_formula)
    return temp.get_pairs(window=2, eob=True)


def latex_math_to_opt_tuples(latex_formula):
    temp = MathExtractor.parse_from_tex_opt(latex_formula)
    return temp.get_pairs(window=2, eob=True)

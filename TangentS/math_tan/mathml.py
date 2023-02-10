__author__ = 'Nidhin, FWTompa'




class MathML:
    """
    List of recognized tags (general MathML)
    """
    namespace = '{http://www.w3.org/1998/Math/MathML}'
    math = f'{namespace}math'

    """
        Presentation MathML only
    """
    mn = f'{namespace}mn'
    mo = f'{namespace}mo'
    mi = f'{namespace}mi'
    mtext = f'{namespace}mtext'
    mrow = f'{namespace}mrow'
    msub = f'{namespace}msub'
    msup = f'{namespace}msup'
    msubsup = f'{namespace}msubsup'
    munderover = f'{namespace}munderover'
    msqrt = f'{namespace}msqrt'
    mroot = f'{namespace}mroot'
    mfrac = f'{namespace}mfrac'
    menclose = f'{namespace}menclose'
    mfenced = f'{namespace}mfenced'
    mover = f'{namespace}mover'
    munder = f'{namespace}munder'
    mpadded = f'{namespace}mpadded'
    mphantom = f'{namespace}mphantom'
    none = f'{namespace}none'
    mstyle = f'{namespace}mstyle'
    mspace = f'{namespace}mspace'
    mtable = f'{namespace}mtable'
    mtr = f'{namespace}mtr'
    mtd = f'{namespace}mtd'
    semantics = f'{namespace}semantics'
    mmultiscripts = f'{namespace}mmultiscripts'
    mprescripts = f'{namespace}mprescripts'
    mqvar = '{http://search.mathweb.org/ns}qvar'
    mqvar2 = f'{namespace}qvar'
    merror = f'{namespace}merror'

    """
        Content MathML only
    """
    ci = f"{namespace}ci"
    cn = f"{namespace}cn"
    csymbol = f"{namespace}csymbol"
    cerror = f"{namespace}cerror"

    apply = f"{namespace}apply"
    matrix = f"{namespace}matrix"
    matrixrow = f"{namespace}matrixrow"
    share = f"{namespace}share"
    vector = f"{namespace}vector"


    _abs = f"{namespace}abs"
    _and = f"{namespace}and"
    _in = f"{namespace}in"
    _not = f"{namespace}not"
    _or = f"{namespace}or"
    approx = f"{namespace}approx"
    arccos = f"{namespace}arccos"
    arccot = f"{namespace}arccot"
    arccsc = f"{namespace}arccsc"
    arcsin = f"{namespace}arcsin"
    arcsec = f"{namespace}arcsec"
    arctan = f"{namespace}arctan"

    arccosh = f"{namespace}arccosh"
    arccoth = f"{namespace}arccoth"
    arccsch = f"{namespace}arccsch"
    arcsinh = f"{namespace}arcsinh"
    arcsech = f"{namespace}arcsech"
    arctanh = f"{namespace}arctanh"

    arg = f"{namespace}arg"
    bvar = f"{namespace}bvar"
    ceiling = f"{namespace}ceiling"
    compose = f"{namespace}compose"
    cos = f"{namespace}cos"
    cosh = f"{namespace}cosh"
    cot = f"{namespace}cot"
    coth = f"{namespace}coth"
    csc = f"{namespace}csc"
    csch = f"{namespace}csch"
    degree = f"{namespace}degree"
    determinant = f"{namespace}determinant"
    divide = f"{namespace}divide"
    emptyset = f"{namespace}emptyset"
    eq = f"{namespace}eq"
    equivalent = f"{namespace}equivalent"
    exp = f"{namespace}exp"
    exists = f"{namespace}exists"
    factorial = f"{namespace}factorial"
    floor = f"{namespace}floor"
    forall = f"{namespace}forall"
    gcd = f"{namespace}gcd"
    geq = f"{namespace}geq"
    gt = f"{namespace}gt"
    imaginary = f"{namespace}imaginary"
    imaginaryi = f"{namespace}imaginaryi"
    implies = f"{namespace}implies"
    infinity = f"{namespace}infinity"
    int = f"{namespace}int"
    interval = f"{namespace}interval"
    intersect = f"{namespace}intersect"
    leq = f"{namespace}leq"
    list = f"{namespace}list"
    limit = f"{namespace}limit"
    log = f"{namespace}log"
    lowlimit = f"{namespace}lowlimit"
    ln = f"{namespace}ln"
    lt = f"{namespace}lt"
    max = f"{namespace}max"
    min = f"{namespace}min"
    minus = f"{namespace}minus"
    moment = f"{namespace}moment"
    momentabout = f"{namespace}momentabout"
    notin = namespace + "notin"
    notsubset = namespace + "notsubset"
    notprsubset = namespace + "notprsubset"
    neq = namespace + "neq"
    partialdiff = namespace + "partialdiff"
    plus = namespace + "plus"
    prsubset = namespace + "prsubset"
    real = namespace + "real"
    root = namespace + "root"
    sec = namespace + "sec"
    sech = namespace + "sech"
    set = namespace + "set"
    setdiff = namespace + "setdiff"
    sin = namespace + "sin"
    sinh = namespace + "sinh"
    subset = namespace + "subset"
    sum = namespace + "sum"
    tan = namespace + "tan"
    tanh = namespace + "tanh"
    times = namespace + "times"
    union = namespace + "union"
    uplimit = namespace + "uplimit"




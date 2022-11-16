# Verify using a regular expression whether a string is a valid CNP.
# resource: https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)#cite_note-cnp-rezidenti-6

import re


def is_cnp_valid(cnp: str) -> bool:
    s = r"(?P<S>[1-8])"
    aa = r"(?P<AA>\d{2})"
    ll = r"(?P<LL>(0[1-9]|1[0-2]))"
    zz = r"(?P<ZZ>(0[1-9]|[1-2]\d|3[0-1]))"
    jj = r"(?P<JJ>(0[1-9]|[1-4]\d|5[0-2]))"
    nnn = r"(?P<NN>\d{2}[1-9])"
    c = r"(?P<C>\d)"

    cnp_expression = re.compile("^"+s+aa+ll+zz+jj+nnn+c+"$")

    match_objs = list(cnp_expression.finditer(cnp))
    if len(match_objs) == 0:
        return False

    # print("-> The values that each group has are: <-")
    # match_obj = match_objs[0]
    # for key in match_obj.groupdict():
    #     print(key + "=>" + match_obj.group(key))

    return True

    # return re.match(cnp_expression, cnp) is not None


if __name__ == '__main__':
    print(f"The cnp is valid: {is_cnp_valid('1220909490017')}")
    print("~"*40)
    print(f"The cnp is valid: {is_cnp_valid('1220909490007')}")

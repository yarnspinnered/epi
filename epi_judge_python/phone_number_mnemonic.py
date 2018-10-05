from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    d = {'0':['0'], '1':['1'], '2':list("ABC"), '3':list("DEF"), '4':list("GHI"), '5':list("JKL"), '6':list("MNO"), '7':list("PQRS"),
         '8':list("TUV"), '9':list("WXYZ")}

    if len(phone_number) == 1:
        return d[phone_number]

    res = []
    for c in d[phone_number[0]]:
        for end in phone_mnemonic(phone_number[1:]):
            res.append(c + end)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))

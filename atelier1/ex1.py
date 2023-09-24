def message_imc(imc):
    """_summary_

    Args:
        imc (_type_): _description_

    Returns:
        _type_: _description_
    """
    if imc < 16.5:
        return "dénutrition ou famine"
    elif imc >= 16.5 and imc < 18.5:
        return "maigreur"
    elif imc >= 18.5 and imc < 25:
        return "corpulence normale"
    elif imc >= 25 and imc < 30:
        return "surpoids"
    elif imc >= 30 and imc < 35:
        return "obésité modérée"
    elif imc >= 35 and imc < 40:
        return "obésité sévère"
    else:
        return "obésité morbide"


def test_message_imc():
    imcs = [15.0, 16.7, 20.0, 27.5, 32.0, 38.5, 45.0]
    for imc in imcs:
        interpretation = message_imc(imc)
        print(f"IMC {imc}: {interpretation}")


test_message_imc()

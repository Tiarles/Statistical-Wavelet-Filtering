# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFiltr.statisticFilter`` **):** Top level functions to filter
wavelet coefficients using consagrated methods (``threshold``) and using
Control Chart CUSUM (``cusum``) proposed in my Undergraduate Thesis, together
with prof. Dr. Fábio Mariano Bayer and prof. Dr. Alice de Jesus Kozakevicius
called *Análise do gráfico de controle CUSUM para a filtragem de coeficientes
wavelet*, in portuguese for the Universidade Federal de Santa Maria (2°/2018).

*Created by Tiarles Guterres, 2018*
'''


def filtration(coefficients, method='visu', p=3, mode='hard', dim_t=1024):
    '''
    Filters the wavelet coefficients returned by the pywt.wavedec function.
    All methods are implemented and showed in [1].

    Parameters
    ----------
    coefficients: list of 1-D array-like
        The wavelet coefficients and the scale coefficients of the last
        level. The scale coefficients isn't modify by the filtration.

    method: string
        Optional, is 'visu' by default.

    p: int or float
        Optional, is 3 by default.

    mode: string
        Optional, is 'hard' by default.

    Returns
    -------
    tuple:
        A tuple with [0] A list if numpy.array. The wavelet coefficients
        truncated by the choiced method, with scale coefficients. Ready for
        pywt.waverec function. (a little 'tip') and [1] a list of float. The
        lambda value used for each wavelet coefficient level.

    See also
    --------
    cusumFiltration: Function that use Cumulative Sum Control Chart and
        some variation for filter wavelet coefficients.

    References
    ----------
    .. [1] KOZAKEVICIUS, A. D. J.; BAYER, F. M. Filtragem de sinais via
           limiarização de coeficientes wavelet. Ciência e Natura, v. 36,
           p. 37–51, 2014. In portuguese.
    '''

    from statsWaveletFiltr.threshold import lambdasVisuShrink, \
        lambdasSureShrink, lambdasBayesShrink, lambdasSPC_Threshold
    import numpy as np
    import pywt

    scaleCoeff = coefficients[0]
    wavCoeff = coefficients[1:]

    if p == 3 and method == 'spc':
        print(('ADVICE: The p value for spc method used is ' +
               'equal to default, 3!'))

    if dim_t == 1024 and method == 'sure':
        print(('ADVICE: The t-dimension value for sure method used is equal ' +
               'to default, 1024!'))

    if method == 'visu':
        lambdaValues = lambdasVisuShrink(wavCoeff)
    elif method == 'sure':
        lambdaValues = lambdasSureShrink(wavCoeff, dim_t)
    elif method == 'bayes':
        lambdaValues = lambdasBayesShrink(wavCoeff)
    elif method == 'spc':
        lambdaValues = lambdasSPC_Threshold(wavCoeff, p=p)

    wavCoeff2 = [np.array(list(wavCoeff_i)) for wavCoeff_i in wavCoeff]

    for j in range(len(wavCoeff2)):
        wavCoeff2[j] = pywt.threshold(wavCoeff2[j], lambdaValues[j], mode)

    coefficients2 = [scaleCoeff]
    coefficients2.extend(wavCoeff2)

    return coefficients2, lambdaValues


def cusumFiltration(coefficients, h=5, k=1/2, method='cusumTrad'):
    '''
    Filters the wavelet coefficients returned by the pywt.wavedec function
    using the Cumulative Sum Control Chart (CUSUM) [1].

    Parameters
    ---------
    wavCoeff: list of array-like.
        Wavelet coefficients
    h: int, float or array-like
        Optional, 5 by default [1]. See "method" parameter.

    k: int, float or array-like
        Optional, 1/2 (or .5) by default [1]. See "method" parameter.

    method: string
        Optional, "cusumTrad" by default.

        If "method" is "cusumTrad" the Control Chart considered to filter the
        wavalet coefficients is the same considered in [1]. If the control
        limit (called **SjB** and **Sjs** here) is bigger than threshold limit
        the wavelet coefficient corresponded will be zero. In this "method" "k"
        and "h" will be constant and equals for all wavelet coefficients in all
        levels, the [1] recomend h = 5 and k = 1/2, but you can change or just
        not alterate.

        But if "method" is "cusumDecay" occurs the same in "cusumTrad" relative
        to truncation form but the "k" and "h" will be like is described in
        [2].

        Or if "method" is "cusumAdap" will be the same of the "cusumDecay"
        but the user can be choice who values of "h" and "k" will be for each
        wavelet level.

    Returns
    -------
    tuple:
        A tuple with [0] A list if numpy.array. The wavelet coefficients
        truncated by the choiced method, with scale coefficients. Ready for
        pywt.waverec function. (a little 'tip'), [1] a list of float. The "k"
        values used for each wavelet coefficient level and [2] a list of float.
        The "h" values used for each wavelet coefficient level.

    See also
    --------
    filtration: Function that use this function to filter via wavelet
        coefficients
    pywt.wavedec: Function that decomposes the signal in wavelet and
        scale coefficients
    pywt.waverec: Function that recomposes the signal from wavelet and
        scale coefficients

    References
    ----------
    .. [1] MONTGOMERY, D. C. Introduction to Statistical Quality Control. Sixth
           edition. United States: John Wiley & Sons, Inc., 2009. 733 p.

    .. [2] GUTERRES, T. D. R. M.; BAYER, F. M; KOZAKEVICIUS, A. D. J. (2018)
           Análise do gráfico de controle CUSUM para filtragem de coeficientes
           wavelet, Undergraduation Thesis, Universidade Federal de Santa
           Maria. In portuguese.
    '''

    from statsWaveletFiltr.cusum import analysisCusum, thresholdCusum
    import numpy as np

    scaleCoeff = coefficients[0]
    wavCoeff = coefficients[1:]

    wavCoeff2 = [np.array(list(wavCoeff_i)) for wavCoeff_i in wavCoeff]

    if method == 'cusumTrad':
        h2 = [h] * len(wavCoeff2)
        k2 = [k] * len(wavCoeff2)

    elif method == 'cusumDecay':

        print(('ADVICE: This method was addaptated to 5 levels of wavelet ' +
               'coefficients [2]! For more levels the method will be ' +
               'readapted, no garanties of performance'))

        k2 = [k] * len(wavCoeff2)

        j_lvl = np.arange(0, len(wavCoeff), 1)
        h2 = -7*np.log10(.201 * (len(wavCoeff) - j_lvl))

    elif method == 'cusumAdap':

        # A serie of raises!
        # 1) Check the 'k' and 'h' parameter types
        if not isinstance(k, (list, np.ndarray)):
            raise Exception("Parameter 'k' isn't a list or numpy.array")

        if not isinstance(h, (list, np.ndarray)):
            raise Exception("Parameter 'h' isn't a list or numpy.array")

        # 2) Check if the size the array-like parameters is the same to the
        #    wavelet coefficients
        if len(k) != len(wavCoeff2):
            raise Exception(("Size of 'k' doesn't match with the size of " +
                             "wavelet coefficients"))

        if len(h) != len(wavCoeff2):
            raise Exception(("Size of 'k' doesn't match with the size of " +
                             "wavelet coefficients"))
        k2 = k
        h2 = h

    for j, Dj in enumerate(wavCoeff2):
        SjB, Sjs = analysisCusum(Dj, k2[j])

        wavCoeff2[j] = thresholdCusum(Dj, SjB, Sjs, h=h2[j])

    coefficients2 = [scaleCoeff]
    coefficients2.extend(wavCoeff2)

    return coefficients2, k2, h2

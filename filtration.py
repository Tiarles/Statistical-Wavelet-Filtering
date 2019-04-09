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
    
    return


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

    return

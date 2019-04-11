# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFilt.threshold`` **):** Statistic functions for obtain threshold
values for wavelet coefficients based in some referenced works.

*Created by Tiarles Guterres, 2018*
'''


def lambdasVisuShrink(wavCoeff):
    '''
    Computes the threshold value (lambda) by VisuShrink [1] method.

    Parameters
    ---------
    wavCoeff: list of lists or array-like
        Wavelet coefficients

    Returns
    -------
    list of float:
        The threshold values for each wavelet coefficients
        vector.

    See also
    --------
    filtration: Function that use this function for filter via wavelet
        coefficients
    pywt.wavedec: Function that decomposes the signal in wavelet and
        scale coefficients
    pywt.waverec: Function that recomposes the signal from wavelet and
        scale coefficients

    References
    ----------
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.
    '''

    import numpy as np

    # Coefficients Vector from the bigger resolution
    d_m1 = list(wavCoeff[-1])  # Make a copy
    d_m1 = np.array(d_m1)       # Turns a numpy.array

    estDeviation = np.median(np.abs(d_m1))/.6745

    lambdaValues = [estDeviation * np.sqrt(2*np.log10(d_m1.size))] * \
        len(wavCoeff)

    return lambdaValues


def _sure(vector, ti):
    '''
    Internal function, for lambdasSureShrink method.

    .. note::
        After the test (via **pytest**) the fuction was changed for better
        performance.

    Parameters
    ---------
    vector: list or array-like
        vector of coefficients who lambdasSureShrink function needs for the
        computes.

    t: list or array-like
        Intern parameter set by lambdasSureShrink method.

    Returns
    -------
    list of float:
        Based on work of Stein [1].

    See also
    --------
    filtration: Function that use this function to filter via wavelet
        coefficients
    lambdasSureShrink: Function that use this function for sureshrink
        algorithm

    References
    ----------
    .. [1] STEIN, C. Estimation of the mean of a multivariate normal
           distribution. Annals of Statistics, v. 9, p. 1135–1151, 1981.
    '''

    import numpy as np

    vector2 = np.array(list(vector))

    soma1 = np.sum(vector2 <= ti)

    ti_list = [[ti]]*vector2.size

    soma2 = np.sum(np.power(np.minimum(vector2, np.concatenate(ti_list)), 2))

    return vector2.size - 2 * soma1 + soma2


def lambdasSureShrink(wavCoeff, dim_t=1024):
    '''
    Computes the threshold value (lambda) by SureShrink [1] method. It's showed
    also in [2].

    .. note::
        After the test (via **pytest**) the fuction was changed for better
        performance.

    Parameters
    ---------
    wavCoeff: list of lists or array-like
        Wavelet coefficients
    dim_t: optional, 1024 by default. t-dimension. Input vector from
        internal function _sure(vector, dim_t).

    Returns
    -------
    list of float:
        The threshold values for each wavelet coefficients vector.

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
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.

    .. [2] KOZAKEVICIUS, A. D. J.; BAYER, F. M. Filtragem de sinais via
           limiarização de coeficientes wavelet. Ciência e Natura, v. 36,
           p. 37–51, 2014. In portuguese.
    '''

    import numpy as np

    wavCoeff2 = [np.array(list(wavCoeff_i)) for wavCoeff_i in wavCoeff]

    lambdaValues = []

    for coeff in wavCoeff2:

        estDeviation = np.median(np.abs(coeff))/.6745

        tmax = estDeviation*np.sqrt(2*np.log10(coeff.size))

        t = np.linspace(0, tmax, dim_t)

        res_sure = [_sure(coeff, ti) for ti in t]

        lambdaValues.append(t[np.argmin(res_sure)])
    return lambdaValues


def lambdasBayesShrink(wavCoeff):
    '''
    Computes the threshold value (lambda) by BayesShrink [1] method. It's
    showed also in [2].

    Parameters
    ---------
    wavCoeff: list of lists or array-like
        Wavelet coefficients

    Returns
    -------
    list of float:
        The threshold values for each wavelet coefficients vector.

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
    .. [1] CHANG, S. G.; YU, B.; VETTERLI, M. Adaptive wavelet thresholding
           for image denoising and compression. IEEE Transactions on Image
           Processing, v. 9, p. 1532–1546, 2000.

    .. [2] KOZAKEVICIUS, A. D. J.; BAYER, F. M. Filtragem de sinais via
           limiarização de coeficientes wavelet. Ciência e Natura, v. 36,
           p. 37–51, 2014. In portuguese.
    '''

    import numpy as np

    wavCoeff2 = [np.array(list(wavCoeff_i)) for wavCoeff_i in wavCoeff]

    d_m1 = wavCoeff2[-1]
    deviation_square = np.power(np.median(np.abs(d_m1))/0.6745, 2)

    lambdaValues = []

    for wavCoeff_i in wavCoeff2:
        deviation2_wavCoeff_i = np.sum(np.power(wavCoeff_i, 2))/wavCoeff_i.size

        deviation_Xj = np.sqrt(
            np.maximum(deviation2_wavCoeff_i - deviation_square, 0))

        lambdaValues.append(deviation_square/deviation_Xj)

    return lambdaValues


def lambdasSPC_Threshold(wavCoeff, p=3):
    '''
    Computes the threshold value (lambda) by SPC-Threshold [1], [2] method

    .. note::
        After the test (via **pytest**) the fuction was changed for better
        performance.

    Parameters
    ---------
    wavCoeff: list of lists or array-like
        Wavelet coefficients
    p: int or float
        Optional, 3 by default. Parameter for the algorithm [1],
        generally is used 2 or 3.

    Returns
    -------
    list of float:
        The threshold values for each wavelet coefficients
        vector.

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
    .. [1] BAYER, F. M.; KOZAKEVICIUS, A. J. SPC-threshold:  uma proposta de
           limiarização para filtragem adaptativa de sinais. Tendências em
           Matemática Aplicada e Computacional, v. 11, n. 2, p. 121–132, 2010.
           In portuguese.

    .. [2] KOZAKEVICIUS, A. D. J.; BAYER, F. M. Filtragem de sinais via
           limiarização de coeficientes wavelet. Ciência e Natura, v. 36,
           p. 37–51, 2014. In portuguese.
    '''

    import numpy as np

    wavCoeff2 = [np.array(list(wavCoeff_i)) for wavCoeff_i in wavCoeff]

    lambdaValues = []

    for wavCoeff_i in wavCoeff2:
        Sj = np.sqrt(1./(wavCoeff_i.size - 1) *
                     np.sum(np.power(wavCoeff_i - wavCoeff_i.mean(), 2)))

        while (np.abs(wavCoeff_i) >= p*Sj).any():
            wavCoeff_i = wavCoeff_i[np.abs(wavCoeff_i) < p*Sj]
            Sj = np.sqrt(1./(wavCoeff_i.size - 1) *
                         np.sum(np.power(wavCoeff_i - wavCoeff_i.mean(), 2)))

        lambdaValues.append(p*Sj)
    return lambdaValues

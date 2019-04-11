# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFilt.signals`` **):** Functions to evaluate the dignal fitering
process using the module ``statisticFilter`` or any kind of filtration.

*Created by Tiarles Guterres, 2018*
'''


def for_dB_scale(x):
    '''
    Converts x to dB scale using 10*log10(x)

    Parameters
    ---------
    x: int or float
        The value for convertion

    Returns
    -------
    float:
        The x value converted in dB scale.
    '''
    import numpy as np
    return 10*np.log10(x)


def for_real_scale(x):
    '''
    Converts x to real scale using 10**(x/10)

    Parameters
    ---------
    x: int or float
        The value for convertion

    Returns
    -------
    float:
        The x value converted in eal scale.
    '''

    return 10**(x/10)


def snr_square_mean_error(currentSignal, idealSignal):
    '''
    Calculate the SNR via the current signal and the ideal using the square
    mean error approach.

    Parameters
    ----------
    currentSignal: 1-D array-like
        The signal for compare with ideal.
    idealSignal: 1-D array-like
        The ideal signal, based in the currentSignal.

    Returns
    -------
    float:
        Mean of idealSignal by standard deviation of the noise.
    '''

    import numpy as np

    (currentSignal, idealSignal) = (np.array(currentSignal),
                                    np.array(idealSignal))

    return np.mean(np.power(currentSignal - idealSignal, 2))


def snr_mean_standardNoise(idealSignal, noiseSignal):
    '''
    Calculate the SNR via ideal signal mean and standard deviation of the
    noise.

    Parameters
    ----------
    idealSignal: 1-D array-like
        The ideal signal, based in the currentSignal.
    noiseSignal: 1-D array-like
        Noise apply to ideal signal, could be a initial or residual noise.

    Returns
    -------
    float:
        Mean of idealSignal by standard deviation of the noise.
    '''

    import numpy as np

    idealSignal, noiseSignal = (np.array(idealSignal), np.array(noiseSignal))
    return idealSignal.mean()/noiseSignal.std()


def snr_variances(idealSignal, noiseSignal):
    '''
    Calculate the SNR via ratio of variances of ideal signal and noise.

    Parameters
    ----------
    idealSignal: 1-D array-like
        The ideal signal, based in the currentSignal.
    noiseSignal: 1-D array-like
        Noise apply to ideal signal, could be a initial or residual noise.

    Returns
    -------
    float:
        Variance ratio value between the ideal and noise signals.
    '''

    import numpy as np

    idealSignal, noiseSignal = (np.array(idealSignal), np.array(noiseSignal))

    var_ideal = idealSignal.var()
    var_noise = noiseSignal.var()

    return var_ideal/var_noise


def cnr_amplitude_standardNoise(idealSignal, noiseSignal):
    '''
    Calculate the CNR (contrast-to-noise ratio [1]) via the amplitude
    of idealSignal and standard deviation of the noise.

    Parameters
    ----------
    idealSignal: 1-D array-like
        The ideal signal, based in the currentSignal.
    noiseSignal: 1-D array-like
        Noise apply to ideal signal, could be a initial or residual noise.

    Returns
    -------
    float:
        Ratio of maximum distance of zero and standard deviation of the noise.
    '''

    import numpy as np

    idealSignal, noiseSignal = (np.array(noiseSignal), np.array(noiseSignal))

    return np.maximum(np.abs(idealSignal.max()),
                      np.abs(idealSignal.min()))/noiseSignal.std()


def differential_snr_dB(initialSignal, finalSignal, method='square_mean_error',
                        idealSignal=None):
    '''
    Calculate the SNR or CNR difference between two signals: after and before
    filtering. Ideal signal may be used.

    Parameters
    ---------
    initialSignal: 1-D array-like
        Initial Signal, before the filtering process

    finalSignal: 1-D array-like
        Final Signal, after the filtering process

    method: string, optional
        Is 'square_mean_error' by default, other forms of calculate the
        SNR differential is 'mean_StandardNoise', 'variances' and
        'amplitude_standardNoise'.

    idealSignal: 1-D array-like or 0, optional
        Is 0 by default,  is necessary in all methods except in
        'square_mean_error' method.

    Returns
    -------
    float:
        The SNR differential value in dB.
    '''

    import numpy as np

    if str(type(idealSignal)) == "<class 'NoneType'>":
        insertedIdeal = False
        idealSignal = np.zeros(initialSignal.size)
    else:
        insertedIdeal = True

    initialSignal, finalSignal = (np.array(initialSignal),
                                  np.array(finalSignal))
    idealSignal = np.array(idealSignal)

    if method == 'square_mean_error':
        ret = for_dB_scale(snr_square_mean_error(initialSignal, finalSignal))
    elif method == 'mean_StandardNoise' or \
            method == 'amplitude_standardNoise' and insertedIdeal:
        noise = initialSignal - idealSignal
        residuo = finalSignal - idealSignal

        ret = for_dB_scale(noise.std()/residuo.std())

    elif method == 'variances' and insertedIdeal:
        noise = initialSignal - idealSignal
        residuo = finalSignal - idealSignal

        ret = for_dB_scale(noise.var()/residuo.var())
    else:
        raise('Not found method or idealSignal isn\'t inserted!')

    return ret

def dopplerFunction(dim=1024, normalize=True, fq=0):
    '''
    Generate the Doppler function in a range of 0 to 1, with dim points.

    Parameters
    ----------
    dim: int
        Dimension of the signal.

    normalize: bool, optional
        It is True by default. This parameter normalize the data values 
        in a range of 0 to 1 with a function present in 
        ``statsWaveletFilt.miscellaneous``.

    fq: int or float, optional
        It is 0 by default. With this default value the original doppler, 
        shown by Donoho [1] will be used.

    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis

    References
    ----------
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.
    '''

    import numpy as np
    import statsWaveletFilt.miscellaneous as misc

    linspace = np.linspace
    sin = np.sin
    pi = np.pi
    sqrt = np.sqrt

    x = linspace(0, 1, dim)
    e = 0.05
    
    if fq == 0:
        y = sqrt(x*(1 - x))*sin(2*pi*(1 + e)/(x + e))
    else:
        y = sqrt(x*(1 - x))*sin(2*fq*pi*(1 + e)/(x + e))
    
    if normalize:
        y_nor = misc.normalizeData(y)
    else:
        y_nor = y
    return (x, y_nor)

def heavsineFunction(dim=1024, normalize=True, heavs = 0):
    '''
    Generate the Heavsine function in a range of 0 to 1, with dim points.

    Parameters
    ----------
    dim: int
        Dimension of the signal.

    normalize: bool, optional
        It is True by default. This parameter normalize the data values 
        in a range of 0 to 1 with a function present in 
        ``statsWaveletFilt.miscellaneous``.

    heavs: int or float, optional
        It is 0 by default. This parameter, called * heavs * is the number of 
        discontinuities in the heavens characteristic signal shown by 
        Donoho [1] with 0 the signal will be the original, used in [1].

    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis

    References
    ----------
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.
    '''

    import numpy as np
    import statsWaveletFilt.miscellaneous as misc

    linspace = np.linspace
    sin = np.sin
    signal = np.sign
    pi = np.pi

    x = linspace(0, 1, dim)
    
    if heavs == 0:
        y = 4*sin(4*pi*x) - signal(x - 0.3) - signal(0.72 - x)
    else:
        y = 4*sin(4*pi*x)
        for i in range(heavs):
            if i % 2:
                y -= signal(x - np.random.random())
            else:
                y += signal(x - np.random.random())
    if normalize:
        y_nor = misc.normalizeData(y)
    else:
        y_nor = y
    return (x, y_nor)


def blockFunction(dim=1024, normalize=True, ht = 0):
    '''
    Generate the Block function in a range of 0 to 1, with dim points.

    Parameters
    ----------
    dim: int
        Dimension of the signal.

    normalize: bool, optional
        It is True by default. This parameter normalize the data values 
        in a range of 0 to 1 with a function present in 
        ``statsWaveletFilt.miscellaneous``.

    ht: int, optional
        It is 0 by default. The parameter called *ht* is the commutation 
        characteristic of block signal. The default parameter will generate 
        the signal shown in [1].

    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis

    References
    ----------
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.
    '''
    import numpy as np
    import statsWaveletFilt.miscellaneous as misc

    linspace = np.linspace
    sign = np.sign
    array = np.array

    if ht == 0:
        h = [0, 4, -5, 3, -4, 5, -4.2, 2.1, 4.3, -3.1, 2.1, -4.2]
        t = array([0, 0.1, 0.13, 0.15, 0.23, 0.25, 0.40, 0.44, 0.65, 0.76, 0.78,
                   0.81])
    else:
        hmax, hmin = 5, -5
        h = np.random.random(ht) * np.abs(hmax - hmin) + hmin
        t = np.random.random(ht)

    x = linspace(0, 1, dim)

    K = lambda t: (1 + sign(t))/2
    y = array([sum([h[j]*K(xi - t[j])
                    for j in range(len(h))])
               for xi in x])

    if normalize:
        y_nor = misc.normalizeData(y)
    else:
        y_nor = y
    return (x, y_nor)


def bumpFunction(dim=1024, normalize=True, wht=0):
    '''
    Generate the Bump function in a range of 0 to 1, with dim points. Take care
    to the representation limits of this function is blows infinity in Y axis.

    Parameters
    ----------

    dim: int
        Dimension of the signal.

    normalize: bool, optional
        It is True by default. This parameter normalize the data values 
        in a range of 0 to 1 with a function present in 
        ``statsWaveletFilt.miscellaneous``.

    wht: int, optional
        It is 0 by default. The parameter called *wht* is the number of peaks
        characteristic of bump signal. The default parameter will generate 
        the signal shown in [1].

    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis

    References
    ----------
    .. [1] DONOHO, D. L.; JOHNSTONE, I. M. Ideal spatial adaptation via
           wavelet shrinkage. Biometrika, v. 81, p. 425–455, 1994.
    '''

    import numpy as np
    import statsWaveletFilt.miscellaneous as misc

    linspace = np.linspace
    array = np.array
    abs = np.abs
    sum = np.sum
    
    if wht == 0:
        h = [4, 5, 3, 4, 5, 4.2, 2.1, 4.3, 3.1, 5.1, 4.2]

        w = [0.005, 0.005, 0.006, 0.01, 0.01, 0.03, 0.01, 0.01, 0.005, 0.008,
             0.005]  # for Bumps
        t = array([0, 0.1, 0.13, 0.15, 0.23, 0.25, 0.40, 0.44, 0.65, 0.76, 0.78,
                   0.81])
    else:
        wmin, wmax = 0.005, 0.03
        hmin, hmax = 0, 5

        h = np.random.random(wht) * np.abs(hmin - hmax) + hmin
        w = np.random.random(wht) * np.abs(wmin - wmax) + wmin
        t = np.random.random(wht)

    x = linspace(0, 1, dim)

    K = lambda t: (1 + abs(t))**(-4)
    y = array([sum([h[j]*K((xi - t[j])/w[j])
                    for j in range(len(h))])
               for xi in x])
    
    if normalize:
        y_nor = misc.normalizeData(y)
    else:
        y_nor = y
    return (x, y_nor)
# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFiltr.signals`` **):** Functions to evaluate the dignal fitering
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
    
    return


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

    return


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

    return


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

    return


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

    return


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

    return

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

    return


def heavsineFunction(dim=1024, normalize=True, heavs = 0):
    '''
    Generate the Heavsine function in a range of 0 to 1, with dim points.

    Parameters
    ----------
    dim: int
        Dimension of the signal.

    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis
    '''

    return


def blockFunction(dim=1024, normalize=True, ht = 0):
    '''
    Generate the Block function in a range of 0 to 1, with dim points.

    Parameters
    ----------
    dim: int
        Dimension of the signal.
    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis
    '''

    return


def bumpFunction(dim=1024, normalize=True, wht=0):
    '''
    Generate the Bump function in a range of 0 to 1, with dim points. Take care
    to the representation limits of this function is blows infinity in Y axis.

    Parameters
    ----------

    dim: int
        Dimension of the signal.
    Returns
    -------
    tuple:
        [0] 1-D array-like, coordinates in X axis and [1] 1-D array-like,
        coordinates in Y axis
    '''

    return
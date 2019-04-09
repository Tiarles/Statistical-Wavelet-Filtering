# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFiltr.miscellaneous`` **):** A Miscellaneous of functions for
work with data and show wavelet coefficients

*Created by Tiarles Guterres, 2018*
'''

def showWaveletCoeff(coefficients, filename='tmp', format='pdf',
                     threshold_value=0, color='black', color_threshold='black',
                     figsize=(7, 8), title=''):
    '''
    Show and save the wavelet and scale coefficients in a plot.

    Parameters
    ----------
    coeff: list of numpy.array's
        With in '0' position the scale coefficients. Equal to the
        ``pywt.wavedec()`` return.
    filename: string
        Optional, is 'tmp' by default. This is the first part of the
        name of the figure.
    format: string
        Optional, is 'pdf' by default. This is the last part of the name of the
        figure. Can be 'png', 'ps', 'eps' and 'svg' too.

    threshold_value: int, float or list.
        Optional, is 0 by default, this means that bothing new happens.
        Otherwise, a line in threshold value will be plotted in all wavelet
        coefficients plots. This value can be a list too, but they was to be
        the same size of wavelet coefficients (without the scale coefficient).

    Returns
    -------
    void:
        Nothing is returned, the plots is show and save.

    See also
    --------
    pywt.wavedec: Function that decomposes the signal in wavelet and
        scale coefficients
    pywt.waverec: Function that recomposes the signal from wavelet and
        scale coefficients

    filtration.filtration: Function that use this function to filter via
        wavelet coefficients

    filtration.filtrationCusum: Function that use Cumulative Sum Control Chart
        and some variation for filter wavelet coefficients.
    '''

    return


def normalizeData(data, min=0, max=1):
    '''
    Its almost a map function. This function normalize the data between a
    min and max values.

    Parameters
    ----------

    data: list or array-like
        The values that desire normalize.
    min: int or float
        Optional, is -1 by default. The min value correspond, in the end,
        of the min value of data.
    max: int or float
        Optional, is 1 by default. The max value correspond, in the end,
        of the max value of data.

    Returns
    -------
    numpy.array:
        The data normalized between min and max values.

    '''

    return


def generateData(functions=['doppler', 'block', 'bump', 'heavsine'],
                 varNoises=[0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007,
                            0.008, 0.009, 0.010],
                 dim_signals=1024,
                 n_samples_per_sig_per_noise=10000, folder='tmp'):
    '''
    If you like to generate your dataset before run your test you can use
    this function to generate the data. With the 1) type of signal and
    2) quantity of noise (in variance). Saves in ``.npy``
    '''

    return

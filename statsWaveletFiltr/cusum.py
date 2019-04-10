# -*- coding: utf-8 -*-

'''
**Wavelet Based in CUSUM control chart for filtering signals Project (module**
``statsWaveletFiltr.cusum`` **):** Functions to analise data using Control
Chart CUSUM. In this package the application of this chart is for filtration of
wavelet coefficients.

*Created by Tiarles Guterres, 2018*
'''


def analysisCusum(data, k=1/2, mean=None, std=None, SjBi_start=0,
                  Sjsi_start=0):
    '''
    Calculates the Control Limits of CUSUM like in [1]. This is a Control Chart
    defined in [2] and this type of tool serves to make a control of data who
    is  called in statistic "process".

    For more details about the parameters see [1] Chapter 9: Cumulative Sum and
    Exponentially Weighted Moving Average Control Charts.

    Parameters
    ----------
    data: list or array-like
        This is the data of "process" who CUSUM has to analize
    k: int or float
        Optional, 1/2 (or .5) by default. It's a parameter of the CUSUM
        algorithm. Helps to the Control Chart acummulate the Control Limits of
        each element of data.
    mean: int or float
        Optional, is None by default, but turns the mean of data. Also an
        intern parameter of the algorithm for help to acumulate the control
        limits.
    std: int or float
        Optional, is None by default, but turns the standard deviation of data.
        The same function of mean in relation of control limits.

    SjBi_start: int or float
        Optional, is 0 by default. Is the start value for acumulation of
        superior control limit.

    Sjsi_start: int or float
        Optional, is 0 by default. Is the start value for acumulation of
        inferior control limit.

    Returns
    -------
    tuple:
        A tuple of control limits. In [0] the superior limits and in [2] the
        inferior limits.

    See also
    --------
    thresholdCusum: Function used to truncation of data using the control
        limits obtained in this function and a decision interval, called "H".

    References
    ----------
    .. [1] MONTGOMERY, D. C. Introduction to Statistical Quality Control. Sixth
           edition. United States: John Wiley & Sons, Inc., 2009. 733 p.

    .. [2] PAGE, E. S. Continous Inspection Schemes. Biometrika, v. 41,
           p. 100-115, 1954

    '''

    import numpy as np

    if std is None:
        std = data.std()
    if mean is None:
        mean = data.mean()

    K = k * std

    SjB, Sjs = [SjBi_start], [Sjsi_start]

    for i, xi in enumerate(data):

        SjBi_temp = np.maximum(0, xi - (mean + K) + SjB[i])
        Sjsi_temp = np.maximum(0, (mean - K) - xi + Sjs[i])

        SjB.append(SjBi_temp)
        Sjs.append(Sjsi_temp)

    SjB = np.array(SjB[1:])
    Sjs = np.array(Sjs[1:])

    return SjB, Sjs


def thresholdCusum(data, SjB, Sjs, std=None, h=5):
    '''
    Makes the truncation of data accordyling with control limits SjB and Sjs
    and the interval of decision [H = h * data.std()]. The threshold method
    it's showed in [1], more about cusum it's showed in [2], Chapter 9.

    .. note::
        The size of **data** must be **equal** to size of **SjB** and **Sjs**.

    .. note::
        After the test (via **pytest**) the fuction was changed for better
        performance.

    Parameters
    ----------
    data: list or array-like
        The data who corresponding to control limits.
    SjB: list or array-like
        The control superior limits who corresponding to data .
    Sjs: list or array-like
        The control inferior limits who corresponding to data .
    std: int or float
        Optional, is None by default, but turns the standard deviation of data.
        It's an intern parameter of the algorithm for help to acumulate the
        control limits.
    h: int or float
        Optional, 5 by default. This variable multiply with standard deviation
        of data to obtain the interval of decision (H).

    Returns
    -------
    numpy.array:
        An array with elements of data truncated or not, depending of the
        control limits and the interval of decision.

    See also
    --------
    analysisCusum: Make the cusum analysis inthe data, return the control
        limits corresponding to data input.

    References
    ----------
    .. [1] GUTERRES, T. D. R. M.; BAYER, F. M; KOZAKEVICIUS, A. D. J. (2018)
           Análise do gráfico de controle CUSUM para filtragem de coeficientes
           wavelet, Undergraduation Thesis, Universidade Federal de Santa
           Maria. In portuguese.

    .. [2] MONTGOMERY, D. C. Introduction to Statistical Quality Control. Sixth
           edition. United States: John Wiley & Sons, Inc., 2009. 733 p.
    '''

    import numpy as np

    if std is None:
        std = data.std()

    data2 = []

    H = h * std

    for i, Dji in enumerate(data):
        if (SjB[i] > H) or (Sjs[i] > H):
            data2.append(Dji)
        else:  # (SjBi =< H) and (Sjsi =< H)
            data2.append(0)
    return np.array(data2)

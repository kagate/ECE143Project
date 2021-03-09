def pie_charts(DataDict, Title, Filename, ExplodeList=[]):
    '''
    This function outputs a pie chart of the input DataDict and saves the figure under Filename
    :param DataDict: Dictionary of number of instances of each possible data value (e.g. {'Action Movies': 22, 'Comedy Movies': 43})
    :param Title: Title of figure
    :param Filename: Filename of saved pie chart figure
    :param ExplodeList: List of the amount of separation between pie slices in the pie chart (bigger values mean more separation)
    :type DataDict: dictionary 
    :type Title: string
    :type Filename: string
    :type ExplodeList: list
    '''
    assert isinstance(DataDict, dict), "Input data must be a dictionary"
    assert isinstance(Title, str), "Title must be a string"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(ExplodeList, list), "ExplodeList must be a list"
    
    import matplotlib.pyplot as plt
    

    pie, _ = plt.subplots(figsize=[12,10])
    labels = DataDict.keys()
    if not ExplodeList:    
        plt.pie(x=DataDict.values(), autopct="%.1f%%", labels=labels, pctdistance=0.8) 
    else:
        plt.pie(x=DataDict.values(), explode=ExplodeList, autopct="%.1f%%", labels=labels, pctdistance=0.8)
    plt.set_cmap('PuBuGn')
    plt.title(Title, fontsize=18)
    pie.savefig(Filename)

def bar_charts(StreamingPlatform, Data1, Data1Name, Filename):
    '''
    This function makes a bar graph with x-values=StreamingPlatform and y-values=Data1
    :param StreamingPlatform: list of streaming platforms
    :param Data1: List containing data on one attribute of each streaming platform
    :param Data1Name: Name of attribute in Data1 (e.g. "Popular Movie Count")
    :param Filename: Filename of saved bar chart 
    :type StreamingPlatform: list of strings
    :type Data1: list 
    :type Data1Name: string
    :type Filename: string
    '''
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    assert isinstance(StreamingPlatform, list), "StreamingPlatform must be a list"
    assert isinstance(Data1, list), "Data1 must be a list"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(Data1Name, str), "Data1Name must be a string"

    plt.figure()
    FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1})
    BarChartFig = sns.barplot(x="Streaming Platform", y=Data1Name, data=FinalDataStruct, palette="Blues_d")
    plt.savefig(Filename)


def scatter_plots(Data1, Data1Name, Filename, Data2=[], Data2Name=""):
    '''
    This function makes a scatter plot with the x-values being the different streaming platforms Data1
    is associated with, and the y-values (Data1) being the attribute we want to compare between streaming platforms 
    (e.g. make plot of all IMDB scores of the movies on Netflix, Hulu, Prime, Disney+). 
    Data2 is an optional argument which adds a third dimension to the plot: the colors of the 
    points are tied to another attibute (e.g. point is red if movie is rated 13+, point is blue if movie is rated 18+, etc)
    Note: order of streaming platforms in Data1 and Data2 must be Netflix, Hulu, Prime, Disney+

    :param Data1: List of lists containing data on one attribute of each streaming platform 
    :param Data1Name: Name of attribute in Data1 (e.g. "IMDB Scores")
    :param Filename: Filename of saved scatter plot 
    :param Data2: List of lists containing data on one attribute of each streaming platform 
    :param Data2Name: Name of attribute in Data2 (e.g. "Ages")
    :type Data1: List of lists
    :type Data1Name: String
    :type Filename: String
    :type Data2: List of lists
    :type Data2Name: String
    '''
    assert isinstance(Data1, list), "Data1 must be a list"
    assert isinstance(Data2, list), "Data2 must be a list"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(Data1Name, str), "Data1Name must be a string"
    assert isinstance(Data2Name, str), "Data2Name must be a string"

    import pandas as pd
    import seaborn as sns

    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"]
    sns.set(rc={'axes.facecolor': Colors[4], 'figure.facecolor': Colors[4]})

    StreamingPlatform = ["Netflix"]*len(Data1[0]) + ["Hulu"]*len(Data1[1]) + ["Prime"]*len(Data1[2]) + ["Disney+"]*len(Data1[3])
    Data1List = sum(Data1, [])

    if Data2:
        Data2List = sum(Data2, [])

    # Make data into long-form structure for seaborn plotting
    if Data2:
        FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1List, Data2Name: Data2List})
    else:
        FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1List})

    IMDBScatter = sns.catplot(x="Streaming Platform", y=Data1Name, hue=Data2Name, data=FinalDataStruct)
    IMDBScatter.savefig(Filename)

def heatmap_plots(data, row_labels, col_labels, Filename):
    '''
    This function creates a heatmap plot of the input data.

    :param data: data to be displayed
    :param row_labels: labels of rows of heatmap
    :param col_labels: labels of columns of heatmap
    :param Filename: name of saved heatmap figure
    :type data: array
    :type row_labels: list of strings
    :type column_labels: list of strings
    :type Filename: string
    '''
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib import colors

    assert isinstance(data, np.ndarray), "input data must be an array"
    assert isinstance(row_labels, list), "row_labels must be a list"
    assert isinstance(col_labels, list), "col_labels must be a list"
    assert isinstance(Filename, str), "Filename must be a string"

    def heatmap(data, row_labels, col_labels, ax=None,
                cbar_kw={}, cbarlabel="", **kwargs):
        """
        Create a heatmap from a numpy array and two lists of labels.

        Parameters
        ----------
        data
            A 2D numpy array of shape (N, M).
        row_labels
            A list or array of length N with the labels for the rows.
        col_labels
            A list or array of length M with the labels for the columns.
        ax
            A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
            not provided, use current axes or create a new one.  Optional.
        cbar_kw
            A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
        cbarlabel
            The label for the colorbar.  Optional.
        **kwargs
            All other arguments are forwarded to `imshow`.
        """

        if not ax:
            ax = plt.gca()

        # Plot the heatmap
        im = ax.imshow(data, **kwargs)

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        # We want to show all ticks...
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))
        # ... and label them with the respective list entries.
        ax.set_xticklabels(col_labels)
        ax.set_yticklabels(row_labels)

        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=True, bottom=False,
                    labeltop=True, labelbottom=False)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-47, fontsize=8, ha="right",
                rotation_mode="anchor")

        # Turn spines off and create white grid.
        for edge, spine in ax.spines.items():
            spine.set_visible(False)

        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar

#--------------------------------------------------------------------------------------
    fig, ax = plt.subplots()

    ColorChoices = colors.ListedColormap(['slategrey', 'powderblue'])
    im1, cbar1 = heatmap(data, row_labels, col_labels, ax=ax,
                    cmap=ColorChoices, cbar_kw=dict(ticks=[0, 1]), cbarlabel="")

    # im2, cbar2 = heatmap(data[30:59], row_labels[30:59], col_labels[30:59], ax=ax2,
    #                 cmap=ColorChoices, cbar_kw=dict(ticks=[0, 1]), cbarlabel="")

    fig.tight_layout()
    fig.savefig(Filename)
    

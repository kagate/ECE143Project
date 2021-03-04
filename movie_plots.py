def movie_pie_charts(NetflixDict, HuluDict, PrimeDict, DisneyDict, Title, Filename, NumSubplots, ExplodeList=[]):
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
    assert isinstance(NetflixDict, dict), "Netflix data must be a dictionary"
    assert isinstance(HuluDict, dict), "Hulu data must be a dictionary"
    assert isinstance(PrimeDict, dict), "Prime data must be a dictionary"
    assert isinstance(DisneyDict, dict), "Disney data must be a dictionary"
    assert isinstance(Title, str), "Title must be a string"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(ExplodeList, list), "ExplodeList must be a list"
    
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    mpl.rcParams['font.size'] = 12.0

    if NumSubplots == 4:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=[12, 10])
        # Netflix subplot 
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], autopct="%.1f%%", labels=[NetLabels for NetLabels in NetflixDict], pctdistance=.8, labeldistance=1.1)
        ax1.set_title('Netflix Plot')
        # Hulu subplot 
        ax2.pie([float(Vals) for Vals in HuluDict.values()], autopct="%.1f%%", labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=.8, labeldistance=1.1)
        ax2.set_title('Hulu Plot')
        # Prime subplot 
        ax3.pie([float(Vals) for Vals in PrimeDict.values()], autopct="%.1f%%", labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=.8, labeldistance=1.1)
        ax3.set_title('Prime Plot')
        # Disney subplot 
        ax4.pie([float(Vals) for Vals in DisneyDict.values()], autopct="%.1f%%", labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=.8, labeldistance=1.1)
        ax4.set_title('Disney Plot')
        # if not ExplodeList:    
        #     plt.pie(x=DataDict.values(), autopct="%.1f%%", labels=labels, pctdistance=0.8) 
        # else:
        #     plt.pie(x=DataDict.values(), explode=ExplodeList, autopct="%.1f%%", labels=labels, pctdistance=0.8)
        plt.set_cmap('PuBuGn')
        # plt.title(Title, fontsize=18)
        fig.savefig(Filename + '.png')
    
    # option currently not used for any figures, but left in for team to decide if subplots with two figures on them could be used anywhere
    elif NumSubplots == 2:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[12, 10])
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], explode=ExplodeList[0], autopct="%.1f%%", labels=[NetLabels for NetLabels in NetflixDict], pctdistance=0.8)
        ax1.set_title('Netflix Plot')
        # Hulu subplot 
        ax2.pie([float(Vals) for Vals in HuluDict.values()], explode=ExplodeList[1], autopct="%.1f%%", labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=0.8)
        ax2.set_title('Hulu Plot')
        fig.savefig(Filename + '1.png')

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[12, 10])
        # Prime subplot 
        ax1.pie([float(Vals) for Vals in PrimeDict.values()], explode=ExplodeList[2], autopct="%.1f%%", labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=0.8)
        ax1.set_title('Prime Plot')
        # Disney subplot 
        ax2.pie([float(Vals) for Vals in DisneyDict.values()], explode=ExplodeList[3], autopct="%.1f%%", labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=0.8)
        ax2.set_title('Disney Plot')
        fig.savefig(Filename + '2.png')
    else:
        # Netflix Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], explode=ExplodeList[0], autopct="%.1f%%", labeldistance=1.16, labels=[NetLabels for NetLabels in NetflixDict], pctdistance=1.08)
        ax1.set_title('Netflix Plot')   
        fig.savefig(Filename + 'Netflix.png')

        # Hulu Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in HuluDict.values()], explode=ExplodeList[1], autopct="%.1f%%", labeldistance=1.16, labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=1.08)
        ax1.set_title('Hulu Plot')   
        fig.savefig(Filename + 'Hulu.png')

        # Prime Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in PrimeDict.values()], explode=ExplodeList[2], autopct="%.1f%%", labeldistance=1.16, labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=1.08)
        ax1.set_title('Prime Plot')   
        fig.savefig(Filename + 'Prime.png')

        # Disney Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in DisneyDict.values()], explode=ExplodeList[3], autopct="%.1f%%", labeldistance=1.16, labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=1.08)
        ax1.set_title('Disney Plot')   
        fig.savefig(Filename + 'Disney.png')

def movies_bar_charts(StreamingPlatform, Data1, Data1Name, Filename):
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
    BarChartFig = sns.barplot(x="Streaming Platform", y=Data1Name, data=FinalDataStruct, palette="Blues_d", alpha=.5)
    plt.savefig(Filename)

def movie_scatter_plots(Data1, Data1Name, Filename, Data2=[], Data2Name=""):
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
    import matplotlib.pyplot as plt

    sns.set(rc={'figure.figsize':(12, 10)})

    # Data1List1 = sum(Data1[0], [])
    # Data1List2 = sum(Data1[2:], [])

    StreamingPlatform1 = ["Netflix"]*len(Data1[0]) 
    StreamingPlatform2 = ["Hulu"]*len(Data1[1])
    StreamingPlatform3 = ["Prime"]*len(Data1[2])
    StreamingPlatform4 = ["Disney+"]*len(Data1[3])

    # if Data2:
    #     Data2List1 = sum(Data2[0:2], [])
    #     Data2List2 = sum(Data2[2:], [])

    # Make data into long-form structure for seaborn plotting
    if Data2:
        FinalDataStruct1 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[0], Data2Name: Data2[0]})
        FinalDataStruct2 = pd.DataFrame({"Streaming Platform": StreamingPlatform2, Data1Name: Data1[1], Data2Name: Data2[1]})
        FinalDataStruct3 = pd.DataFrame({"Streaming Platform": StreamingPlatform3, Data1Name: Data1[2], Data2Name: Data2[2]})
        FinalDataStruct4 = pd.DataFrame({"Streaming Platform": StreamingPlatform4, Data1Name: Data1[3], Data2Name: Data2[3]})
    else:
        FinalDataStruct1 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[0]})
        FinalDataStruct2 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[1]})
        FinalDataStruct3 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[2]})
        FinalDataStruct4 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[3]})

    plt.figure()
    swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct1, palette="magma", size=5)
    IMDBScatter = swarm_plot.get_figure()
    IMDBScatter.savefig(Filename+str(1)+".png") 

    plt.figure()
    swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct2, palette="magma", size=5) #alpha=.9
    IMDBScatter = swarm_plot.get_figure()
    IMDBScatter.savefig(Filename+str(2)+".png") 

    plt.figure()
    swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct3, palette="magma", size=5)
    IMDBScatter = swarm_plot.get_figure()
    IMDBScatter.savefig(Filename+str(3)+".png") 

    plt.figure()
    swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct4, palette="magma", size=5)
    IMDBScatter = swarm_plot.get_figure()
    IMDBScatter.savefig(Filename+str(4)+".png") 

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
    

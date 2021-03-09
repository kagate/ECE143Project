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

    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"]
    sns.set(rc={'axes.facecolor': Colors[4], 'figure.facecolor': Colors[4]})

    plt.figure()
    FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1})
    BarChartFig = sns.barplot(x="Streaming Platform", y=Data1Name, data=FinalDataStruct, palette="Blues_d", alpha=.5)
    plt.savefig(Filename)

def movie_scatter_plots(Data1, Data1Name, Filename, Data2=[], Data2Name="", PlotFlag=4):
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
    :param PlotFlag: Specifies how many plots to have on one figure. Can take on value 1 or 4.
    :type Data1: List of lists
    :type Data1Name: String
    :type Filename: String
    :type Data2: List of lists
    :type Data2Name: String
    :type PlotFlag: int
    '''
    assert isinstance(Data1, list), "Data1 must be a list"
    assert isinstance(Data2, list), "Data2 must be a list"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(Data1Name, str), "Data1Name must be a string"
    assert isinstance(Data2Name, str), "Data2Name must be a string"
    assert isinstance(PlotFlag, int), "Data2Name must be a string"
    assert PlotFlag == 1 or PlotFlag == 4, "PlotFlag can only take on values 1 or 4 currently"

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(rc={'figure.figsize':(18, 10)})

    # Create an array with the colors you want to use
    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"] # Jake added Colors[-1] because this is the background of the slides
    # Set your custom color palette
    sns.set_palette(sns.color_palette(Colors))
    # Data1List1 = sum(Data1[0], [])
    # Data1List2 = sum(Data1[2:], [])
    sns.set(rc={'axes.facecolor': Colors[4], 'figure.facecolor': Colors[4]})

    if PlotFlag == 1:
        StreamingPlatform1 = ["Netflix"]*len(Data1[0]) 
        StreamingPlatform2 = ["Hulu"]*len(Data1[1])
        StreamingPlatform3 = ["Prime"]*len(Data1[2])
        StreamingPlatform4 = ["Disney+"]*len(Data1[3])

    if Data2:
        if PlotFlag == 4:
            StreamingPlatform = sum([["Netflix"]*len(Data1[0]), ["Hulu"]*len(Data1[1]), ["Prime"]*len(Data1[2]), ["Disney+"]*len(Data1[3])], [])
            Data1 = sum(Data1, [])
            Data2 = sum(Data2, [])
    # Make data into long-form structure for seaborn plotting
    if PlotFlag == 1:
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
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct1, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(1)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct2, size=5) #alpha=.9
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(2)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct3, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(3)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct4, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        plt.legend(fontsize='15', title_fontsize='20')
        IMDBScatter.savefig(Filename+str(4)+".png") 
    if PlotFlag == 4:
        if Data2:
            FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1, Data2Name: Data2})
            plt.figure()
            swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct, size=5)
            IMDBScatter = swarm_plot.get_figure()
            swarm_plot.set_xlabel("")
            swarm_plot.set_ylabel(Data1Name,fontsize=20)
            swarm_plot.tick_params(labelsize=20)
            plt.legend(fontsize='15', title_fontsize='20')
            IMDBScatter.savefig(Filename+".png") 

def lollipop(NetflixDict, HuluDict, PrimeDict, DisneyDict, Filename):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    
    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"]
    # Create a dataframe
    NetflixDF = pd.DataFrame({'Languages':NetflixDict.keys(), 'values':NetflixDict.values()})
    HuluDF = pd.DataFrame({'Languages':HuluDict.keys(), 'values':HuluDict.values()})
    PrimeDF = pd.DataFrame({'Languages':PrimeDict.keys(), 'values':PrimeDict.values()})
    DisneyDF = pd.DataFrame({'Languages':DisneyDict.keys(), 'values':DisneyDict.values()})
    
    # Reorder it based on the values
    # ordered_df = df.sort_values(by='values')
    fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(2, 2, figsize=[20, 10])
    
    # The horizontal plot is made using the hline function
    # Netflix
    ax1.hlines(y=NetflixDF['Languages'], xmin=0, xmax=NetflixDF['values'], color=Colors[2], linewidth=3)
    ax1.plot(NetflixDF['values'], NetflixDF['Languages'], "o", markerfacecolor=Colors[1], markersize=5)
    # ax1.yticks(NetflixDF['Languages'], FontSize=14)
    # Hulu
    ax2.hlines(y=HuluDF['Languages'], xmin=0, xmax=HuluDF['values'], color=Colors[2], linewidth=3)
    ax2.plot(HuluDF['values'], HuluDF['Languages'], "o", markerfacecolor=Colors[1], markersize=5)
    # Prime
    ax3.hlines(y=PrimeDF['Languages'], xmin=0, xmax=PrimeDF['values'], color=Colors[2], linewidth=3)
    ax3.plot(PrimeDF['values'], PrimeDF['Languages'], "o", markerfacecolor=Colors[1], markersize=5)
    # Diseny
    ax4.hlines(y=DisneyDF['Languages'], xmin=0, xmax=DisneyDF['values'], color=Colors[2], linewidth=3)
    ax4.plot(DisneyDF['values'], DisneyDF['Languages'], "o", markerfacecolor=Colors[1], markersize=5)
    # plt.set_ylabel()

    # Add titles and axis names
    # ax1.yticks(NetflixDF['Languages'])
    # ax1.title("Netflix", labelsize=20)
    # # ax1.xlabel('')
    # ax1.ylabel('Languages', labelsize=20)

    # Show the plot
    plt.savefig("lollipop"+".png") 


    labels = set(sum([list(NetflixDict.keys()), 
                        list(HuluDict.keys()), 
                        list(PrimeDict.keys()), 
                        list(DisneyDict.keys())], []))
    # labels = PrimeDict.keys()
    NetflixVals = [NetflixDict[key] if key in NetflixDict.keys() else 0 for key in labels]
    HuluVals = [HuluDict[key] if key in HuluDict.keys() else 0 for key in labels]
    PrimeVals = [PrimeDict[key] if key in PrimeDict.keys() else 0 for key in labels]
    DisneyVals = [DisneyDict[key] if key in DisneyDict.keys() else 0 for key in labels]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(list(labels), DisneyVals, width, label='Disney')
    ax.bar(list(labels), HuluVals, width, bottom=DisneyVals,label='Hulu')
    ax.bar(list(labels), NetflixVals, width, bottom=np.array(DisneyVals)+np.array(HuluVals), label='Netflix')
    ax.bar(list(labels), PrimeVals, width, bottom=np.array(DisneyVals)+np.array(NetflixVals)+np.array(HuluVals),label='Prime')
    
    ax.set_ylabel('Number of Movies', fontsize=17)
    plt.setp(ax.get_xticklabels(), rotation=47, fontsize=17, ha="right",rotation_mode="anchor")
    ax.set_title('')
    ax.legend()
    plt.savefig(Filename) 

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

    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"]

    ColorChoices = colors.ListedColormap([Colors[0], Colors[2]])
    im1, cbar1 = heatmap(data, row_labels, col_labels, ax=ax,
                    cmap=ColorChoices, cbar_kw=dict(ticks=[0, 1]), cbarlabel="")

    # im2, cbar2 = heatmap(data[30:59], row_labels[30:59], col_labels[30:59], ax=ax2,
    #                 cmap=ColorChoices, cbar_kw=dict(ticks=[0, 1]), cbarlabel="")

    fig.tight_layout()
    fig.savefig(Filename)
    

def make_CM(cm,title):
    plt.imshow(cf,cmap=plt.cm.Blues,interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('Ground truth')
    tick_marks = np.arange(len(set(expectedData))) # length of classes
    class_labels = ['Reject','Accept']
    tick_marks
    plt.xticks(tick_marks,class_labels)
    plt.yticks(tick_marks,class_labels)
    # plotting text value inside cells
    thresh = cf.max() / 2.
    for i,j in itertools.product(range(cf.shape[0]),range(cf.shape[1])):
        plt.text(j,i,f"{cf[i,j]:.2f}",horizontalalignment='center',color='white' if cf[i,j] >thresh else 'black')
    plt.show();

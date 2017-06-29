def run():

    dir_in='INPUT'
    f = str(raw_input("Enter your file name located at INPUT folder: "))
    print "You entered: ------", str(f),' ------'
    lcc_min = int(raw_input("Enter the minimum size of LCC, we recommend a number between 30 and 50: "))
    lcc_max = int(raw_input("Enter the maximum size of LCC, we recommend a number between 300 and 500: "))
    print '.....loading data.....'

    import os
    import pickle
    import numpy as np
    import time
    start_time = time.time()

    id_to_sym = pickle.load(open("DATA/id_to_sym_human.p", "r" ))

    # ------- Read data and keep pval<0.05 and then convert gene name to gene ID ---------
    G = pickle.load(open("DATA/PPI_2015_raw.p", "r" ))
    full_path = os.path.join(dir_in, f)
    file = open(full_path, "r")
    initial_data = file.read().splitlines()
    file.close()

    threshold=0.05
    gene=[];pval=[]

    for row in initial_data:
        n=row.strip().split(',')
        p=float(n[1].strip())
        g=int(n[0].strip())
        if p<=threshold:
            gene.append(g)
            pval.append(p)


    print 'Number of genes with P.val<0.05: ',len(gene)
    print '.....Identifying disease module.....'

    data=zip(gene,pval)
    #---------------------
    from func import CONFINE as conf
    result=conf(data,G,lcc_min,lcc_max)

    z_list=result[0]
    pval_cut_list=result[1]
    sig_Cluster_LCC=result[2]
    z_score=z_list[result[3]]
    p_val_cut=pval_cut_list[result[3]]
    print 'LCC size: ',len(sig_Cluster_LCC.nodes())
    print 'Z-score: ',z_score
    print 'P.val cut-off: ',p_val_cut

    output_name=f.split('.')[0]
    b=open('OUT/LCC_'+output_name+'.txt',"w")
    for node in sig_Cluster_LCC.nodes():
        try:
            print>> b, str(id_to_sym[int(node)])+','+ str(int(node))
        except KeyError:
            print>> b, '    ' + ',' + str(int(node))

    b.close()

    from pylab import plt, matplotlib
    fig=plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)

    #----------------------------------------------------plotting--------

    plt.style.use('ggplot')
    plt.rcParams['text.usetex'] = True

    ax.plot(pval_cut_list,z_list,'o',color='saddlebrown',markersize=4)
    plt.axvline(x=p_val_cut, color='r', linestyle='--')
    ax.set_xlabel('$\mathbf{P.value \ \ cut-off}$',fontsize=30,fontweight='bold',labelpad=18)
    ax.set_ylabel('$\mathbf{Z-Score}$',fontsize=30,fontweight='bold', labelpad=18)
    ax.set_title('$\mathbf{LCC}$'+' = '+str(len(sig_Cluster_LCC.nodes()))+'   ,'+'$\mathbf{Z-Score}$'+' = '+str("{0:.3f}".format(round(z_score,4))))
    ax.grid(True)
    plt.ylim(min(z_list)-min(z_list)/5,max(z_list)+max(z_list)/3)

    font = {'family' : 'Helvetica', 'weight' : 'bold', 'size'   : 20}
    matplotlib.rc('font', **font)
    plt.savefig('OUT/'+output_name+'.png',dpi=150,bbox_inches='tight'); plt.close()
    print("--- %s seconds ---" % (time.time() - start_time))
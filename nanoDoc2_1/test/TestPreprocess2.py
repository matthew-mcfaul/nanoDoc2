
import nanoDoc2_1.preprocess.fast5ToProcessedPq as fast5ToProcessedPq
if __name__ == "__main__":

    # path = '/data/nanopore/IVT/koreaIVT/multifast5_2/workspace'
    # pathout = '/data/nanopore/nanoDoc2_1/SARSCOV2'
    # ref = "/data/nanopore/reference/Cov2_Korea.fa"
    # fmercurrent = "/data/nanopore/signalStatRNA180.txt"
    #
    # path = '/data/nanopore/rRNA/1623_native-multi/multifast5_2/workspace'
    # pathout = '/data/nanopore/nanoDoc2_1/1623_wt'
    # ref = "/data/nanopore/reference/NC000913.fa"
    # fmercurrent = "/data/nanopore/signalStatRNA180.txt"

    path = '/data/nanopore/rRNA/1623_native-multi/multifast5_2/workspace'
    pathout = '/data/nanopore/nanoDoc2_1/1623_wt'
    ref = "/data/nanopore/reference/NC000913.fa"
    fmercurrent = "/data/nanopore/signalStatRNA180.txt"

    path = '/data/nanopore/rRNA/1825_native-multi/multifast5_2/workspace'
    pathout = '/data/nanopore/nanoDoc2_1/1825_native'
    ref = "/data/nanopore/reference/Yeast_sk1.fa"
    fmercurrent = "/data/nanopore/signalStatRNA180.txt"

    MAX_CORE = 24
    qvaluethres = 5
    fast5ToProcessedPq.h5tosegmantedPq(path,pathout,ref,MAX_CORE,qvaluethres,fmercurrent)
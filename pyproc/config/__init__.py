import numpy as np

from config.configure import Configure

conf = Configure()

#== universal
conf.sampling_rate = 44100
conf.duration = 1
conf.hop_length = 347 # to make time steps 128
conf.fmin = 20
conf.fmax = conf.sampling_rate // 2
conf.n_mels = 128
conf.n_fft = conf.n_mels * 20
conf.model = 'mobilenetv2' # 'alexnet'
conf.samples = conf.sampling_rate * conf.duration
conf.num_classes = 2

#== for recognizer
conf.rt_process_count = 1
conf.rt_oversamples = 10
conf.pred_ensembles = 10

#== for trainer
conf.folder = '.'
conf.n_fold = 1
conf.normalize = 'samplewise'
conf.valid_limit = None
conf.random_state = 42
conf.test_size = 0.01
conf.samples_per_file = 5
conf.batch_size = 32
conf.learning_rate = 0.0001
conf.epochs = 500
conf.verbose = 2
conf.dims = (conf.n_mels, 1 + int(np.floor(conf.samples/conf.hop_length)), 1)

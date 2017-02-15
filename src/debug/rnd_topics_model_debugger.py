'''
Created on Jan 30, 2017

This is tests the initialization
of the topic tracking model.

@author: root
'''
from dataset.corpus import SyntheticRndTopicPropsDoc
from model.rnd_topics_segmentor import RndTopicsModel
import debug.debug_tools  as debug_tools
from debug.debug_tools import print_ref_hyp_plots
        
pi = 0.2
alpha = 0.1
beta = 0.1
K = 6
W = 8
n_sents = 200
sentence_l = 15
log_flag = False

'''
doc_synth_tt = SyntheticRndTopicPropsDoc(pi, alpha, beta, K, W, n_sents, sentence_l)
doc_synth_tt.generate_doc()
gamma = 10
rnd_topics_model = RndTopicsModel(gamma, alpha, beta, K, doc_synth_tt, log_flag)
'''

outFile = "debug/rnd_topics_model/rnd_topics_theta_heat_map_initial.png"
'''
debug_tools.test_model_state(rnd_topics_model, outFile)
debug_tools.test_z_ui_sampling(rnd_topics_model)
debug_tools.test_Z_sampling(rnd_topics_model, outFile)
debug_tools.test_rho_sampling(rnd_topics_model, outFile)
'''

log_file = "logging/Sampler.log"
'''
n_iter = 500
burn_in = 0
lag = 0
debug_tools.run_gibbs_sampler(rnd_topics_model, n_iter, burn_in, lag, log_file)
'''

plot_dir = "debug/rnd_topics_model/ref_hyp_plots/"
print_ref_hyp_plots(log_file, plot_dir, "RndTopics")
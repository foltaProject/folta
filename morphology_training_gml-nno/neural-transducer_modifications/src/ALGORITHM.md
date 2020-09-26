# Neural Transducer


## Goal


The goal is to train models capable of generating morphological inflections for a given word stem, and POS tags. 


## hyperparameters

for language to train

LANG= aka ang azg ceb cly cpa ctp czn dan deu eng est fin frr gaa gmh hil isl izh kon krl lin liv lug mao mdf mhr mlg myv nld nob nya ote otm pei sme sot swa swe tgl vep vot xty zpv zul

* bash example/sigmorphon2020-shared-tasks/task0-launch.sh

for train.py || overall training file

* '--dataset', required=True, type=Data
	+ choices=['g2p', 'p2g', 'news15', 'histnorm', 'lemma', 'lemmanotag', 'lematus', 'unimorph', 'sigmorphon[16-19]task1']
* '--max_seq_len', default=128, type=int
* '--max_decode_len', default=128, type=int
* '--init', default='', help='control initialization'
* '--dropout', default=0.2, type=float, help='dropout prob'
* '--embed_dim', default=100, type=int, help='embedding dimension'
* '--nb_heads', default=4, type=int, help='number of attention head'
* '--src_layer', default=1, type=int, help='source encoder number of layers'
* '--trg_layer', default=1, type=int, help='target decoder number of layers'
* '--src_hs', default=200, type=int, help='source encoder hidden dimension'
* '--trg_hs', default=200, type=int, help='target decoder hidden dimension'
* '--label_smooth', default=0., type=float, help='label smoothing coeff'
* '--tie_trg_embed', default=False, action='store_true', help='tie decoder input & output embeddings'
* '--arch', required=True, type=Arch
	+ choices=['soft', 'hard', 'approxihard', 'softinputfeed', largesoftinputfeed', 'approxihardinputfeed', 'hardmono', 'hmm', 'hmmfull', 'transformer', 'universaltransformer', tagtransformer', taguniversaltransformer']
* '--nb_sample', default=2, type=int, help='number of sample in REINFORCE approximation'
* '--wid_siz', default=11, type=int, help='maximum transition in 1st-order hard attention'
* '--indtag', default=False,maction='store_true', help='separate tag from source string'
* '--decode', default=Decode.greedy, type=Decode, choices=['greedy', 'sample', 'beam']
* '--mono', default=False, action='store_true', help='enforce monotonicity'
* '--bestacc', default=False, action='store_true', help='select model by accuracy only'

for trainer.py || individual training file

* '--seed', default=0, type=int
* '--train', required=True, type=str, nargs='+'
* '--dev', required=True, type=str, nargs='+'
* '--test', default=None, type=str, nargs='+'
* '--model', required=True, help='dump model filename'
* '--load', default='', help='load model and continue training; with `smart`, recover training automatically'
* '--bs', default=20, type=int, help='training batch size'
* '--epochs', default=20, type=int, help='maximum training epochs'
* '--max_steps', default=0, type=int, help='maximum training steps'
* '--warmup_steps', default=4000, type=int, help='number of warm up steps'
* '--total_eval', default=-1, type=int, help='total number of evaluation'
* '--optimizer', default=Optimizer.adam, type=Optimizer
	+ choices=['sgd', 'adadelta', 'adam', 'amsgrad']
* '--scheduler', default=Scheduler.reducewhenstuck, type=Scheduler
	+ choices=['reducewhenstuck', 'warmupinvsqr']
* '--lr', default=1e-3, type=float, help='learning rate'
* '--min_lr', default=1e-5, type=float, help='minimum learning rate'
* '--momentum', default=0.9, type=float, help='momentum of SGD'
* '--beta1', default=0.9, type=float, help='beta1 of Adam'
* '--beta2', default=0.999, type=float, help='beta2 of Adam'
* '--estop', default=1e-8, type=float, help='early stopping criterion'
* '--cooldown', default=0, type=int, help='cooldown of `ReduceLROnPlateau`'
* '--patience', default=0, type=int, help='patience of `ReduceLROnPlateau`'
* '--discount_factor', default=0.5, type=float, help='discount factor of `ReduceLROnPlateau`'
* '--max_norm', default=0, type=float, help='gradient clipping max norm'
* '--gpuid', default=[], nargs='+', type=int, help='choose which GPU to use'
* '--loglevel', default='info', choices=['info', 'debug']
* '--saveall', default=False, action='store_true', help='keep all models'
* '--shuffle', default=False, action='store_true', help='shuffle the data'
* '--cleanup_anyway', default=False, action='store_true', help='cleanup anyway'

## Algorithm

Data Manipulation || task0-build-dataset.py

* data halluication 
* stores data as
	+ <lang>.trn
	+ <lang>.tst
	+ <lang>.dev (?)
	+ <lang>.hall

Setup Training || train.py

* set parameters
* load data -- calls dataloader.py
* IF model has been trained:
	+ load model
	+ load training parameters
* ELSE start from scratch:
	+ build model
* train model at given epoch -- calls train.py

Training At Given Epoch || train.py

* checklist for proper run
* calc how many epochs (times to iterate training)
	+ evaluate model every epoch (unless changed)
* train model for each [transformer, mono-hmm, hall-transformer, hall-mono-hmm]
	+ iterate word batch
	+ math -> decode -- calls decoding.py
	+ calculate loss
	+ optimize model
* evaluate model
	+ IF difference of previous loss and current loss is within threshold
		- stop training at given epoch
	+ ELSE difference is not within threshold
		- continue training
* save model
	+ {lang}.nll_{devloss}.{evaluation}.{epoch index}
* save training
* cleanup models if finished (or if changed)


from h1st.contrib.quality.neuron_coverage import TFNeuronCoverage1, TFNeuronCoverage2
from en2spa_transformer import En2SpaSeq2SeqTransformer

def test_neuron_coverage_1():
    model = En2SpaSeq2SeqTransformer()
    train_pairs, val_pairs, test_pairs = model.load_data()
    nc1 = TFNeuronCoverage1()
    nc1.gen_diff(seeds=test_pairs, model=model)


def test_neuron_coverage_2():
    model = En2SpaSeq2SeqTransformer()
    train_pairs, val_pairs, test_pairs = model.load_data()
    nc1 = TFNeuronCoverage2()
    nc1.gen_diff(seeds=test_pairs, model=model)

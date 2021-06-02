from en2spa_transformer import En2SpaSeq2SeqTransformer

def test_train():
    model = En2SpaSeq2SeqTransformer()
    model_version = 'v2'
    train_pairs, val_pairs, _ = model.load_data(verbose=False)
    train_ds, val_ds = model.prep_data(data=(train_pairs, val_pairs))

    model.train(data=(train_ds, val_ds), epochs=20)
    model.persist(model_version)

def test_accuracy_1():
    model = En2SpaSeq2SeqTransformer()
    model_version = 'v2'
    model.load(model_version)

    ret = []
    for _ in range(100):
        r = model.predict('Hello')
        print(r)
        ret.append(r)

    print(sum(['hola' in r for r in ret]))
from h1st_ai.models import MyModel


def run():
    model = MyModel()

    train_data, val_data, _ = model.load_data()
    train_ds, val_ds = model.prep_data(data=(train_data, val_data))

    model.train(data=(train_ds, val_ds))

    model.persist('v1')

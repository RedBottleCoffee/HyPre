from keras.models import load_model

def main():
    model = load_model('model/alexnet.h5')


if __name__ == '__main__':
    main()

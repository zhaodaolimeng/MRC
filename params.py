#coding=utf-8

class Params():

    # model: ('r_net', 'mnemonic_reader', 'transformer')
    model = 'r_net'

    # data
    data_dir = "./data/"
    train_dir = data_dir + "trainset/"
    dev_dir = data_dir + "devset/"
    logdir = "./data/train"
    logdir_r_net = './data/train_r_net'
    logdir_transformer = './data/train_transformer'
    glove_dir = "./data/glove.840B.300d.txt"
    glove_char = "./data/char_embedding.txt"

    # Data dir
    target_dir = "indices.txt"
    q_word_dir = "words_questions.txt"
    q_chars_dir = "chars_questions.txt"
    c_word_dir = "words_context.txt"
    c_chars_dir = "chars_context.txt"

    max_c_len = 300  # Maximum number of words in each passage context
    max_q_len = 30  # Maximum number of words in each question context
    max_char_len = 25  # Maximum number of characters in a word
    c_time_step = 300
    q_time_step = 30
    char_vocab_size = 95
    word_vocab_size = 73601

    mode = 'train'
    lr = 0.0005
    emb_size = 300
    size = 100
    batch_size = 32
    max_run_steps = 5000000
    steps_per_checkpoint = 100
    num_gpus = 1
    max_grad_norm = 5.0
    num_layers = 3
    dropout_rate = 0.2

    T = 2
    L = 2
    Lambda = 0.01
    RL = False  # reinforcement learning
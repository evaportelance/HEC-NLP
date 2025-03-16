from collections import Counter
import torch
from torch.utils.data import Dataset


class Tokenizer:
    def __init__(
        self, data, vocab_size=2000, pad="<PAD>", bos="<BOS>", eos="<EOS>", unk="<UNK>"
    ):
        self.data = data
        self.vocab_size = vocab_size
        self.pad = pad
        self.bos = bos
        self.eos = eos
        self.unk = unk
        self.vocabulary = {
            pad: 0,
            bos: 1,
            eos: 2,
            unk: 3,
        }
        self._create_vocab(data, vocab_size)
        self.pad_idx = self.token_to_idx(pad)
        self.bos_idx = self.token_to_idx(bos)
        self.eos_idx = self.token_to_idx(eos)
        self.unk_idx = self.token_to_idx(unk)

    def _create_vocab(self, data, vocab_size):
        counts = Counter([token for sent in data for token, _ in sent])
        vocab = {
            token: idx + len(self.vocabulary)
            for idx, (token, _) in enumerate(counts.most_common(vocab_size))
        }
        self.vocabulary = {
            **self.vocabulary,
            **vocab,
        }  # merge vocab with existing vocabulary
        self.idx_to_tokens = {v: k for k, v in self.vocabulary.items()}

    def tokens_to_indices(self, tokens):
        return [
            self.vocabulary[token] if token in self.vocabulary else self.unk_idx
            for token in tokens
        ]

    def indices_to_tokens(self, indices):
        if isinstance(indices, torch.Tensor):
            indices = indices.tolist()
        return [self.idx_to_tokens[idx] for idx in indices]

    def token_to_idx(self, token):
        return self.vocabulary[token]

    def idx_to_token(self, idx):
        return self.idx_to_tokens[idx]
    
    def encode(self, text, add_special_tokens=True):
        tokens = text.split()
        if add_special_tokens:
            tokens = [self.bos] + tokens + [self.eos]
        return self.tokens_to_indices(tokens)


class SentenceDataset(Dataset):
    def __init__(self, sentences, tokenizer):
        self.sentences = sentences
        self.tokenizer = tokenizer
        self.indexed_sentences = []
        self._create_indexed_sentences()

    def __getitem__(self, idx):
        sent = self.indexed_sentences[idx]
        return torch.tensor(sent, dtype=torch.long)

    def __len__(self):
        return len(self.indexed_sentences)

    def _create_indexed_sentences(self):
        for sent in self.sentences:
            indexed_sent = []
            for token, _ in sent:
                token_idx = (
                    self.tokenizer.token_to_idx(token)
                    if token in self.tokenizer.vocabulary
                    else self.tokenizer.unk_idx
                )
                indexed_sent.append(token_idx)
            indexed_sent = (
                [self.tokenizer.bos_idx] + indexed_sent + [self.tokenizer.eos_idx]
            )
            self.indexed_sentences.append(indexed_sent)


def collate_fn(items, tokenizer, max_len=None, pad="right"):
    assert pad in ["right", "left"]

    inputs = items
    if max_len is None:
        max_len = max([len(sent) for sent in inputs])

    batched_inputs = []
    for sent in inputs:
        truncate = len(sent) > max_len
        if truncate:
            sent = sent[:max_len]
        n_pads = max_len - len(sent)
        pads = torch.ones(n_pads, dtype=torch.long) * tokenizer.pad_idx
        if pad == "right":
            pad_sent = torch.cat((sent, pads))
        elif pad == "left":
            pad_sent = torch.cat((pads, sent))
        batched_inputs.append(pad_sent)

    batched_inputs = torch.stack(batched_inputs)

    return batched_inputs

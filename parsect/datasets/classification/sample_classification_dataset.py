from parsect.datasets.sprinkle_dataset import sprinkle_dataset
from parsect.datasets.classification.base_text_classification import (
    BaseTextClassification,
)
from typing import Dict, Any, Optional, Union, List
from parsect.vocab.vocab import Vocab
from torch.utils.data import Dataset
import torch
from parsect.tokenizers.word_tokenizer import WordTokenizer


@sprinkle_dataset()
class sample_classification_dataset(Dataset, BaseTextClassification):
    def __init__(
        self,
        filename: str,
        dataset_type: str,
        max_num_words: int,
        max_instance_length: int,
        debug: bool = False,
        debug_dataset_proportion=0.1,
        word_embedding_type: Optional[str] = "random",
        word_embedding_dimension: Optional[int] = "100",
        word_start_token: str = "<SOS>",
        word_end_token: str = "<EOS>",
        word_pad_token: str = "<PAD>",
        word_unk_token: str = "<UNK>",
        train_size: float = 0.8,
        test_size: float = 0.2,
        validation_size: float = 0.5,
        word_tokenizer=WordTokenizer(),
        word_tokenization_type="vanilla",
    ):
        pass

    def __len__(self):
        return len(self.word_instances)

    def __getitem__(self, idx) -> Dict[str, Any]:
        pass

    def get_lines_labels(self, filename: str) -> (List[str], List[str]):
        pass

    @classmethod
    def get_classname2idx(cls) -> Dict[str, int]:
        pass

    def get_num_classes(self) -> int:
        pass

    def get_class_names_from_indices(self, indices: List) -> List[str]:
        pass

    def get_disp_sentence_from_indices(self, indices: List) -> str:
        pass

    def get_preloaded_word_embedding(self) -> torch.FloatTensor:
        pass

    def emits_keys(cls):
        pass

    @classmethod
    def get_iter_dict(
        cls,
        lines: Union[List[str], str],
        word_vocab: Vocab,
        word_tokenizer: WordTokenizer,
        max_word_length: int,
        word_add_start_end_token: bool,
        labels: Optional[Union[str, List[str]]] = None,
    ):
        pass

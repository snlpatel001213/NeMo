from dataclasses import dataclass
from typing import Any

from omegaconf.omegaconf import MISSING
from pytorch_lightning.trainer.trainer import Trainer

from nemo.collections.nlp.models.nlp_model import NLPModel
from nemo.collections.nlp.modules.common.decoder_module import DecoderModule
from nemo.collections.nlp.modules.common.encoder_module import EncoderModule
from nemo.collections.nlp.modules.common.tokenizer_utils import TokenizerConfig, get_tokenizer
from nemo.core.config.modelPT import ModelConfig


@dataclass
class EncDecNLPModelConfig(ModelConfig):
    encoder_tokenizer: TokenizerConfig = MISSING
    decoder_tokenizer: TokenizerConfig = MISSING
    encoder: Any = MISSING
    decoder: Any = MISSING
    head: Any = MISSING


class EncDecNLPModel(NLPModel):
    """Base class for encoder-decoder NLP models.
    """

    def __init__(self, cfg: EncDecNLPModelConfig, trainer: Trainer = None):
        super().__init__(cfg=cfg, trainer=trainer)

    @property
    def encoder_vocab_size(self):
        return self.encoder_tokenizer.vocab_size

    @property
    def decoder_vocab_size(self):
        return self.decoder_tokenizer.vocab_size

    @property
    def encoder_tokenizer(self):
        return self._encoder_tokenizer

    @encoder_tokenizer.setter
    def encoder_tokenizer(self, tokenizer):
        self._encoder_tokenizer = tokenizer

    @property
    def decoder_tokenizer(self):
        return self._decoder_tokenizer

    @decoder_tokenizer.setter
    def decoder_tokenizer(self, tokenizer):
        self._decoder_tokenizer = tokenizer

    @property
    def encoder(self) -> EncoderModule:
        return self._encoder

    @encoder.setter
    def encoder(self, encoder):
        self._encoder = encoder

    @property
    def decoder(self) -> DecoderModule:
        return self._decoder

    @decoder.setter
    def decoder(self, decoder):
        self._decoder = decoder


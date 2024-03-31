import pathlib
from dataclasses import dataclass

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Once the model is trained, you can use it to classify text snippets extracted from PDF files
# For each text snippet extracted from the PDF:
# 1. Preprocess the text
# 2. Tokenize and pad the sequence
# 3. Use the trained model to predict whether it's a SCPI command or not
# 4. Generate a list of SCPI commands based on the predictions


class ModelSaveError:
    pass


@dataclass
class Sequence:
    sequence: tf.keras.utils.Sequence
    padded_sequences: tf.keras.utils.pad_sequences
    max_length: int


class ModelSCPI:
    def __init__(self, text: list) -> None:
        self.text = text
        self.tokenizer = Tokenizer()

        self.sequence = Sequence()

    def tokenize_text(self) -> None:
        self.tokenizer.fit_on_texts([data[0] for data in self.text])

    def sequence_text(self) -> None:
        # Convert text to sequences
        self.sequence.sequence = self.tokenizer.texts_to_sequences(
            [data[0] for data in self.text]
        )

    def pad_text(self) -> None:
        # Pad sequences to ensure uniform length
        self.sequence.max_length = max([len(seq) for seq in self.sequence])
        self.sequence.padded_sequences = pad_sequences(
            self.sequence, maxlen=self.sequence.max_length, padding="post"
        )

    def define_model(self) -> None:
        # Define a simple neural network model using TensorFlow
        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Embedding(
                    input_dim=len(self.tokenizer.word_index) + 1,
                    output_dim=64,
                    input_length=self.sequence.max_length,
                ),
                tf.keras.layers.GlobalAveragePooling1D(),
                tf.keras.layers.Dense(64, activation="relu"),
                tf.keras.layers.Dense(1, activation="sigmoid"),
            ]
        )

    def compile_model(self) -> None:
        # Compile the model
        self.model.compile(
            optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
        )

    def train_model(self) -> None:
        # Prepare data for training
        X_train = self.sequence.padded_sequences
        y_train = np.array([data[1] for data in self.text])

        # Train the model (replace X_train and y_train with your actual dataset)
        self.model.fit(X_train, y_train, epochs=10, validation_split=0.2)

    def save_model(self, dir_path: pathlib.Path) -> bool:

        suscces = self.model.save(dir_path)
        if suscces:
            return True
        else:
            raise ModelSaveError

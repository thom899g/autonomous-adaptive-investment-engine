import numpy as np
from tensorflow.keras import layers, Model

class LSTMForecaster:
    """Implements an LSTM-based model for time series forecasting.
    
    Attributes:
        input_shape: Shape of the input data.
        units: Number of units in the LSTM layer.
    """
    
    def __init__(self, input_shape: tuple, units: int = 64):
        self.input_shape = input_shape
        self.units = units
        
    def build_model(self) -> Model:
        """Builds and compiles the LSTM model.
        
        Returns:
            Compiled Keras Model.
        """
        model = self._build()
        model.compile(optimizer='adam', loss='mse')
        return model
    
    def _build(self) -> Model:
        """Constructs the model architecture."""
        input_layer = layers.Input(shape=self.input_shape)
        lstm_layer = layers.LSTM(self.units, return_sequences=True)(input_layer)
        dropout_layer = layers.Dropout(0.2)(lstm_layer)
        dense_layer = layers.Dense(1)(dropout_layer)
        model = Model(inputs=input_layer, outputs=dense_layer)
        return model
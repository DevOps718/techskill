import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from pandas.core.arrays.base import (
    ExtensionArray as ExtensionArray,
    ExtensionOpsMixin as ExtensionOpsMixin,
)
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from typing import Union

class PandasDtype(ExtensionDtype):
    def __init__(self, dtype) -> None: ...
    @property
    def numpy_dtype(self): ...
    @property
    def name(self): ...
    @property
    def type(self): ...
    @classmethod
    def construct_from_string(cls, string): ...
    @classmethod
    def construct_array_type(cls): ...
    @property
    def kind(self): ...
    @property
    def itemsize(self): ...

class PandasArray(ExtensionArray, ExtensionOpsMixin, NDArrayOperatorsMixin):
    __array_priority__: int = ...
    def __init__(
        self, values: Union[np.ndarray, PandasArray], copy: bool = ...
    ) -> None: ...
    @property
    def dtype(self): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...
    def __getitem__(self, item): ...
    def __setitem__(self, key, value) -> None: ...
    def __len__(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    def isna(self): ...
    def fillna(self, value=..., method=..., limit=...): ...
    def take(self, indices, allow_fill: bool = ..., fill_value=...): ...
    def copy(self): ...
    def unique(self): ...
    def any(self, axis=..., out=..., keepdims: bool = ..., skipna: bool = ...): ...
    def all(self, axis=..., out=..., keepdims: bool = ..., skipna: bool = ...): ...
    def min(self, axis=..., out=..., keepdims: bool = ..., skipna: bool = ...): ...
    def max(self, axis=..., out=..., keepdims: bool = ..., skipna: bool = ...): ...
    def sum(
        self,
        axis=...,
        dtype=...,
        out=...,
        keepdims: bool = ...,
        initial=...,
        skipna: bool = ...,
        min_count: int = ...,
    ): ...
    def prod(
        self,
        axis=...,
        dtype=...,
        out=...,
        keepdims: bool = ...,
        initial=...,
        skipna: bool = ...,
        min_count: int = ...,
    ): ...
    def mean(
        self, axis=..., dtype=..., out=..., keepdims: bool = ..., skipna: bool = ...
    ): ...
    def median(
        self,
        axis=...,
        out=...,
        overwrite_input: bool = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def std(
        self,
        axis=...,
        dtype=...,
        out=...,
        ddof: int = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def var(
        self,
        axis=...,
        dtype=...,
        out=...,
        ddof: int = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def sem(
        self,
        axis=...,
        dtype=...,
        out=...,
        ddof: int = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def kurt(
        self, axis=..., dtype=..., out=..., keepdims: bool = ..., skipna: bool = ...
    ): ...
    def skew(
        self, axis=..., dtype=..., out=..., keepdims: bool = ..., skipna: bool = ...
    ): ...
    def to_numpy(self, dtype=..., copy: bool = ..., na_value=...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def __invert__(self): ...
